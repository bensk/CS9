---
layout: "post"
title: "❝String Methods❞"
date: "2016-11-23 21:10"
category: "Python"
---

## 🎯 Learning Target
I can write strings and utilize string methods in Python

## Do Now (in Google Classroom)
```python
# What prints if you run this code?
print("2+1")
print("2+1") + 2
print("2+1") * 2
```

## Strings & Things
Strings are any characters inside quotes.

```python
print("This is a string with double quotes")
print('This is a string with single quotes')
# doesn't matter which quotes you use as long as you are consistent.
```
Python can't **evaluate** anything inside of a string, so `print('1+2')` becomes: `'1+2'`.

What is the proper way to print the statement below:

`It’s a Wonderful Life!`

```python
print(  “It’s a Wonderful Life!’ )
print ( ‘It’s a Wonderful Life!’ )
print ( It’s a Wonderful Life! )
print ( “It’s a Wonderful Life!” )
```

## String Methods
Built-in actions you can use on string data.

For example:

```python
name = "sk"
print(name.upper())
message = "WHY ARE YOU YELLING!"
print(message.lower())
book = "to kill a mockingbird"
print(book.title())
```

`.upper()`
`.title()`
`.lower()`

We can also add strings together. In Python, this is called **concatenation**:

```python
first_name = 'grace'
last_name = 'hopper'
name = first_name.title() + last_name.title()
print(name)
# What's the mistake?
```

## Practice!
👉 Go to [repl](https://repl.it/data/lti/assignments/15094)!
