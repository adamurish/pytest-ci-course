from pytest-ci-template.example import is_even

def test_is_even():
  assert is_even(2) is True
  assert is_even(3) is False
