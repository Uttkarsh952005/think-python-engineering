# Notes on Iteration

- **Iteration vs Recursion**: Anything that can be done with iteration can be done with recursion, and vice versa. However, in Python, `while` loops are much more memory efficient for long sequences because they don't consume a new stack frame for every step.
- **The Loop Mental Model**: When debugging loops, I must trace the values of variables immediately before the condition is checked, and immediately after the update step.
- **Infinite Loops**: It's common to accidentally create an infinite loop. Using `Ctrl+C` in the terminal to raise a `KeyboardInterrupt` is an essential tool.
