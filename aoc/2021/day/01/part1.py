import logging

from aoc.utils.parsers import get_data

log = logging.getLogger(__name__)

DEPTHS = get_data(2021, 1, func=int, split=True)

result: int = 0

for index, depth in enumerate(DEPTHS):
    if index == 0:
        log.debug(f"Skipping index 0, depth {depth}")
        continue

    if DEPTHS[index - 1] < depth:
        result += 1

if __name__ == "__main__":
    print("--- Day 1: Sonar Sweep ---")
    print(f"There are {result} sums larger then their previous sum.")
    print()
