import sys
from functools import cache
from pathlib import Path


class Grid:
    def __init__(self, input: str) -> None:
        self.cells = [list(line) for line in input.splitlines()]
        self.rows = len(self.cells)
        self.cols = len(self.cells[0]) if self.rows > 0 else 0
        self.start = next(
            (
                (x, y)
                for y in range(self.rows)
                for x in range(self.cols)
                if self.cells[y][x] == "S"
            ),
            None,
        )

    def is_in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.cols and 0 <= y < self.rows

    def get_cell(self, x: int, y: int) -> str:
        return self.cells[y][x] if self.is_in_bounds(x, y) else None


class Data:
    def __init__(self, filename: Path, puzzle_type: str) -> None:
        self.filename = filename
        self.part = 1
        self.result = 0
        self.expected = None
        self.type = puzzle_type
        self.parse_data()

    def parse_data(self) -> None:
        with open(self.filename) as infile:
            self.grid = Grid(infile.read())

    def set_expected(self, expected: int) -> None:
        self.expected = expected

    def unit_test(self) -> str:
        if self.expected is None:
            return ""
        if self.result == self.expected:
            return "✅"
        return f"❌ (expected {self.expected})"

    def print_solution(self) -> None:
        color = GRAY if self.part == 1 else YELLOW
        print(
            f"{color}Part {self.part} {self.type}: {self.result}{RESET}",
            self.unit_test(),
        )
        self.part += 1
        self.result = 0


#####################
## PART 1 SOLUTION ##
#####################


def part1(data: Data) -> None:
    """Counts how many times the beam will split"""

    @cache
    def dfs(x: int, y: int) -> frozenset[tuple[int, int]]:
        match data.grid.get_cell(x, y):
            case ".":
                return dfs(x, y + 1)
            case "^":
                return (
                    dfs(x - 1, y + 1) | dfs(x + 1, y + 1) | frozenset({(x, y)})
                )
            case _:
                return frozenset()

    data.result = len(dfs(data.grid.start[0], data.grid.start[1] + 1))
    data.print_solution()

    #####################
    ## PART 2 SOLUTION ##
    #####################


def part2(data: Data) -> None:
    """Counts how many different paths can a beam take"""

    @cache
    def dfs(x: int, y: int) -> int:
        match data.grid.get_cell(x, y):
            case ".":
                return dfs(x, y + 1)
            case "^":
                return dfs(x - 1, y + 1) + dfs(x + 1, y + 1)
            case _:
                return 1

    data.result = dfs(data.grid.start[0], data.grid.start[1] + 1)
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
        example.set_expected(21)
        part1(example)
    part1(puzzle)
    if example:
        example.set_expected(40)
        part2(example)
    part2(puzzle)
