# [Pytest - Parameterizing Tests](https://www.tutorialspoint.com/pytest/pytest_parameterizing_tests.htm)
import pytest

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   if num == 3:
      assert not 11*num == output
   else:
      assert 11*num == output