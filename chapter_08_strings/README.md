# Chapter 8: Strings

A string is a sequence of characters. This chapter introduces the concept of sequences and how to manipulate, traverse, and search them.

## Core Concepts
- **Traversal**: Processing a sequence one element at a time using a `for` or `while` loop.
- **Slicing**: Extracting a segment of a string using bracket notation `[start:stop:step]`.
- **Immutability**: Strings cannot be changed once created. To "modify" a string, you must build a completely new one.
- **String Methods**: Built-in functions that operate on string objects (e.g., `.upper()`, `.find()`).
- **The `in` Operator**: A boolean operator that checks if one string is a substring of another.

## Engineering Takeaways
- **Immutability simplifies logic**: Because strings can't be changed, you never have to worry about a function accidentally modifying your string behind your back.
- **Idiomatic Python**: `for char in string:` is almost always preferred over `for i in range(len(string)):` unless the index itself is specifically needed.
