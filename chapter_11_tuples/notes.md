# Notes on Tuples

- **Performance**: Tuples are slightly more memory efficient than lists and marginally faster to iterate over, but the primary reason to use them is semantic meaning: it communicates to the next engineer that "this collection of items should not change."
- **Data Structures**: `dict.items()` returns an iterable of `(key, value)` tuples. This is why the idiomatic way to loop through a dictionary is `for key, value in my_dict.items():`.
- **Tuple Unpacking**: Unpacking fails loudly if the number of variables on the left doesn't match the elements in the tuple on the right. This is a good thing (fail fast).
