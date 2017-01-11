---
layout: "post"
title: "✅ To-do List App"
date: "2017-01-08 21:22"
category: "Python"
---

## Do Now (Google Classroom)
WITHOUT running the code, predict what is printed by the code below:

```python
this_is_a_dictionary = {"cat":12, "dog":6, "elephant":23}
print(this_is_a_dictionary["dog"])
```

## <span class="mega-octicon octicon-tasklist"></span> Todo List App

We're going to create to-do list app.

### Todos los `To-do` to-dos

| Specification                                                                 |   Points   |
|:------------------------------------------------------------------------------|:----------:|
| Empty dictionary to store information                                         |     1      |
| Key for each day of the week                                                  |     1      |
| Each key has a list value that stores items                                   |     1      |
| User is prompted                                                              |     1      |
| User can type `add` program will ask what day and add it correctly            |     1      |
| User can type `get` and the program will ask for the day and print the values |     1      |
| **Extensions**                                                                | **Points** |
| Use .split() to allow the user to type `get Friday` and see the values        |     1      |
| Use .split() to make `add Friday watch tv and relax` update the list          |     1      |
| **Total**                                                                     |   _ / 8    |

Example Output

```
What would you like to do?
add
What day?
Friday
What would you like to add to Friday's to-do list?
practice clarinet
What would you like to do?
get
What day?
Friday
You have to practice clarinet.
What would you like to do?
```

## Our notes

```python
# some way to add
# some way to read
# some way to KEEP asking until exit


some_dictionary={
    "monday":[]

    #days of the week
}

def add():
    # loop this question...
        #append the action to the list value of the day keys
        some_dictionary[day].append(action)
    #until you...
    # I need an option to call choice()

def get():
    print(some_dictionary[day])
    # I need an option to call choice()

def choice():
    user_choice = input("How can I help you?")
    # if they choose 'add' call add()
    # if they choose 'get' call get()
add("something", "monday")

get("monday")
```

## Groups
| Choice                            | Functions                                                     | Get                                  | Lists                   | Looping                                                           |
|:----------------------------------|:--------------------------------------------------------------|:-------------------------------------|:------------------------|:------------------------------------------------------------------|
| Annalis, Crystal, Elizabeth, Eric | Anthony, Brianna, David, Emarie, Jose, Josue, Shakira, Soriel | Alexander, Alyssa, Kathryn, Matthew, | Axel, Jeremiah, Yaritza | Dallana, Devonte, Emily, Evelyn, Katia, Stephanie, Carlos, Nayeli |
