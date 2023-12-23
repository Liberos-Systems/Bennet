from pydantic import BaseSettings

class Settings(BaseSettings):
    version: str = "0.0.3"
    debug: bool = True

# load and parse settings
settings = Settings()

# access variables
version = settings.version
debug = settings.debug
