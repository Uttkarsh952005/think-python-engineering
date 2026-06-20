# Notes on The Goodies

- **Overusing Comprehensions**: While list comprehensions are beautiful, they can become unreadable monsters if nested too deeply. If a comprehension spans multiple lines and has multiple `if`/`for` clauses, it is usually better engineering practice to rewrite it as a standard `for` loop for readability.
- **The Magic of `any` and `all`**: These functions short-circuit. If `any()` finds a `True` value on the first item, it stops checking the rest. Combined with generator expressions, they form highly optimized query engines: `any(is_prime(n) for n in massive_list)`.
- **`defaultdict` saves time**: Before `defaultdict`, engineers constantly had to write `if key not in d: d[key] = []`. `defaultdict` handles this internally, resulting in cleaner, faster code.
