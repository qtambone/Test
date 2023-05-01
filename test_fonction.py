from fonction import *

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(4, 7) != 10
    assert division(10, 2) == 5