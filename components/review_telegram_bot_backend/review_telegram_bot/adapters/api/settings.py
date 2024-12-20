from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    telegram_token: str
    huggingface_hub_token: str

    class Config:
        env_file = ".env"
