"""
Basic test suite to verify core functions across chapters.
Ensures CI/CD pipelines can validate the repository.
"""

import os
import sys

import pytest

# Add the project root to sys.path so we can import chapter modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import from chapter 6
from chapter_06_fruitful_functions.exercises import is_palindrome

# Import from chapter 11
from chapter_11_tuples.exercises import sumall

# Import from chapter 13
from chapter_13_classes_objects.exercises import Point, distance_between_points


def test_is_palindrome():
    """Validates the recursive palindrome logic."""
    assert is_palindrome("racecar") is True
    assert is_palindrome("redivider") is True
    assert is_palindrome("python") is False
    assert is_palindrome("noon") is True


def test_sumall():
    """Validates the *args tuple gathering function."""
    assert sumall(1, 2, 3) == 6
    assert sumall(10.5, 20.2) == 30.7
    assert sumall() == 0


def test_distance_between_points():
    """Validates basic OOP math."""
    p1 = Point()
    p1.x, p1.y = 0, 0

    p2 = Point()
    p2.x, p2.y = 3, 4

    # 3-4-5 right triangle
    assert distance_between_points(p1, p2) == 5.0
