---
layout: "post"
title: "🔀 Conditionals"
date: "2016-11-27 19:49"
category: "Python"
---

## Learning Targets
- I can write conditionals in Python using `if` and `else`.
- I can predict the output of conditionals in Python.

## Conditionals
```python
if #something true
    # run this indented code
else:
    #run this indented code
```

**Quick check**

```python
# What's the difference between
school = "F&T"
#and
223 == 223
# what about...
223 = "F&T"
```

## Python Comparison Operators

| Operator | Description              | Example  |
|:--------:|:-------------------------|:---------|
|    ==    | equal to                 | `x == 2` |
|    !     | not equal to             | `y != 3` |
|    >     | greater than             | `4 > 3`  |
|    <     | less than                | `1 < 1`  |
|    >=    | greater than or equal to | `x >= 2` |
|    <=    | less than or equal to    | `y <= 3` |

```python
"""
What will print after each conditional is run?
"""
# Number 1:
if 5<2:
    print "I am right"
else:
    print "I am wrong"

    # Number 2:
if 5>2:
    print "I am right"
else:
    print "I am wrong"
```

## `if` even...
How can we tell if a number is even or odd?

# `%`
This is **not** the percentage sign. I mean, it is, but in Python, it means **modulo** or **mod**. What?

It divides one number by another and returns the remainder. Like this:

```python
print(4 % 3)
print(1040934 % 2)
print(1040934 % 2)
```

Before you start calculating, what are the **only** possibilities of each **modulo** operation?
