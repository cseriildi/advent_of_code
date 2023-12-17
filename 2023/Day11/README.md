# Day 11

You can find the task description and input on [the Advent of Code website](https://adventofcode.com/2023/day/11), which I cannot copy here due to copyright.

## Short summary:

### Part One

We have a list of <code>n x m</code> patterns which contains <code>#</code> and <code>.</code> characters.
All empty columns and rows (which only contain <code>.</code> characters) have to be doubled. 

To get the desired output sum:
- the shortest path between every <code>#</code> character pair, which is the distance of their coordinates.

### Part Two

In Part Two we have to multiply the empty columns and rows by 1 000 000 instead of 2.

The output can be calculated the same way as before.