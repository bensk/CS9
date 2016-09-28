---
layout: "post"
title: "➿ Nested Loops"
date: "2016-09-27 21:32"
---

## 🎯 Learning Target
I can use nested loops to solve programming problems.

## Do Now (in Google Classroom)
Why are loops useful?

Let's look an example. Write code to draw two squares, next to each other.

[⬛⬛](http://snap.berkeley.edu/snapsource/snap.html#present:Username=223bsk&ProjectName=nestedLoops)

## Nested Loops
> A loop in a loop.

_In other words..._

![]({{ site.url }}/images/NestedLoops.jpg)

How many times will the sprite take 20 steps?

![]({{ site.url }}/images/NestedLoopsRepeat.png)


---

## Lab 2.2 - It's Brick

In this lab, you will use nested loops to draw a large brick wall using as little code as possible.

## Part 1 - Build a Brick
1. Write a SNAP script to draw a single 20x10 "brick" in the lower left corner of the stage when the green flag is clicked.
2. Modify your code to draw two bricks side by side. The bricks should share a short edge.
3. Now modify your code again to build a full row of bricks across the entire length of the stage. Use loop to keep your code as concise as possible. Remember that the stage is 480 pixels wide and 360 pixels tall (by default- you can change that).

## Part 2 - Build a Wall
1. Now that you can build a row of bricks, add code to build a second row above the first row. The bricks in the second row should share a long edge with those in the first row, but should be "offset" so that the ends of the second row bricks are at the middle of the first row bricks.
2. Modify your code to build more rows, alternating back and forth between the "regular" and "offset" rows. Use nested loops to keep your code concise.
3. Finish off the wall the by building alternating rows all the way to the top of the stage. Remember that the stage is 360 pixels tall. Your final wall should look like this:

![]({{ site.url }}/images/Bricks.gif)


















Can you build the whole wall with one nested loop?
