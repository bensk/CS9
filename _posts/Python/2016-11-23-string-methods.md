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
<!--hiiiiii  -->
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
👉 Go to [repl](http://repl.it/)!

### Organization

Separate each exercise with a line space and add a comment above each to tell me what you are doing.

### Grading Policy

- 2 ⭐, 1 ⭐⭐ = 80
- 2 ⭐, 2 ⭐⭐ = 85
- 2 ⭐, 2 ⭐⭐, 1 ⭐⭐⭐ = 90
- 2 ⭐, 2 ⭐⭐, 2 ⭐⭐ = 100

#### ⭐
 **Option 1:** Store a person's name in a variable. Print the name in uppercase, lowercase and title case.    

**Option 2:** Find a quote from a famous person that you admire. Print the quote and the name of it's author.

#### ⭐⭐
**Option 1:** Find a quote from a famous person that you admire and store it in a variable called message. Store the name of the author in a variable called famous_person. Print the quote and the name of it's author using concatenation. It should look like:

`Steve Jobs: "_____________quote_here_____________". `

**Option 2:** In order to use a tab in your display you need to add \t in front of what you want printed.

For example:
This code -->   

```python
print("\tThis creates a tab.")       
```
will end up looking like -->

`    This creates a tab.`

Find another quote and print the quote and the author but tab the author's name on a new line after the quote.

#### ⭐⭐⭐
This line of code:

```python
print("Languages:\n\Python\nC\nJavaScript")
```

Creates this -->

```
Languages:
Python
C
JavaScript
```

**Option 1:** Utilize `\n` and `\t`  to create a shopping list with just one print statement.

**Option 2:** Utilize `\n` and `\t`  to recreate the statement in the picture below using just one print statement. Each word must be printed on the same line and in approximately the same position as it appears in the picture.
