---
layout: "post"
title: "🎉 Functions"
date: "2016-12-09 11:55"
category: "Python"
---


## Do Now (in repl)

```python
import random
random.randint(0, 3)
random.randint(0, 3)
print (random.randint(0, 3))
print (random.randint(0, 3))
print (random.randint(0, 3))
# In comments:
# What does randint do?
# What do the values 0 and 3 do?
# Try changing those numbers, rerun the program, and write down what changed.
# What is the difference between random.randint(0,3) and print(random.randint(0,3))?
```

`print` is a built-in function– it takes an input and produces some output when you use it.

## Functions
Why use functions?    
**→ Reusable Code**    
If you find yourself doing something more than once, make it a function.

_In other words..._

- **Be lazy. **
- **Don’t repeat yourself. **
- **Make the computer do the work.**

### Functions have to be defined and then called:
```python
def name_of_function(this):
  """What it do???"""
  print "It prints " + this + "!"
```

Take a look at this one...

```python
def power(base, exponent):  
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)  
```



Write a for loop to print only the odd numbers from this list

`list = [3,4,7,13,54,32,653,256,1,41,65,83,92,31]``

Now, iterate and turn your loop into a function called `find_odds` that takes an input and prints the odd numbers in ANY list.

`def find_odds(input):``

To exceed standards, create functions to ADD all of the odd numbers in a list. Then create a function to add all of the even numbers in a list. Test your functions using a randomly generated list of numbers.

`def odd_sum(input):`   
`def even_sum(input):`

## Make a random list
```python
import random
my_randoms = random.sample(range(100), 15)
```

### Checklist
**Meeting Standards (3)**
- for loop prints odd numbers from list
- function `find_odds` takes a list, prints odds.
```python
def find_odds(input):
```

**Exceeding Standards (4)**
- Redo [Lab 1⃣.1⃣](http://bsk.education/CS9/python/2016/12/08/lab-1-1-with-python/) with functions for each shape.
