---
layout: "post"
title: "⚔ Choose your own adventure"
date: "2016-12-1 19:11"
category: "Python"
---


## Take a look at this:

```python
print ("You've enter the cave")
print ("Do you take the passage on the left, in the middle, or the right?")
answer = input("Type left, right, or middle and hit 'Enter'. \n")
answer = answer.lower()
if answer == "left" or answer == "l":
    print ("Poor choice. This path is dark and hopeless.")
elif answer == "right" or answer == "r":
    print ("This path is less dark, but it smells worse...")
else:
    print ("Things are looking up. Keep walking.")
```

What does it do? How does it work? Can you make your own adventure?

To repl!
