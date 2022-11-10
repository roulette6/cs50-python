# My CS50 Python psets and final project
* This repo contains my lecture scrips and psets for the [CS50 Python course](https://cs50.harvard.edu/python/2022/).
* pset4/figlet has a handy code same for the `pyfiglet` library.
* The final project has a detailed README.md

## The following topics were covered in lecture 9
* `set`: houses.py
* `global`: bank_global.py
    - bank.py is a better solution, b/c all functions in a class have access to the instance var.
* `constants`: cont_meows.py
    - Like in private properties, Python doesn't enforce this. Honor system.
* `type hints`: bark.py
    - Python doesn't enforce type hints, but you can use a tool such as `mypy`
    - `$ mypy bark.py`
* `docstrings`: bark.py
    - If you adhere to convention with docstrings, there are tools that will generate documentation for you.
* `argparse`: meows.py
* `unpacking`: unpack.py
    - Unpack lists with `*`
    - Unpack dicts with `**`
    - A function such as `def f(*args, **kwargs):` can take a variable number of positional or keyword arguments
* `map`: yell.py
    - Python is procedural, object-oriented, and __functional__. Functional programming relies on functions that take inputs and return values w/o side effects.
    - `map` lets you apply a function to every item in an iterable.
* `list comprehensions`: yell.py, gryffindors.py
    - Pythonic way of processing items in a list: In the example below, execute the function on every item on the list.
    - `foo = [bar.upper() for bar in bat]`
    - `gryf = [dude["name"] for dude in dudes if dude["house"] == "Gryffindor"]`
* `filter`: gryffindors.py
    - `filter` expects a function that returns True or False
* `dict comprehensions`: dict_gryf.py
* `enumerate`: enum_gryf.py
* `generators`, `iterators`, `yield`: sleep.py
    - A program that generates massive amounts of data can tax the system's RAM or CPU badly enough for the program to hang and eventually quit.
    - Generator functions can generate massive amounts of data, but `yield` returns an `iterator` that allows a loop in main to iterate through the generated values one at a time.
