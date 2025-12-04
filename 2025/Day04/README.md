# Day 4

You can find the full task description and your input on [the Advent of Code website](https://adventofcode.com/2025/day/4).

## Short summary

We have a storage unit with papers. A roll of paper is represented by `@`, an empty space by `.` on a grid.

### Example
```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```


### Part 1

A roll is accessible by the forklifts if there are less than 4 rolls on the 8 adjacent positions (including diagonals).
Count how many rolls are accessible by the forklifts.

### Part 2

Once a roll is accessible it can be removed; removing rolls may make other rolls accessible.
Count how many rolls can be removed.
