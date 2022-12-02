import logging

from aoc.utils.parsers import get_data

log = logging.getLogger(__name__)


def solve(inventories: list[list[int]]) -> int:
    """Determine how many calories are in the top 3 most calorific inventories."""
    return sum(sorted([sum(inventory) for inventory in inventories], reverse=True)[:3])


if __name__ == "__main__":
    # Fetch the puzzle's input.

    CALORIES: list[list[int]] = get_data(
        2022, 1,
        func=lambda raw: [[int(calories) for calories in inv.splitlines()] for inv in raw.split("\n\n")]
    )

    # Solve the puzzle.
    result = solve(CALORIES)

    print("--- Part Two ---")
    print(f"The top 3 Elves carrying the most calories are carrying {result} calories in total.")
    print()
