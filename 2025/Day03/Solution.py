import sys
from pathlib import Path


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
            self.banks = infile.read().splitlines()

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


def find_biggest_jolt(bank: str, num: int = 2) -> int:
    """Find the biggest possible jolt.
    A jolt is formed by concatenating 'num' batteries from the bank.
    The order of batteries can't be changed, but does have to be contiguous."""

    jolt = ""
    start = 0
    end = len(bank) - num

    for _ in range(num):
        end += 1
        max_battery = max(bank[start:end])
        jolt += max_battery
        start = bank.index(max_battery, start) + 1

    return int(jolt)


def part1(data: Data) -> None:
    """Sums the biggest jolts from each bank using 2 batteries."""

    data.result = sum(find_biggest_jolt(bank) for bank in data.banks)
    data.print_solution()


#####################
## PART 2 SOLUTION ##
#####################


def part2(data: Data) -> None:
    """Sums the biggest jolts from each bank using 12 batteries."""

    data.result = sum(find_biggest_jolt(bank, 12) for bank in data.banks)
    data.print_solution()


##########
## MAIN ##
##########

GRAY = "\033[90m"
YELLOW = "\033[33m"
RED = "\033[1;91m"
RESET = "\033[0m"


def load_data(puzzle_type: str):
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
        example.set_expected(357)
        part1(example)
    part1(puzzle)
    if example:
        example.set_expected(3121910778619)
        part2(example)
    part2(puzzle)
