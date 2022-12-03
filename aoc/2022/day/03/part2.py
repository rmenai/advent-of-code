import logging
from functools import reduce
from string import ascii_letters

from aoc.utils.parsers import get_data

log = logging.getLogger(__name__)


def solve(sacks: list[tuple[str]]) -> int:
    """Determine the sum of the priorities of the item types in the sacks."""
    return sum([ascii_letters.index(reduce(lambda a, b: set(a) & set(b), sack).pop()) + 1 for sack in sacks])

def parse(raw: str) -> list[tuple[str]]:
    """Parse the raw data into a list of tuples of 3 strings."""
    split_data = raw.splitlines()
    return [(split_data[i], split_data[i + 1], split_data[i + 2]) for i in range(0, len(split_data), 3)]

if __name__ == "__main__":
    # Fetch the puzzle's input.
    SACKS: list[tuple[str]] = get_data(2022, 3, func=parse)

    # Solve the puzzle.
    result = solve(SACKS)

    print("--- Day 3: Rucksack Reorganization ---")
    print(f"The sum of the priorities of the item types is {result}.")
    print()
