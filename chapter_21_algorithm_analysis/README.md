# Chapter 21: Analysis of Algorithms

Performance only matters when it matters. However, as an engineer, you must understand the theoretical limits of your algorithms so you know *when* it will matter.

## Core Concepts
- **Big O Notation**: A mathematical way of describing how the runtime or space requirements of an algorithm grow as the input size grows.
- **O(1) - Constant Time**: Takes the same amount of time regardless of input size (e.g., looking up a key in a dictionary).
- **O(n) - Linear Time**: Takes time proportional to the input size (e.g., looping through a list).
- **O(n^2) - Quadratic Time**: Takes time proportional to the square of the input size (e.g., a nested loop).
- **Search Algorithms**: Linear Search (O(n)) vs Binary Search (O(log n)).
- **Sorting Algorithms**: Bubble Sort (O(n^2)) vs Merge Sort/Timsort (O(n log n)).

## Engineering Takeaways
- **Data Structures dictate Algorithms**: You cannot perform a Binary Search on an unsorted list or a standard dictionary. Choosing the right data structure (Set vs List) is often the most important architectural decision you will make.
- **Premature Optimization is the Root of All Evil**: Do not write complex, unreadable O(n log n) code if the list will never have more than 100 items. A simple O(n) loop is fine for small inputs. Optimize only when profiling proves it's a bottleneck.
