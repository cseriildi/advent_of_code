# Day 8

You can find the full task description and your input on [the Advent of Code website](https://adventofcode.com/2025/day/8).

## Short summary

We are given a list of 3D coordinates. We can connect 2 points with a straight line. These connections form circuits.

#### [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance)

```math
 d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}
```

### Example

```
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
```

### Part 1

Calculate the product of the size of the 3 largest circuits formed by making 1000 connections _(10 for the example)_ between the closest points.

### Part 2

Calculate the product of the x coordinates of the last point we need to connect in order to have only 1 big circuit.
