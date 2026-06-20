# Chapter 20: Debugging

Debugging is a fundamental engineering skill. It is the process of identifying, isolating, and fixing bugs. It requires patience, systematic thinking, and a willingness to question your own assumptions.

## Core Concepts
- **Syntax Errors**: Caught by the interpreter before the code runs. Usually typos or indentation issues.
- **Runtime Errors (Exceptions)**: Occur while the program is running (e.g., dividing by zero, reading a missing file).
- **Semantic Errors**: The code runs perfectly without crashing, but does the *wrong thing*. These are the hardest to find.
- **Bisection Debugging**: Cutting the search space in half. Print the state halfway through the program to see if the bug happened before or after that point.
- **Rubber Duck Debugging**: Explaining your code line-by-line to an inanimate object. The act of verbalizing forces your brain to evaluate the logic objectively.

## Engineering Takeaways
- **Bugs are Science**: Debugging is the scientific method. You observe a failure, form a hypothesis about the cause, design a test (add a print statement or an assert), and run it to prove or disprove your hypothesis.
- **Don't guess**: Changing code randomly hoping it fixes the bug is a recipe for disaster. Understand *why* it is broken before changing it.
- **Fail Fast**: Use assertions (`assert type(x) == int`) to crash the program immediately when an assumption is violated, rather than letting corrupted data propagate silently.
