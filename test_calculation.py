from калькулятор_дробей import add, sub, mult, div
import pytest


def test_add():
    assert add(1, 2, 1, 2) == (4, 4)
    assert add(1, 5, 2, 5) == (15, 25)



def test_div():
    with pytest.raises(ZeroDivisionError):
        div(1, 0, 2, 5)

