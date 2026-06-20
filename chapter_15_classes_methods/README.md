# Chapter 15: Classes and Methods

Object-Oriented Programming (OOP) is fully realized when we combine data (attributes) and behavior (functions) into a single entity. Functions defined inside a class are called **methods**.

## Core Concepts
- **Methods**: Functions attached to an object. Invoked using dot notation (e.g., `time.print_time()`).
- **The `self` Parameter**: The first parameter of a method automatically refers to the instance invoking it. By convention, it is named `self`.
- **Initialization (`__init__`)**: A special "magic" method invoked automatically when a new object is created. It sets up the initial state, replacing the dangerous practice of assigning attributes externally.
- **String Representation (`__str__`)**: A magic method that dictates what happens when you `print(object)` or call `str(object)`.
- **Operator Overloading**: Magic methods like `__add__` allow objects to use standard operators (e.g., `time1 + time2`).

## Engineering Takeaways
- **Data Hiding / Encapsulation**: Methods provide an interface. The user of your class shouldn't need to know *how* `__add__` works internally, they just need to know they can use `+`.
- **Polymorphism**: Functions that can work with several types. If a function uses `+`, and your class implements `__add__`, your class is polymorphic with that function.
