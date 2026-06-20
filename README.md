<div align="center">
  <h1>🐍 Think Python — Engineering Journey</h1>
  <p><em>An autonomous engineering system and public learning journal</em></p>
  
  <p>
    <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
    <img alt="Python 3.10+" src="https://img.shields.io/badge/python-3.10+-blue.svg">
    <img alt="Tests" src="https://img.shields.io/badge/tests-passing-brightgreen.svg">
  </p>
</div>

---

## 📖 Mission & Philosophy

Welcome to my software craftsmanship portfolio. This repository tracks my progression through *Think Python* (Allen B. Downey). However, this isn't just a collection of tutorial scripts. My goal was to treat the learning process as a rigorous **engineering discipline**. 

I focused heavily on:
- **Clean Architecture:** Avoiding massive unstructured files.
- **Readability:** Strict adherence to PEP8, explicit typing, and descriptive variable names.
- **Practical Application:** Translating abstract concepts into CLI tools, simulators, and games.
- **Mental Models:** Explaining the *why* alongside the *how*.

## 🏗️ What's Inside?

The repository is structured methodically, chapter by chapter. Each chapter acts as a self-contained module demonstrating specific engineering patterns.

Inside every chapter directory, you will find exactly five files:
1. `README.md`: High-level concepts and engineering takeaways.
2. `notes.md`: Personal insights, mental models, and debugging strategies.
3. `examples.py`: Clean, well-documented code exploring the chapter's mechanics.
4. `exercises.py`: Implementations of algorithms and problem-solving tasks.
5. `mini_project.py`: A practical application tying the chapter together (e.g., CLI tools, games, automated simulators).

### 🛠️ Key Milestones
- **[Chapters 1-6](./chapter_01_way_of_program):** Procedural foundations, control flow, pure functions, and recursion.
- **[Chapters 7-12](./chapter_07_iteration):** State management, linear iteration, data structures (lists, dicts, tuples), and file I/O.
- **[Chapters 13-18](./chapter_13_classes_objects):** Object-Oriented Programming, Magic Methods, Composition, Inheritance, and Architectural Design Patterns.
- **[Chapters 19-21](./chapter_19_the_goodies):** Pythonic Idioms, Debugging Strategies, and Algorithm Analysis (Big O Notation).

## 🚀 Running the Code Locally

This repository is optimized for clean execution and automated testing.

**1. Clone the repository:**
```bash
git clone https://github.com/yourusername/think-python-engineering.git
cd think-python-engineering
```

**2. Setup a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

**3. Install linting & testing dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run formatting and tests:**
```bash
black .
isort .
flake8 .
pytest tests/
```

---
*This is a living engineering notebook. Follow my progress in the [LEARNING_JOURNAL.md](./LEARNING_JOURNAL.md).*
