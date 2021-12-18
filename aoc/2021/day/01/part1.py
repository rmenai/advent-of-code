import logging

from aoc.utils.parsers import get_data

log = logging.getLogger(__name__)


def solve(depths: list[int]) -> int:
    """Determine how many measurements are larger than the previous one."""
    larger_measurements = 0

    for i, depth in enumerate(depths):
        if i == 0:
            log.debug(f"Skipping index 0, depth {depth}")
            continue

        if depths[i - 1] < depth:
            larger_measurements += 1

    return larger_measurements


if __name__ == "__main__":
    # Fetch the puzzle's input.
    DEPTHS: list[int] = get_data(2021, 1, func=int, split=True)

    # Solve the puzzle.
    result = solve(DEPTHS)

    print("--- Day 1: Sonar Sweep ---")
    print(f"There are {result} measurements larger then their previous measurement.")
    print()
