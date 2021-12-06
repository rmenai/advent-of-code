import logging

from aoc.utils.parsers import get_data

log = logging.getLogger(__name__)

DEPTHS = get_data(2021, 1, func=int, split=True)

result: int = 0

# Get the value of window A first.
compare_value = DEPTHS[0] + DEPTHS[1] + DEPTHS[2]

# Loop through the starting indices of each following window.
for index in range(1, len(DEPTHS) - 2):
    current_sum = DEPTHS[index] + DEPTHS[index + 1] + DEPTHS[index + 2]

    if current_sum > compare_value:
        result += 1

    compare_value = current_sum  # Store the current sum to compare next.

if __name__ == "__main__":
    # print("--- Day 1: Sonar Sweep ---")
    print("--- Part Two ---")
    print(f"There are {result} three-measurement sums larger then their previous sum.")
