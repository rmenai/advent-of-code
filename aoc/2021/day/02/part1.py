import logging

from aoc.utils.parsers import get_data

log = logging.getLogger(__name__)


def solve(instructions: list[tuple[str, int]]) -> int:
    """Calculate the final horizontal position and the final depth and multiply them together."""
    horizontal, depth = 0, 0

    # Execute all instructions.
    for command, value in instructions:
        if command == "forward":
            horizontal += value
        elif command == "down":
            depth += value
        elif command == "up":
            depth -= value
        else:
            log.error(f"Unexpected instruction {command} {value}")

    return horizontal * depth


def parse(line: str) -> tuple[str, int]:
    """Parse a line from the input."""
    command, value = line.split()
    return command, int(value)


if __name__ == "__main__":
    # Fetch the puzzle's input.
    INSTRUCTIONS: list[tuple[str, int]] = get_data(2021, 2, func=parse, split=True)

    # Solve the puzzle.
    result = solve(INSTRUCTIONS)

    print("--- Day 2: Dive! ---")
    print(f"If I multiply the final horizontal position by the final depth I get {result}.")
    print()
