import math
import sys
from itertools import combinations
from pathlib import Path


class Point:
    """3D point in space."""

    def __init__(self, x: int, y: int, z: int) -> None:
        self.x: int = x
        self.y: int = y
        self.z: int = z

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __eq__(self, other: "Point") -> bool:
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def distance(self, other: "Point") -> float:
        """Calculate Euclidean distance to another point."""
        return math.sqrt(
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
            + (self.z - other.z) ** 2
        )


class Circuit:
    """Represents a circuit made up of multiple points."""

    def __init__(self, points: set[Point]) -> None:
        self.points: set[Point] = points

    def __len__(self) -> int:
        return len(self.points)

    def __or__(self, other: "Circuit") -> "Circuit":
        return Circuit(self.points | other.points)

    def __contains__(self, point: Point) -> bool:
        return point in self.points

    def __lt__(self, other: "Circuit") -> bool:
        return len(self.points) < len(other.points)

    def __hash__(self) -> int:
        return hash(frozenset(self.points))

    def __eq__(self, other: "Circuit") -> bool:
        return self.points == other.points


class Connection:
    """Represents a connection between two points in 3D space."""

    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1: Point = p1
        self.p2: Point = p2
        self.distance: float = p1.distance(p2)

    def __lt__(self, other: "Connection") -> bool:
        return self.distance < other.distance

    def __eq__(self, other: "Connection") -> bool:
        return self.distance == other.distance

    def __hash__(self) -> int:
        return hash((self.p1, self.p2, self.distance))

    def update_circuits(self, circuits: list[Circuit]) -> None:
        """Applies this connection to the given circuits."""

        old_circuits = [c for c in circuits if self.p1 in c or self.p2 in c]

        if len(old_circuits) == 2:
            c1, c2 = old_circuits
            circuits.remove(c1)
            circuits.remove(c2)
            circuits.append(c1 | c2)


class Data:
    def __init__(self, filename: Path, puzzle_type: str) -> None:
        self.filename = filename
        self.part = 1
        self.result = 0
        self.expected = None
        self.type = puzzle_type
        self.parse_data()
        self.possible_connections = sorted(
            [Connection(p1, p2) for p1, p2 in combinations(self.points, 2)],
        )
        self.circuits = [Circuit({point}) for point in self.points]

    def parse_data(self) -> None:
        with open(self.filename) as infile:
            self.points = [
                Point(*map(int, line.split(",")))
                for line in infile.read().splitlines()
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


def part1(data: Data, num_connections: int) -> None:
    """Calculates the product of the sizes of the three largest circuits formed
    by making the specified number of connections
    between points with the shortest Euclidean distances in 3D space."""

    for _ in range(num_connections):
        data.possible_connections.pop(0).update_circuits(data.circuits)

    data.result = math.prod(
        len(c) for c in sorted(data.circuits, reverse=True)[:3]
    )
    data.print_solution()


#####################
## PART 2 SOLUTION ##
#####################


def part2(data: Data) -> None:
    """Connects points with the shortest Euclidean distances in 3D space,
    until all points are connected. Calculates the product of x-coordinates
    of the two points that were connected last."""

    for _ in range(len(data.possible_connections)):
        connection = data.possible_connections.pop(0)
        connection.update_circuits(data.circuits)
        if len(data.circuits) == 1:
            data.result = connection.p1.x * connection.p2.x
            break

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
        example.set_expected(40)
        part1(example, 10)

    part1(puzzle, 1000)
    if example:
        example.set_expected(25272)
        part2(example)
    part2(puzzle)
