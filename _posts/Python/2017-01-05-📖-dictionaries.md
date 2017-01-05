---
layout: "post"
title: "📖 Dictionaries"
date: "2017-01-05 23:08"
category: "Python"
---

## Learning Targets
- I can create and modify dictionaries in Python.
- I can add, remove, and search through lists and dictionaries.
- `AP` I can explain how lists and other collections can be treated as abstract data types (ADTs) in developing programs.

## Do Now

In repl:

Run the following code:

```python
my_dictionary = {
'cat': 'a domestic feline',
'dog': 'a domestic canine',
'chair': 'furniture piece for sitting',
'car': 'automobile'
}
print(my_dictionary)
print(my_dictionary['dog'])
print(my_dictionary.get('dog'))
print('cat' in my_dictionary)
print('monkey' in my_dictionary)
```

In comments:
1. What prints?    
2. What type[^1] is my_dictionary?
3. Add a line of code that will print the definition of `chair`, then run the code again.
4. What happens if you use my_dictionary['kittens']? What do you think that error means?

[^1]: Hint: try `print(type(my_dictionary))`

---

## ✍ `Dictionary = { }` ← note curly brackets

Like a list, but has a key instead of an index.
Dictionaries pair the key with a value.

```python
password = {'SK':12345}
```

The key & value can be any string or number.

Dictionaries look like:

```python
passwords = {'SK': 12345, 'Lentino': 67890, 'Perez': 54321}
print(passwords['SK'])
```

Dictionaries are great for things like **address books** (pairing a name with a phone number), **login pages** (pairing an e-mail address with a username), etc.

## Dictionary Lab
In repl: `Dictionary_Lab`

1⃣ Create a social network profile for yourself using a dictionary. I've suggested some keys, but you should feel free to add your own.

```python
user_profile = {
	# name
	# school
	# birthday
	# email
	# username(s)
	# where are you from?
	# number of siblings
	# skills
	# about you
	# favorite quote
	# favorite movie
	# favorite musician
	# favorite TV show
	# favorite book
}
```

2⃣ Test your profile by `print`ing the value for each key.

3⃣ Create a function that lets someone look through your profile. When called, it should ask something like "what would you like to know about me?" and they can respond with an aspect like `email` and get back your email. If the key is not in your profile, let them know that they can't have that information.

4⃣ Add a `while` loop
