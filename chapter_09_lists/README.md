# Chapter 9: Lists

While strings are sequences of characters, lists are sequences of *anything*. More importantly, unlike strings, lists are **mutable**—they can be changed after creation. This introduces immense power, but also new categories of bugs.

## Core Concepts
- **Mutability**: You can change an element inside a list without creating a new list object (e.g., `numbers[0] = 5`).
- **List Operations & Methods**: `+` concatenates, `*` repeats. Methods like `.append()`, `.extend()`, and `.sort()` modify lists in-place.
- **Map, Filter, Reduce**: Common patterns for processing lists:
  - *Map*: Applying an operation to every element.
  - *Filter*: Selecting elements that meet a criteria.
  - *Reduce*: Combining elements into a single value (e.g., sum).
- **Objects and Values**: If `a = [1, 2, 3]` and `b = [1, 2, 3]`, they have the same *value* but are different *objects*.
- **Aliasing**: If `a = b`, both variables point to the same object. Modifying `a` modifies `b`.

## Engineering Takeaways
- **Beware of Aliasing**: Passing a list into a function means the function can modify the original list. If you don't want this, pass a copy (`my_list[:]`).
- **In-place vs Returning**: `.sort()` modifies a list and returns `None`. `sorted()` returns a new sorted list and leaves the original untouched. Mixing these up is a common beginner mistake.
