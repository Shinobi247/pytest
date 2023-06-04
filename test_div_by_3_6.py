# [Pytest - Fixtures](https://www.tutorialspoint.com/pytest/pytest_fixtures.htm)
from typing import Literal
import pytest


def test_divisible_by_3(input_value: Literal[39]):
    assert input_value % 3 == 0


def test_divisible_by_6(input_value: Literal[39]):
    assert input_value % 6 == 0
