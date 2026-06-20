# Notes on Strings

- **Off-by-one errors**: When using indices, it's very easy to access `len(string)`, which causes an `IndexError` because indices start at `0` and go up to `len(string) - 1`.
- **String Building**: Because strings are immutable, repeatedly concatenating them in a loop (`s = s + "a"`) creates a new string object every time. While fine for small strings, it becomes highly inefficient for large amounts of text. (In real-world Python, `.join()` is used for performance).
- **Duck Duck Goose**: The `find` pattern (returning an index or `-1`) is a classic computer science pattern, though in modern Python, we often just rely on the built-in `.find()` method or the `in` operator.
