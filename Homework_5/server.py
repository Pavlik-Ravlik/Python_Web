import asyncio
import logging
import websockets
import names
from websockets import WebSocketServerProtocol
from websockets.exceptions import ConnectionClosedOK
from main_py import get_currency_rates, get_exchange_rates

logging.basicConfig(level=logging.INFO)


class Server:
    clients = set()

    async def register(self, ws: WebSocketServerProtocol):
        ws.name = names.get_full_name()
        self.clients.add(ws)
        logging.info(f'{ws.remote_address} connects')


    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.remove(ws)
        logging.info(f'{ws.remote_address} disconnects')


    async def send_to_clients(self, message: str):
        if self.clients:
            [await client.send(message) for client in self.clients]


    async def ws_handler(self, ws: WebSocketServerProtocol):
        await self.register(ws)
        
        try:
            await self.distrubute(ws)
        
        except ConnectionClosedOK:
            pass
        
        finally:
            await self.unregister(ws)


    async def distrubute(self, ws: WebSocketServerProtocol):
        async for message in ws:
            if message == 'exchange':
                rates = get_currency_rates(1, '')
                formatted_rates = ""
                
                for rate in rates:
                    
                    for date, currencies in rate.items():
                        formatted_rates += f"{date}:\n"
                        
                        for currency, values in currencies.items():
                            formatted_rates += f"  {currency}:\n"
                            formatted_rates += f"    Sale: {values['sale']}\n"
                            formatted_rates += f"    Purchase: {values['purchase']}\n"
                await self.send_to_clients(f"{ws.name}:\n{formatted_rates}")
            
            else:
                await self.send_to_clients(f"{ws.name}: {message}")


async def main():
    server = Server()
    
    async with websockets.serve(server.ws_handler, 'localhost', 8080):
        await asyncio.Future()  # run forever


if __name__ == '__main__':
    asyncio.run(main())