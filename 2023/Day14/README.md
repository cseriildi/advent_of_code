# Day 14

You can find the task description and input on [the Advent of Code website](https://adventofcode.com/2023/day/14), which I cannot copy here due to copyright.

## Short summary:

### Part One

We have an <code>n x m</code> pattern which contains <code>O, .</code> and <code>#</code> characters.
The pattern lies horizontally and we have to tilt it to its north side vertically and let the "gravity" move the <code>O</code> characters till it hits the bottom of the pattern or a <code>#</code>.

Basically we have to change the order of the <code>., O</code> characters to <code>O, .</code> until there is no more <code>.</code> berfore an <code>O</code>.

The value of a <code>O</code> in the last row is 1, in the second to last 2 etc...

To get the desired output sum:
- the value of the <code>O</code> characters.

### Part Two

In Part Two we have to tilt it to all sides in north, west, south, east order 1000000000 times.

However that would take to much time, but after a while there will be a sequence as the pattern changes after a full cycle.
So we have to find the sequence and with its length we can figure out which element of the sequence will be the pattern after 1000000000 cycle.

The output can be calculated the same way as before.