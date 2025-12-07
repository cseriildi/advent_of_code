import sys
from pathlib import Path
from math import prod


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
            self.input = [line.rstrip("\n") for line in infile]

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


def do_operation(op: str, nums: list[int]) -> int:
    if op == "+":
        return sum(nums)
    elif op == "*":
        return prod(nums)


def part1(data: Data) -> None:
    """Applies the operation in last row to each number above and sums them."""

    numbers = [line.split() for line in data.input[:-1]]
    operations = data.input[-1].split()
    rows = len(numbers)
    cols = len(numbers[0])

    for x in range(cols):
        nums = [int(numbers[y][x]) for y in range(rows)]
        data.result += do_operation(operations[x], nums)

    data.print_solution()


#####################
## PART 2 SOLUTION ##
#####################


def part2(data: Data) -> None:
    cols = max(len(line) for line in data.input)
    numbers = [(line.ljust(cols)) for line in data.input[:-1]]
    operations = data.input[-1]
    rows = len(numbers)

    nums = []
    for x in range(cols - 1, -1, -1):
        num = "".join(
            numbers[y][x] for y in range(rows) if numbers[y][x] != " "
        )
        if num:
            nums.append(int(num))
        if operations[x] in "+*":
            data.result += do_operation(operations[x], nums)
            nums.clear()

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
        example.set_expected(4277556)
        part1(example)
    part1(puzzle)
    if example:
        example.set_expected(3263827)
        part2(example)
    part2(puzzle)
