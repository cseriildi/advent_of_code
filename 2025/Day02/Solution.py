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
            self.ranges = [
                range(int(start), int(end) + 1)
                for pair in infile.read().split(",")
                for start, end in [pair.split("-")]
            ]

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


def is_repeated_twice(id: int) -> bool:
    """Check if number's first half equals second half."""

    id_str = str(id)
    mid = len(id_str) // 2
    return id_str[:mid] == id_str[mid:]


def part1(data: Data) -> None:
    """Sums IDs that are formed by repeating a pattern 2 times."""

    data.result = sum(
        id
        for id_range in data.ranges
        for id in id_range
        if is_repeated_twice(id)
    )
    data.print_solution()


#####################
## PART 2 SOLUTION ##
#####################


def is_repeated_multiple(id: int) -> bool:
    """
    My original solution:
    Check if number can be formed by repeating a pattern.
    """

    id_str = str(id)
    length = len(id_str)
    return any(
        id_str == id_str[:i] * (length // i)
        for i in range(length // 2 + 1, 1, -1)
    )


def has_pattern(id: int) -> bool:
    """s in (s+s)[1:-1] idiom to check for repeated patterns."""

    id_str = str(id)
    return id_str in (id_str * 2)[1:-1]


def part2(data: Data) -> None:
    """Sums IDs that are formed by repeating pattern any number of times."""

    data.result = sum(
        id for id_range in data.ranges for id in id_range if has_pattern(id)
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
        example.set_expected(1227775554)
        part1(example)
    part1(puzzle)
    if example:
        example.set_expected(4174379265)
        part2(example)
    part2(puzzle)
