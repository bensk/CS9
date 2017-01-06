---
layout: "post"
title: "🔍 Word Counter"
date: "2017-01-05 23:23"
category: "Python"
---


Last time, we saw that dictionaries can pair keys of any data type with values of any data type. We paired strings with strings last time, but now we're going to pair strings with lists.

Let's review how we **add** values to a dictionary.

```python
list_dictionaries = {
 'i': [1, 3, 4],
 'am': [1, 2, 3, 4]
}

list_dictionaries['groot'] = [1,2,3,4,5]
# update the key 'groot' with a list value
```

What if I know what to add the string `"6"` to the key `"groot"`? How do we add things to a list? `.append()`!

```python
list_dictionaries['groot'].append("six")
```

Dictionaries are good for storing values of all different, types, but they're also helpful for *finding* and *counting* values.

Consider a dictionary from yesterday:

```python
my_dictionary = {
'cat': 'a domestic feline',
'dog': 'a domestic canine',
'chair': 'furniture piece for sitting',
'car': 'automobile'
}
```

How many times does the letter `'a'` appear in the entry for `'dog'`?

`print(my_dictionary['car'].count("a"))`

Ok, that's not so impressive. But something people often want coders to do is **analyze** a bunch of data, and a useful statistic to find is **frequency**.

> Frequency: the (relative) number of times something occurs in a given sample.

We can use dictionaries and loops to analyze frequency.

```python
sentence = input("Give me a sentence")
report = {}

for i in sentence:
	report[i] = sentence.count(i)
#          ^key         ^ value (counting each i in the sentence)
print(report)
```

---

In this lab we will implement a word frequency algorithm. It will tell you how many of each word you had in an essay.

Make a variable for user input, something like

```python
text_input = input("Paste your text here")
```

In order to turn this text into a list of lower case words we will use the `split("")`, ``replace()``, and `lower()` functions.


For each word in the document, count the number of times it occurs.

Consider the following phrase: 'Cats are cool. Baby cats are called kittens. Cats make great pets.'

The word 'cats' appears 3 times. The word 'are' appears 2 times.
The program will first create a dictionary with the words as keys and the number of times they occur as values.

Then it will prompt the user which word they are curious about. If the word was in the paragraph it will print the number of times it occurred.
