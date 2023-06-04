# [Pytest - Starting With Basic Test](https://www.tutorialspoint.com/pytest/pytest_starting_with_basic_test.htm)
import math
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 40

def tesequality():
   assert 10 == 11