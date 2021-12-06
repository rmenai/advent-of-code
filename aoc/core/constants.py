from pydantic import BaseModel


class Constants(BaseModel):
    """The aoc constants."""

    aoc_url: str = "https://adventofcode.com/{year}/day/{day}"
    root: str = __name__.split(".")[0]


constants = Constants()
