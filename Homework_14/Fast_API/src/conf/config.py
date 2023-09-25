from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_user: str = 'postgres'
    password: str = 'Zasobi2007'
    port: int = '5432'
    db_name: str = 'fast_app'
    sqlalchemy_database_url: str = 'postgresql+psycopg2://postgres:Zasobi2007@localhost:5432/fast_app'
    secret_key: str = 'secret_key'
    algorithm: str = 'HS256'
    mail_username: str = 'pastet1990@meta.ua'
    mail_password: str = 'Zasobi2007'
    mail_from: str = "pastet1990@meta.ua"
    mail_port: int = '465'
    mail_server: str = 'smtp.meta.ua'
    redis_host: str = 'localhost'
    redis_port: int = 6379
    cloudinary_name: str = 'dfnnqtknu'
    cloudinary_api_key: str = '386221182173588'
    cloudinary_api_secret: str = 'oW4ly_zJa2SVMB8oHlZSU8erDn4'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()