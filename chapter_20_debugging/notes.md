# Notes on Debugging

- **Print statements vs Logging**: Beginners use `print()` to debug. Professionals use the `logging` module. Why? Because you can leave `logging.debug()` in your code forever and just flip a switch to hide them in production. Print statements have to be manually deleted, which risks deleting real code.
- **The 80/20 Rule**: You will spend 20% of your time writing code, and 80% of your time debugging it. This is normal. Do not feel frustrated when code doesn't work on the first try.
- **Git as a debugging tool**: If the code worked yesterday but is broken today, `git diff` is your best friend. The bug is almost certainly inside the lines that changed.
