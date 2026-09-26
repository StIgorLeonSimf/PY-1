import pytest
from калькулятор_дробей import add, sub, mult, div

#
# def test_add():
#     assert add(1, 2, 1, 2) == (4, 4)
#     assert add(1, 5, 2, 5) == (15, 25)

@pytest.mark.parametrize('n1, d1, n2, d2, res',
                         [
                             (1, 2, 1, 2, (4, 4)),
                             (1, 5, 2, 5, (15, 25))
                         ])
def test_add(n1, d1, n2, d2, res):
    assert add(n1, d1, n2, d2 ) == res

# test_add()
# assert add(1, 2, 1, 2) == (4, 4)