# Day 15

You can find the task description and input on [the Advent of Code website](https://adventofcode.com/2023/day/15), which I cannot copy here due to copyright.

## Short summary:

### Part One

We have a comma separated list of strings, which are starting with a couple of letters followed by a <code>-</code> or an <code>=</code>, then endig in a number between 0 and 9.

We have been given a method called HASHMAP:

0. start from 0
1. add the character's ASCII value
2. multiply it by 17
3. get the remainder of dividing by 256
4. repeat 1-3. steps for the rest of the string

To get the desired output sum:
- the result of the HASHMAP method for every string in the input.

### Part Two

In Part Two we have 265 boxes and we have to go through the strings in the input. 

- Using the HASHMAP method on the letters in the beginning of each string we can determine the relevant box.
- If the special character is <code>=</code> then we have to put it in the relevant box with the number assignt after the <code>=</code>.
- If those letters can already be found in the relevant box then assign the new number to it.
- If the special character is <code>-</code> then we have remove from the relevant box the same letters if it's in it.

To get the desired output sum:
- the box index of an element + 1 multiplied by the element's index in the box + 1 and multiplied by its assigned number for all element in the boxes.
