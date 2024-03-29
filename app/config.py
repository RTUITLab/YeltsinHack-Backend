from pydantic import BaseSettings


class Settings(BaseSettings):
    # database settings
    database_url: str = "sqlite:///./sql_app.db"

    # main app settings
    debug_mode: bool = False

    # proxy settings
    root_path: str = ''

    class Config:
        env_file = ".env"
