# Chapter 16: Inheritance

Inheritance is the ability to define a new class that is a modified version of an existing class. It allows for massive code reuse and logically structured hierarchies.

## Core Concepts
- **Class Attributes**: Variables defined inside a class but outside any method. They are associated with the class itself, not any specific instance.
- **Inheritance**: A child class inherits all attributes and methods of its parent class.
- **Overriding**: A child class can provide a new implementation for a method defined in its parent class (e.g., overriding `__init__` or `__str__`).
- **`super()`**: A built-in function that allows a child class to call a method from its parent class (useful when overriding `__init__`).

## Engineering Takeaways
- **HAS-A vs IS-A**: 
  - *Composition (HAS-A)*: A Rectangle has a Point. A Deck has Cards. 
  - *Inheritance (IS-A)*: A Hand is a kind of Deck. A Poodle is a kind of Dog. 
  - Favor composition over inheritance unless the IS-A relationship is absolute.
- **Class vs Instance Attributes**: Class attributes are shared across all instances (like a constant dictionary mapping card suits to strings). Modifying them affects everything. Instance attributes (`self.x`) are unique to the object.
