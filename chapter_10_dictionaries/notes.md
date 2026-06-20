# Notes on Dictionaries

- **Time Complexity**: The transition from Lists (O(n) for lookups) to Dictionaries (O(1) for lookups) is one of the most profound performance leaps in software engineering. If you are constantly searching a list for a specific value, you should probably be using a dictionary or a set.
- **Global Variables**: Dictionaries are sometimes used as global configuration objects or caches (memoization). Because they are mutable, passing them around means any part of the program can update the cache.
- **JSON compatibility**: Python dictionaries map almost perfectly to JSON (JavaScript Object Notation), making them the backbone of web API communication.
