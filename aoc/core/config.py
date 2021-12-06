from pydantic import BaseSettings


class Global(BaseSettings):
    """The aoc settings."""

    debug: bool = False
    aoc_session: str

    class Config:
        """The Pydantic settings configuration."""

        env_file = ".env"


settings = Global()
