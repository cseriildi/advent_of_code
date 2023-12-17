# Day 13

You can find the task description and input on [the Advent of Code website](https://adventofcode.com/2023/day/13), which I cannot copy here due to copyright.

## Short summary:

### Part One

We have a list of <code>n x m</code> patterns which contains <code>#</code> and <code>.</code> characters.
We have to find a vertical or horizontal symmetry line in every pattern.
The line isn't necessarily in the middle, hence some parts of the pattern may have to be ignored.

To get the desired output sum:
- the number of columns to the left from the symmetry line for the vertical type
- 100 multiplied by the number of rows above the symmetry line for the horizontal type.

### Part Two

In Part Two we have to find the symmetry line with exactly 1 difference ("smudge on the mirror") which is a <code>#</code> instead of a <code>.</code> or vice versa.

The output can be calculated the same way as before.