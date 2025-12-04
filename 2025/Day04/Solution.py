import sys
from pathlib import Path


class Grid:
    def __init__(self, input: str) -> None:
        self.cells = [list(line) for line in input.splitlines()]
        self.rows = len(self.cells)
        self.cols = len(self.cells[0]) if self.rows > 0 else 0

    NEIGHBOURS = [
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0),
        (1, -1),
        (1, 1),
        (-1, -1),
        (-1, 1),
    ]

    def is_in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.cols and 0 <= y < self.rows

    def is_paper(self, x: int, y: int) -> bool:
        return self.is_in_bounds(x, y) and self.cells[y][x] == "@"

    def count_neighbors(self, x: int, y: int) -> int:
        return sum(self.is_paper(x + dx, y + dy) for dx, dy in self.NEIGHBOURS)

    def is_accessible_paper(self, x: int, y: int) -> bool:
        return self.is_paper(x, y) and self.count_neighbors(x, y) < 4

    def remove_paper(self, x: int, y: int) -> None:
        self.cells[y][x] = "."

    def remove_if_accessible(self, x: int, y: int) -> bool:
        if self.is_accessible_paper(x, y):
            self.remove_paper(x, y)
            return True
        return False

    def apply(self, fn):
        """Apply fn(x,y) for each coordinate."""
        for y in range(self.rows):
            for x in range(self.cols):
                yield fn(x, y)


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
    """Counts papers ('@') in the grid with less than 4 neighboring paper."""

    data.result = sum(data.grid.apply(data.grid.is_accessible_paper))

    data.print_solution()


#####################
## PART 2 SOLUTION ##
#####################


def part2(data: Data) -> None:
    """Counts papers ('@') that can be removed iteratively.
    A paper can be removed if it has less than 4 neighboring paper."""

    while removed := sum(data.grid.apply(data.grid.remove_if_accessible)):
        data.result += removed

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
        example.set_expected(13)
        part1(example)
    part1(puzzle)
    if example:
        example.set_expected(43)
        part2(example)
    part2(puzzle)
