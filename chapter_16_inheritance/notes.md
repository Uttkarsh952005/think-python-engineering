# Notes on Inheritance

- **Overriding `__init__`**: When a child class overrides `__init__`, the parent's `__init__` is NOT called automatically. You must call it explicitly using `super().__init__()` if you want the parent's initialization logic to run.
- **Debugging Inheritance**: If a method isn't behaving as expected, you must check the object's class, then its parent, then its parent's parent. The Method Resolution Order (MRO) dictates this. Deep inheritance trees make code incredibly difficult to debug. Keep inheritance shallow.
- **Composition over Inheritance**: It's a common beginner mistake to use inheritance everywhere. If an object is composed of other objects, use attributes. Only use inheritance for structural "is a type of" relationships.
