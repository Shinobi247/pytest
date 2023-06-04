# [Pytest - Conftest.py](https://www.tutorialspoint.com/pytest/pytest_conftest_py.htm)
import pytest

def test_divisible_by_13(input_value):
   assert input_value % 13 == 0