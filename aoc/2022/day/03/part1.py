import logging
from string import ascii_letters

from aoc.utils.parsers import get_data

log = logging.getLogger(__name__)


def solve(sacks: list[str]) -> int:
    """Determine the sum of the priorities of the item types in the sacks."""
    return sum([ascii_letters.index((set(sack[:len(sack) // 2]) & set(sack[len(sack) // 2:])).pop()) + 1 for sack in sacks])


if __name__ == "__main__":
    # Fetch the puzzle's input.
    SACKS: list[str] = get_data(2022, 3, split=True)

    # Solve the puzzle.
    result = solve(SACKS)

    print("--- Day 3: Rucksack Reorganization ---")
    print(f"The sum of the priorities of the item types is {result}.")
    print()
