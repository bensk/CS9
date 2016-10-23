---
layout: "post"
title: "👌 SNAP Final Project"
date: "2016-10-24 09:12"
---

## Overview
Platform games are among the most widely recognized types of video games. Composing about one third of all console games at the peak of their popularity, platform games are characterized by their relative simplicity and by the common gameplay element of jumping across suspended platforms (hence the name) to avoid falling into a hazard. Platform games also typically include enemy characters, items that grant the hero special abilities ("power-ups"), and a "checkpoint" system that allows the player to restart from partway through a game or level when he or she dies.

## Details
1⃣ **Hero** Your program should have a "Hero" sprite. You will be designing this character (a simple stick figure will suffice, if your art skills are like mine). "Hero" should respond to user input. Specifically:

- "Hero" should clearly “face” the right when you push the right arrow key
- "Hero" should clearly “face” the left when you push the left arrow key
- "Hero" should jump when you push space bar
- "Hero" should perform an animated walk when you hold left or right arrow key

2⃣ **Scenery** You should have scenery sprites that move based upon "Hero" traveling on the level. It is up to you to decide the level scenery, but you should meet the following requirements:

- There should be at least two scenery sprites (Example: A mountain and a tree)
You should layer these sprites relative to "Hero" and each other. For example, "Hero" should always be “in front” of any background scenery sprites
- Scenery sprites move relative to "Hero" as she moves. For example, when you hold down the right arrow key, the background sprites should move from right to left in the stage.
- Following with the layers, scenery sprites should move at different speeds so that one seems farther away. For example, a faraway mountain should move more slowly than a nearby tree.
- Scenery sprites should roll over/reappear when they hit the edge of the stage. For example, when "Hero" is walking to the right, the scenery Sprites should re-appear on the right side of the stage when they roll off the left.

3⃣ **Enemy** There should be an on-ground enemy for "Hero" to contend with. Specific criteria here include:

- There is at least one on-ground enemy
- The enemy sprite moves towards "Hero", independent of whether "Hero" is moving (e.g. regardless of whether the user is pressing an arrow key).
- The enemy sprite reappears/rolls-over when it hits the edge of the stage
- The enemy sprite is animated when it is moving towards "Hero"
- If "Hero" does not jump, she runs into the enemy and the game ends with an appropriate message (HINT: you can use the “STOP ALL” block to end all scripts)
- It should be possible for "Hero" to jump over the enemy.

## Programming
I am looking for you to incorporate good programming habits in your code:

- Using Start and Stop blocks.
- Making sure you initialize appropriately so that your program is repeatable.
- Use conditionals and variables, not precisely timed waits.
- Add comments to your code so it is easy to understand.

## Extensions (for the 4⃣!)
Once you complete the above, you can extend your program. Some suggestions:

- Include flying enemies for "Hero" to dodge or duck
- Keep score based on how many objects "Hero" gets by [Hint: Use a variable and show it on the screen]
- Have "Hero" jump to ‘grab’ an object that offers "Hero" extra points or more powerful abilities (such as jumping higher or not being killed when she runs into an enemy). The objects must appear at random times and move smoothly as "Hero" runs

## Rubric
The detailed list for what I will use to grade your projects is below. Please review your projects before submitting to be sure you meet all of them.

| Requirement	|  Value  |
|:--|:--:|
| "Hero" turns to the right on right arrow key	|  5  |
| "Hero" turns to the left on left arrow key	|  5  |
| "Hero" performs an in-place animated walk if you hold down either arrow key	|  5  |
| "Hero" jumps based on some input	|  5  |
| There are least two scenery sprites	|  5  |
| Scenery sprites are layered with "Hero" (e.g. appropriate layering blocks are in your program)	|  5  |
| Scenery sprites move based on "Hero" movement	|  5  |
| Scenery sprites move at different speeds (e.g. far away versus near)	|  5  |
| Scenery sprites roll over when the fall of the stage	|  5  |
| There is at least one on-ground enemy	|  5  |
| Enemy sprite always moves towards "Hero"	|  5  |
| Enemy sprite re-appears/rolls over correctly	|  5  |
| Enemy sprite is animated when it moves	|  5  |
| If "Hero" does not jump, she runs into the enemy and the game ends nicely and properly	|  10  |
| "Hero" can jump over the enemy	|  5  |
| Good programming #1: Program has clear start and stop	|  5  |
| Good programming #2: Program is repeatable and initializes state correctly	|  5  |
| Good programming #3: Use of comments in your code	|  5  |
| Good programming #4: Use conditionals and variables, not precisely timed waits.	|  5  |
| Extra Credit: Include flying enemies for "Hero" to dodge or duck	|  5  |
| Extra Credit: Keep score based on how many objects "Hero" gets by	|  5  |
| Extra Credit: Have "Hero" jump to ‘grab’ an object that offers "Hero" extra points or more powerful abilities. The objects must appear at random  times and move smoothly as "Hero" runs	|  10  |
| Extra Credit: Create Your Own Extension	| 0-10  |
| **TOTAL POINTS**	| **100**   |
