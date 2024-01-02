import pytest
import allure
def test_first_():
  print("This is test")
  
@pytest.Mark.sanity
def test_second_():
  print("This is second")
