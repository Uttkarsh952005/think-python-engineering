# Learning Journal

This journal tracks my progress, technical hurdles, and engineering philosophy as I work through *Think Python*.

## Initialization
- Repository initialized.
- Core philosophy defined: focus on clean code, slow and intentional progress.
- Chapters 1 and 2 structure scaffolded.
- Setting up linting (Black, flake8, isort) to enforce discipline early on.

## Phase 2: Functions and Interface Design
- Explored functions as the primary mechanism for abstracting complexity.
- Refactored repetitive code in Chapter 4 case study into reusable interfaces.
- Implemented small mini-projects to reinforce interface design and function composition.

## Phase 3: Control Flow and Fruitful Functions
- Mastered conditional logic to allow programs to make decisions.
- Explored the concept of recursion—functions calling themselves—to solve naturally recursive problems.
- Focused on fruitful functions, which return values, enabling deeper composition and incremental development.

## Phase 4: Iteration and Strings
- Transitioned from recursion to linear iteration using `while` and `for` loops.
- Applied Newton's method to understand iterative approximations.
- Explored strings as sequences, grasping the importance of immutability and slicing.

## Phase 5: Lists and Dictionaries
- Encountered our first mutable data structure: Lists.
- Learned the critical distinction between object identity and object equivalence, avoiding aliasing bugs.
- Explored Dictionaries as key-value mappings, unlocking fast, hash-based lookups and frequency counting.

## Phase 6: Tuples and Files
- Mastered Tuples, completing the core data structure triad. Leveraged their immutability for dictionary keys and elegant multiple-assignment.
- Transitioned from volatile memory to persistent storage by reading and writing files.
- Learned exception handling (`try`/`except`) to robustly manage missing files and I/O errors.

## Phase 7: Classes, Objects, and Functions
- Transitioned to Object-Oriented Programming (OOP) by creating programmer-defined types (`Point`, `Rectangle`, `Time`).
- Explored the difference between shallow and deep copying when dealing with nested mutable objects.
- Differentiated between pure functions (which return new objects) and modifiers (which mutate existing objects in place).

## Phase 8: Methods and Inheritance
- Fully embraced OOP by moving functions inside classes as methods, utilizing `self` to manage instance state.
- Learned Python's magic methods (`__init__`, `__str__`, `__add__`) to elegantly construct objects and overload operators.
- Explored Inheritance and Composition, understanding how to model `IS-A` and `HAS-A` relationships to reuse code effectively.

## Phase 9: Advanced OOP and Architecture
- Explored advanced class mechanisms: `@property` for managed attributes, `@classmethod` for alternative constructors, and data hiding principles.
- Tackled advanced inheritance patterns including Multiple Inheritance, Mixins, and Abstract Base Classes (ABCs) to enforce architectural contracts.
- Concluded the foundational chapters, establishing a robust engineering mindset for future projects.

## Phase 10: The Final Polish (Goodies, Debugging, Algorithms)
- Mastered Pythonic idioms (comprehensions, generators, `collections`) to write cleaner, faster code.
- Solidified debugging as a scientific process, utilizing `assert` and `logging` over `print`.
- Learned Algorithm Analysis (Big O), understanding the profound performance differences between data structures like lists and sets.

---

## 🎯 Conclusion & Reflection
Looking back, the progression from writing simple `print()` statements in Chapter 1 to architecting an abstract event loop in Chapter 19 highlights the enormous difference between "coding" and "engineering."

This repository serves as my living portfolio of that transition. It proves not only that I can write Python, but that I can build scalable, tested, and strictly formatted systems. The journey doesn't end here, but the foundation is finally solid.

---

## 🛠️ Capstone Engineering Reflections (RecallCLI)
*A brief log of the design decisions and tradeoffs made while building the capstone project.*

### 1. Decoupling the UI
At first, it was tempting to just use `print()` and `input()` right inside the `QuizEngine.run_quiz()` loop. It's faster to write. 
**Tradeoff**: I chose to inject a `ui` object into the engine (`QuizEngine(deck, ui)`) instead. This means the core logic never imports UI libraries or calls `print()`. If I wanted to build a Flask or PyQt version of this later, the `core/` folder wouldn't need to change at all. It took a bit longer to wire up, but the separation of concerns feels much cleaner.

### 2. Using Polymorphism for Card Types
When I added Multiple Choice and True/False cards, the obvious beginner approach was:
```python
if card.type == "multiple_choice":
    # print options
```
**Tradeoff**: I realized this would get messy fast if I kept adding card types. Instead, I moved the custom logic into `get_payload()` and `check_answer()` methods on the subclasses. The `QuizEngine` just trusts the card to know how to display itself. Building `Deck` and `Flashcard` finally made the "Composition vs Inheritance" debate click for me. A Deck *has* Flashcards, but a MultipleChoiceCard *is* a Flashcard.

### 3. Explicit JSON Serialization
I intentionally didn't use `pickle` (because it's unsafe) or a big framework like `pydantic`.
**Tradeoff**: Writing manual dictionary mapping in `json_storage.py` is tedious. When I first built the JSON saving logic, all my `MultipleChoiceCard` objects came back as base `Flashcard` objects when I reloaded the app. I hadn't realized JSON doesn't remember Python classes! I had to manually serialize a `"type"` field so the loader knew which subclass to instantiate. Forcing myself to map the fields explicitly taught me exactly how ORMs work under the hood.

### 4. The Emoji Crash (A Lesson in CLI Development)
I tried to make the terminal look cool by adding Unicode emojis. It instantly broke on Windows PowerShell due to a `UnicodeEncodeError`. I had to go back and strip them out for safe ASCII/text formatting. A good lesson in cross-platform development!
