"""
Chapter 15: Classes and Methods
Refactoring the Time class to use methods and magic methods.
"""


class Time:
    """Represents the time of day."""

    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        """Initializes the Time object with optional default values."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self) -> str:
        """Returns a string representation of the time."""
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def time_to_int(self) -> int:
        """Converts internal state to an integer representation."""
        minutes = self.hour * 60 + self.minute
        return minutes * 60 + self.second

    def __add__(self, other: "Time") -> "Time":
        """Overloads the + operator."""
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            # Type-based dispatch: handle adding an integer (seconds)
            return self.increment(other)

    def add_time(self, other: "Time") -> "Time":
        """Adds two Time objects."""
        seconds = self.time_to_int() + other.time_to_int()
        return self.int_to_time(seconds)

    def increment(self, seconds: int) -> "Time":
        """Adds integer seconds to a Time object."""
        seconds += self.time_to_int()
        return self.int_to_time(seconds)

    # Note: Using @classmethod is advanced for this chapter,
    # but clean for factory methods. We'll use a static approach here.
    def int_to_time(self, seconds: int) -> "Time":
        """Helper to create a new Time object from an integer."""
        t = Time()
        minutes, t.second = divmod(seconds, 60)
        t.hour, t.minute = divmod(minutes, 60)
        return t


def main():
    # Utilizing __init__
    start = Time(9, 45)
    duration = Time(1, 35)

    print("--- Magic Methods ---")
    # Utilizing __str__
    print(f"Start: {start}")
    print(f"Duration: {duration}")

    # Utilizing __add__
    end = start + duration
    print(f"End: {end}")

    # Utilizing Type-Based Dispatch in __add__
    later = end + 1800  # Add 30 minutes (1800 seconds)
    print(f"30 minutes later: {later}")


if __name__ == "__main__":
    main()
