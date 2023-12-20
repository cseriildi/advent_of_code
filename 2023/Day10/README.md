# Day 10

You can find the task description and input on [the Advent of Code website](https://adventofcode.com/2023/day/10), which I cannot copy here due to copyright.

## Short summary:

### Part One

We have an <code>n x m</code> pattern which contains <code>., -, |, L, F, J, 7</code> characters and 1 <code>S</code>. The pattern represent a pipe network, and we have to find the main pipeline which is a loop. The <code>-, |, L, F, J, 7</code> characters are basicly the same as <code>═, ║, ╚, ╔, ╝, ╗</code>, the <code>.</code> characters are empty spaces and the <code>S</code> is an animal, which is in the main pipeline.

To get the desired output:
- divide the length of the pipeline by 2.

### Part Two

In Part Two we have to tell if a character is located in the area enclosed by the main pipeline.

To get the desired output:
- count the characters enclosed by the main pipeline.