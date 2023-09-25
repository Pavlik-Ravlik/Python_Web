from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi_limiter import FastAPILimiter

import uvicorn
import redis.asyncio as redis

from ipaddress import ip_address
from typing import Callable

from src.routes import contacts, auth, users
from src.conf.config import settings

app = FastAPI()

origins = [ 
    "http://localhost:8000"
    ]
banned_ips = [ip_address("193.168.1.1"), ip_address("192.168.1.2")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(contacts.router, prefix='/contacts')
app.include_router(auth.router, prefix='/contacts')
app.include_router(users.router, prefix='/contacts')


@app.middleware("http")
async def ban_ips(request: Request, call_next: Callable):
    ip = ip_address(request.client.host)
    
    if ip in banned_ips:
        return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={"detail": "You are banned"})
    
    response = await call_next(request)
    return response


@app.on_event("startup")
async def startup():
    '''Information caching function'''
    r = await redis.Redis(host=settings.redis_host, port=settings.redis_port, db=0, encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(r)


@app.get("/")
def read_root():
    '''main page'''
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
