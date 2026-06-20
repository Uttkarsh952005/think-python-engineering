# Chapter 11: Tuples

A tuple is a sequence of values. They are very similar to lists, but with one critical difference: **tuples are immutable**. You cannot modify, append, or remove elements from a tuple once it's created.

## Core Concepts
- **Immutability**: Syntactically, tuples are comma-separated values, often enclosed in parentheses `(1, 2, 3)`.
- **Tuple Assignment**: An elegant way to swap values or unpack structures: `a, b = b, a`.
- **Multiple Return Values**: Functions can only return one value, but if that value is a tuple, it effectively returns multiple values.
- **Variable-length Arguments (`*args`)**: Functions can take an arbitrary number of arguments, gathering them into a tuple.
- **Tuples as Dictionary Keys**: Because tuples are immutable (and therefore hashable), they can be used as keys in a dictionary. Lists cannot.

## Engineering Takeaways
- **The DSU Pattern (Decorate, Sort, Undecorate)**: A classic pattern for complex sorting. You build a list of tuples where the first element is the sort key (decorate), sort the list (sort), and extract the data (undecorate).
- **`zip()`**: A built-in function that takes two or more sequences and interleaves them into an iterator of tuples.
