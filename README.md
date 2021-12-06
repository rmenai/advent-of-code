<br />
<p align="center">
  <a href="https://github.com/rmenai/advent-of-code">
    <img src="https://user-images.githubusercontent.com/16360374/49324718-7954f100-f4e8-11e8-8ef6-1b701afc504f.png" alt="Logo" width="80">
  </a>

<h3 align="center">Advent of Code Solutions</h3>

  <p align="center">
    An annual programming puzzles event in December
    <br />
    <a href="https://github.com/rmenai/advent-of-code"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/rmenai/advent-of-code">View Demo</a>
    ·
    <a href="https://github.com/rmenai/advent-of-code/issues/new?assignees=&labels=&template=bug_report.md&title=">Report Bug</a>
    ·
    <a href="https://github.com/rmenai/advent-of-code/issues/new?assignees=&labels=&template=feature_request.md&title=">Request Feature</a>
  </p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
   <li>
      <a href="#cheating">Cheating</a>
    </li>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li>
      <a href="#environment-variables">Environment Variables</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

This repository contains my completed and functional python solutions to each
year's [Advent of Code](https://adventofcode.com/) challenges starting from 2021.

<!-- CHEATING -->

## Cheating

This repository is not intended to promote or otherwise encourage cheating on any of these sites. You should always try
to complete a challenge on your own before viewing the solutions in this repository.

<!-- INSTALLATION -->

## Installation

The first step will be to clone the repo

```shell
git clone https://github.com/rmenai/advent-of-code.git
```

The requirements are:

* [Python](https://www.python.org/downloads/) and [Poetry](https://python-poetry.org/docs/)

1. Install the dependencies
   ```shell
   poetry install
   ```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file.

| Variable    | Description                                                                        | Default    |
|-------------|------------------------------------------------------------------------------------|------------|
| AOC_SESSION | Your aoc [cookie session](https://github.com/wimglenn/advent-of-code-wim/issues/1) | * Required |
| DEBUG       | Toggles debug mode                                                                 | False      |

<!-- USAGE EXAMPLES -->

## Usage

Now you are done! You can run the project using

```shell
poetry run task start [-h] [-p {1,2}] puzzle

positional arguments:
  puzzle                  choose a specific challenge [year].[day]

optional arguments:
  -h, --help              show this help message and exit
  -p {1,2}, --part {1,2}  run a specific part of the puzzle

ex. python -m aoc 2021.01 -p 2 (Part 2 of the first day of aoc 2021)

```

<!-- LICENSE -->

## License

Distributed under the MIT License. See [LICENSE](https://github.com/rmenai/advent-of-code/blob/main/LICENSE) for more
information.

<!-- ACKNOWLEDGMENTS -->

## Acknowledgements

- [bsoyka/advent-of-code](https://github.com/bsoyka/advent-of-code)
