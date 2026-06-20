# Chapter 12: Files

Everything we've built so far is volatile—when the program ends, the data disappears. To create lasting applications, we must persist data to secondary memory (the file system).

## Core Concepts
- **Persistence**: Data that outlives the process that created it.
- **Reading and Writing**: `open()` returns a file object. You must specify the mode: `'r'` for reading, `'w'` for writing, `'a'` for appending.
- **File Pointers**: When you read a file, an invisible pointer moves through it. You cannot read the same line twice without resetting the pointer.
- **Catching Exceptions**: File operations are prone to errors (file not found, permissions denied). `try`/`except` blocks prevent the program from crashing abruptly.
- **Context Managers (`with`)**: The safest way to handle files, ensuring they are closed even if an error occurs.

## Engineering Takeaways
- **Resource Leaks**: Failing to `.close()` a file leaves it locked by the OS. Context managers (`with open() as f:`) solve this elegantly and should almost always be used.
- **File Paths**: `os.path` (or `pathlib`) is crucial for building robust software that runs on both Windows (which uses `\`) and Unix/Mac (which uses `/`).
