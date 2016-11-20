---
layout: "post"
category: "Unit 1: SNAP"
title: "🍂 Lab 2⃣.3⃣ Defining Gravity"
date: "2016-09-29 07:20"
---

**In this lab, you will use everything you've learned about loops and conditionals to construct a simplified model for gravity.**

## What goes up...🐶
1. Create a SNAP program with a background that looks like an outside scene. Add a single sprite that looks like an object of your choice (a brick or a ball would work well) and place it so it is touching the "ground."
2. Write code for your sprite so that, when the green flag is clicked, the object moves to the top of the stage and "falls" towards the bottom at a constant speed.
3. What happens in your program when the object hits the "ground"? Is that an accurate model of how gravity works on Earth?
4. Modify your program so that the problem you identified in part 3 is fixed. Make your object do something appropriate when it hits the "ground." (Making sure the ground is a unique color and making use of that color will be helpful.

✅ **Check: Press Green Flag, object falls from top of the screen, hits the ground, and looks like it’s hitting the ground.**

## ...Must Come Down
1. Add a second sprite that looks like something that might already be on the ground when your first object is falling (like a house, a picnic table, a person, etc.). Put this new object directly below where the first object falls so that the falling object will hit it.
2. What should happen when the following object hits the object on the ground? Will that happen with the model we currently have? Why or why not?
3. Modify your code so that you fix the problem you identified in part 2.2. Make your falling object do something appropriate if it hits the object on the ground. Once you've made that work, move the falling object and make sure you didn't break the situation when the falling object doesn't hit something on the way down.

✅ **Check: Code for a collision between two objects, and a miss.**

4. Add code so that both objects move to a random x coordinate every time the green flag is clicked. The falling object should be at the top of the stage, and the other object at the bottom. Verify that the falling object does the right thing no matter where the two objects end up relative to each other.

5. Add a hill to your outdoor scene and make sure that your falling object does something appropriate when it hits the hill.

✅ **Check: Green Flag sets random position. Object falls, collides or “rolls.”**
