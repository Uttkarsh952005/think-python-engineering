# Notes on Lists

- **Performance**: Accessing an element by index `[i]` is instantaneous (O(1)). Appending to the end of a list is fast. However, inserting or deleting from the *beginning* of a list (`t.pop(0)`) is slow (O(n)) because every subsequent element must be shifted over in memory.
- **Method side effects**: I must be very careful with methods that return `None`. Writing `t = t.sort()` destroys the list `t`, replacing it with `None`. 
- **List Comprehensions**: While Think Python introduces them later, the map/filter patterns discussed in this chapter are the exact use-case for list comprehensions.
