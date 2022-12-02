import logging

from aoc.utils.parsers import get_data

log = logging.getLogger(__name__)


def solve(games: list[tuple[str, str]]) -> int:
    """Determine how many points in total after all the games."""
    scores = {"AY": 4, "AZ": 8, "AX": 3, "BX": 1, "BY": 5, "BZ": 9, "CZ": 7, "CX": 2, "CY": 6}
    return sum(scores[game] for game in games)


if __name__ == "__main__":
    # Fetch the puzzle's input.

    GAMES: list[tuple[str, str]] = get_data(
        2022, 2,
        func=lambda raw: ["".join(game.split()) for game in raw.split("\n")],
    )

    # Solve the puzzle.
    result = solve(GAMES)

    print("--- Part Two ---")
    print(f"If everything goes exactly according to the strategy guide, the total score will be {result} points.")
    print()
