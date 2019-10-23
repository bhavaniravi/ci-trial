from ..app import Calculator
import pytest

def test_calculator():
    assert type(Calculator()) is Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 2 + 3

def test_subtract():
    calc = Calculator()
    assert calc.sub(2, 3) == 2 - 3

def test_power():
    calc = Calculator()
    assert calc.power(2, 3) == 2 ** 3

def test_fails_on_string():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.sub("2", "3")