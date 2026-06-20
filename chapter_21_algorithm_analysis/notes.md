# Notes on Algorithm Analysis

- **Space vs Time Tradeoffs**: Often, you can make an algorithm faster (reduce Time Complexity) by using more memory (increasing Space Complexity). For example, caching/memoization stores previous answers in memory so you don't have to compute them again.
- **Constants don't matter in Big O**: An algorithm that takes `5n` steps is still O(n). An algorithm that takes `n^2 / 2` steps is still O(n^2). As `n` approaches infinity, the constants become irrelevant.
- **Python's `in` operator**: The `in` keyword hides complexity. `x in list` is O(n). `x in dict` is O(1). Be very careful when using `in` inside a `for` loop. If it's a list, you've just accidentally created an O(n^2) algorithm.
