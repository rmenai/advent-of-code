import logging

from aoc.utils.parsers import get_data

log = logging.getLogger(__name__)


def solve(instructions: list[tuple[str, int]]) -> int:
    """Calculate the final horizontal position and the final depth and multiply them together."""
    horizontal, depth, aim = 0, 0, 0

    # Execute all instructions.
    for command, units in instructions:
        if command == "forward":
            horizontal += units
            depth += aim * units
        elif command == "down":
            aim += units
        elif command == "up":
            aim -= units
        else:
            log.error(f"Unexpected instruction {command} {units}")

    return horizontal * depth


def parse(line: str) -> tuple[str, int]:
    """Parse a line from the input."""
    command, units = line.split()
    return command, int(units)


if __name__ == "__main__":
    # Fetch the puzzle's input.
    INSTRUCTIONS: list[tuple[str, int]] = get_data(2021, 2, func=parse, split=True)

    # Solve the puzzle.
    result = solve(INSTRUCTIONS)

    print("--- Part Two ---")
    print(f"If I multiply the final horizontal position by the final depth I get {result}.")
