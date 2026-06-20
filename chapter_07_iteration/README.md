# Chapter 7: Iteration

Iteration is the ability to run a block of statements repeatedly. While recursion achieves repetition by having a function call itself, iteration uses dedicated loop structures to maintain state and execute code until a condition is met.

## Core Concepts
- **Multiple Assignment**: A variable can point to one value, and later point to a completely different value (`x = 5`, then `x = 7`).
- **Updating Variables**: Changing a variable by depending on its previous value (`x = x + 1`).
- **The `while` Statement**: Executes a block of code continuously as long as a boolean expression remains `True`.
- **`break` Statement**: Used to exit a loop immediately, bypassing the loop's conditional check.
- **Algorithms**: A mechanical process for solving a category of problems (e.g., Newton's method for finding square roots).

## Engineering Takeaways
- **State Management**: Iteration requires careful management of state (variables changing over time). If state is not updated correctly, infinite loops occur.
- **`while True` pattern**: Often used with `break` to wait for an event, allowing the loop exit condition to be placed anywhere in the loop body rather than just at the top.
