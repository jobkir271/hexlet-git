from test_17_rabota import A, calculator
import pytest
from typing import Union
def test_main():
    assert 1 == 1

def test_test_1():
    assert A.x == 1

def test_test_3():
    assert A.x + A.y == 3

def test_test_4():
    x = 1
    y = 2
    while x < y:
        x += 1
    assert x == 2




class TestClass:
    @pytest.mark.parametrize(
        "x,y,res",
        [
            (1, 2, 0.5),
            (5,-1,-5),
        ]
    )
    def test_divide(self,x,y,res):
        assert calculator().divide(x, y) == res

    @pytest.mark.parametrize(
        "x,y,res",
        [
            (1, 2, 3),
            (5, -1, -4),
        ]
    )
    def test_add(self,x, y, res):
        assert calculator().add(x, y) == res



