# Notes on Fruitful Functions

- **Pure Functions**: A function that takes arguments, returns a value, and has no side effects (like mutating global state or printing to the console) is a pure function. They are incredibly reliable and easy to reason about.
- **Incremental Development strategy**: 
  1. Start with a working program that does nothing (e.g., returns 0).
  2. Add small amounts of code.
  3. Use variables to hold intermediate values so you can inspect them.
  4. Once working, you can optionally consolidate statements to make the code concise, but only if it doesn't hurt readability.
