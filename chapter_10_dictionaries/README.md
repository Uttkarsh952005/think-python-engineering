# Chapter 10: Dictionaries

While lists use integers as indices to look up values, dictionaries (dicts) use almost any type as an index. A dictionary is a mapping between a set of indices (keys) and a set of values.

## Core Concepts
- **Key-Value Pairs**: The fundamental structure of a dictionary (`{'key': 'value'}`).
- **Hash Tables**: The underlying implementation of a dictionary. Looking up a key is extremely fast (O(1)), regardless of how large the dictionary gets.
- **Keys Must Be Hashable**: Keys must be immutable types (like strings, integers, or tuples). You cannot use a list as a dictionary key.
- **Histogram Pattern**: Dictionaries are incredibly useful for counting frequencies of items in a collection.
- **Reverse Lookup**: Finding a value given a key is fast. Finding a key given a value requires a slow, linear search.

## Engineering Takeaways
- **`.get()` Method**: Trying to access a non-existent key throws a `KeyError`. Using `d.get(key, default_value)` is a safer way to retrieve values, especially when counting.
- **Dictionaries are unordered (mostly)**: Prior to Python 3.7, dictionaries did not guarantee order. While modern Python maintains insertion order, algorithms should rarely rely on this property.
