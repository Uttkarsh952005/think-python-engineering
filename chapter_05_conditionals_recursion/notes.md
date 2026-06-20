# Notes on Conditionals and Recursion

- **Flat is better than nested**: Deeply nested `if` statements are hard to read. Often, `elif` chains or early `return` statements (guard clauses) can flatten the logic.
- **Recursion Depth**: Python has a limit on how deep recursion can go (usually 1000 stack frames). This means recursion is elegant but not always the most practical tool for long linear sequences in Python, unlike languages with tail-call optimization.
- **Infinite Recursion**: Forgetting a base case leads to infinite recursion and a `RecursionError`. It is the recursive equivalent of an infinite loop.
