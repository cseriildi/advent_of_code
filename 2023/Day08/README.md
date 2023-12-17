# Day 8

You can find the task description and input on [the Advent of Code website](https://adventofcode.com/2023/day/8), which I cannot copy here due to copyright.

## Short summary:

### Part One

We have a list of  <code>left/right</code> directions and a list of nodes like <code>AAA = (BBB, CCC)</code>.
Following the <code>left/right</code> directions we have to go through the map, for example if it's left then go to the <code>BBB</code> node if it's right to the <code>CCC</code>, until we arrive at <code>ZZZ</code>.

We have to count the steps it takes to get from <code>AAA</code> to <code>ZZZ</code>.

To get the desired output sum:
- the number of steps.

### Part Two

In Part Two we have to go through the map with every node that ends with an <code>A</code> till we arrive a node that ends with a <code>Z</code>.

We have to count the steps it takes to get to a point where all nodes end with a <code>Z</code> at the same time.

The output can be calculated the same way as before.