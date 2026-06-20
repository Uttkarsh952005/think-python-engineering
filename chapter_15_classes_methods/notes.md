# Notes on Classes and Methods

- **Syntactic Sugar**: Writing `time.print_time()` is translated by Python into `Time.print_time(time)`. The object before the dot becomes the `self` argument. Understanding this demystifies why every method requires `self` as the first parameter.
- **Fail Fast Initialization**: `__init__` is crucial because it ensures that an object is created in a valid state. If an object requires an X and Y coordinate, enforcing that in `__init__` prevents bugs where an object is passed around half-initialized.
- **Type-Based Dispatch**: Checking `isinstance(other, Time)` inside `__add__` allows our objects to behave intelligently whether we add another object to them, or just a raw integer.
