"""Tests for the public package interface."""

from calcutils import add, average, multiply


def test_add():
    assert add(10, 25) == 35


def test_multiply():
    assert multiply(5, 4) == 20


def test_average():
    assert average([10, 20, 30, 40]) == 25.0


def test_average_empty():
    assert average([]) == 0.0
