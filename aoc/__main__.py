import argparse
import logging

from aoc.core import constants
from aoc.utils.runners import run_puzzle

log = logging.getLogger(__name__)

# Set up the arguments' parser.
parser = argparse.ArgumentParser(epilog="ex. python -m aoc 2021.01 -p 2"
                                        " (Part 2 of the first day of aoc 2021)")

parser.add_argument("puzzle", type=str,
                    help="choose a specific challenge [year].[day]")

parser.add_argument("-p", "--part", type=int, choices=[1, 2],
                    help="run a specific part of the puzzle")

args = parser.parse_args()

# Parse the year and day of the puzzle.
year, day = map(int, args.puzzle.split("."))

# Format the log message.
puzzle_url = constants.aoc_url.format(year=year, day=day)
log.info(f"Running Advent of Code {year} day {day} {puzzle_url}")

# Run the puzzle.
run_puzzle(year, day, args.part)
