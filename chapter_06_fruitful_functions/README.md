# Chapter 6: Fruitful Functions

Up to this point, our functions have mostly been "void" — they performed actions (like printing) but didn't return values. Fruitful functions return results, allowing us to compose complex pipelines of logic.

## Core Concepts
- **Return Values**: The `return` statement immediately ends the function execution and sends a value back to the caller.
- **Incremental Development**: Writing a small amount of code, testing it, and adding more. This avoids massive debugging sessions.
- **Scaffolding**: Temporary code (like `print` statements) used during development to verify intermediate values, removed before finalization.
- **Composition**: Using the result of one function as an argument to another.
- **Boolean Functions**: Functions that return `True` or `False`. They are excellent for hiding complex conditional logic.

## Engineering Takeaways
- **Testing**: Fruitful functions are significantly easier to test than void functions. You can assert that given an input, the output matches an expectation.
- **Dead Code**: Code that appears after a `return` statement will never execute.
