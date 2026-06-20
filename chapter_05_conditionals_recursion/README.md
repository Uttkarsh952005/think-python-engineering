# Chapter 5: Conditionals and Recursion

This chapter introduces the ability to make decisions and repeat actions without relying on standard looping constructs. It shifts programs from linear scripts to dynamic systems.

## Core Concepts
- **Modulus Operator (`%`)**: Yields the remainder. Excellent for determining divisibility (e.g., `x % 2 == 0`).
- **Boolean Expressions**: Expressions that evaluate to `True` or `False`.
- **Logical Operators**: `and`, `or`, `not` allow combining boolean expressions.
- **Conditional Execution**: `if`, `elif`, `else` statements control the flow of execution based on conditions.
- **Recursion**: A function that calls itself. It requires a base case to terminate and a recursive step that moves towards the base case.

## Engineering Takeaways
- **Guard Clauses**: Instead of deeply nesting `if` statements, return early when a condition is not met. It keeps the "happy path" unindented.
- **Mental Models of Recursion**: Trust the recursion. When writing a recursive step, assume the recursive call works correctly for the smaller sub-problem.
