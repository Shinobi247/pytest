# [Pytest - Conftest.py](https://www.tutorialspoint.com/pytest/pytest_conftest_py.htm)
import pytest
'''
define the fixture functions in this file to make them accessible across multiple test files
'''


@pytest.fixture
def input_value():
    input = 39
    return input
