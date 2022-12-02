import logging

from aoc.utils.parsers import get_data

log = logging.getLogger(__name__)


def solve(inventories: list[list[int]]) -> int:
    """Determine how many calories are in the most calorific inventory."""
    return max(sum(inventory) for inventory in inventories)


if __name__ == "__main__":
    # Fetch the puzzle's input.

    CALORIES: list[list[int]] = get_data(
        2022, 1,
        func=lambda raw: [[int(calories) for calories in inv.splitlines()] for inv in raw.split("\n\n")]
    )

    # Solve the puzzle.
    result = solve(CALORIES)

    print("--- Day 1: Calorie Counting ---")
    print(f"The Elf carrying the most calories is carrying {result} calories.")
    print()
