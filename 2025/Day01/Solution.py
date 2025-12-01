import sys
from pathlib import Path

DIALSTART = 50
DIRECTIONS = {"R": 1, "L": -1}


class Data:
    def __init__(self, filename: Path, puzzle_type: str) -> None:
        self.filename = filename
        self.part = 1
        self.result = 0
        self.type = puzzle_type
        self.parse_data()

    def parse_data(self) -> None:
        with open(self.filename) as infile:
            lines = infile.read().splitlines()
            self.moves = [
                (DIRECTIONS[line[0]], int(line[1:])) for line in lines
            ]

    def print_solution(self) -> None:
        color = GRAY if self.part == 1 else YELLOW
        print(f"{color}Part {self.part} {self.type}: {self.result}{RESET}")
        self.part += 1
        self.result = 0


#####################
## PART 1 SOLUTION ##
#####################


def part1(data: Data) -> None:
    dial = DIALSTART
    data.result = sum(
        1 for d, move in data.moves if (dial := (dial + d * move) % 100) == 0
    )
    data.print_solution()


#####################
## PART 2 SOLUTION ##
#####################


def part2(data: Data) -> None:
    dial = DIALSTART
    for d, move in data.moves:
        data.result += sum(
            1 for _ in range(move) if (dial := (dial + d) % 100) == 0
        )
    data.print_solution()


##########
## MAIN ##
##########

GRAY = "\033[90m"
YELLOW = "\033[33m"
RED = "\033[1;91m"
RESET = "\033[0m"


def load_data(puzzle_type: str) -> Data | None:
    filename = Path(__file__).parent / f"{puzzle_type}.txt"
    try:
        return Data(filename, puzzle_type)
    except FileNotFoundError:
        print(
            f"{RED}Save {puzzle_type} input to {filename}{RESET}",
            file=sys.stderr,
        )
        return None


if __name__ == "__main__":
    puzzle = load_data("puzzle")
    if puzzle is None:
        sys.exit(1)
    example = load_data("example")

    if example:
        part1(example)
    part1(puzzle)
    if example:
        part2(example)
    part2(puzzle)
