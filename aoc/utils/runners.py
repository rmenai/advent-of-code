import logging
import subprocess
from typing import Any

from aoc.core import constants

log = logging.getLogger(__name__)


def run_puzzle(year: int, day: int, part: int = None) -> Any:
    """Get and run a specific puzzle.

    Args:
        year (int): The event year.
        day (int): The challenge day.
        part (int): The part of the puzzle (1 or 2).
    """
    if part is None:
        # Run part 1.
        file = f"{constants.root}/{year}/day/{day:02}/part1.py"
        subprocess.run(["python", file])

        # Run part 2.
        file = f"{constants.root}/{year}/day/{day:02}/part2.py"
        subprocess.run(["python", file])
    else:
        file = f"{constants.root}/{year}/day/{day:02}/part{part}.py"
        subprocess.run(["python", file])
