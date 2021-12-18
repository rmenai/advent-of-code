import logging

from aoc.utils.parsers import get_data

log = logging.getLogger(__name__)


def solve(depths: list[int]) -> int:
    """Determine how many three-measurement sums are larger than the previous sum."""
    larger_measurements = 0

    # Get the first sum.
    past_sum = depths[0] + depths[1] + depths[2]

    for i in range(1, len(depths) - 2):
        current_sum = depths[i] + depths[i + 1] + depths[i + 2]

        if current_sum > past_sum:
            larger_measurements += 1

        past_sum = current_sum  # Update the past sum.

    return larger_measurements


if __name__ == "__main__":
    # Fetch the puzzle's input.
    DEPTHS: list[int] = get_data(2021, 1, func=int, split=True)

    # Solve the puzzle.
    result = solve(DEPTHS)

    print("--- Part Two ---")
    print(f"There are {result} three-measurement sums larger than the previous sum.")
