from test_17_rabota import A, calculator
import pytest
from contextlib import nullcontext as does_not_raise
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
        "x,y,res,expectation",
        [
            (1, 2, 0.5,does_not_raise()),
            (5,0,-5,pytest.raises(ZeroDivisionError)),
            (5,"f",1,pytest.raises(TypeError)),
        ]
    )
    def test_divide(self,x,y,res,expectation):
        with expectation:
                assert calculator().divide(x, y) == res

    @pytest.mark.parametrize(
        "x,y,res,expectation",
        [
            (1, 2, 3,does_not_raise()),
            (5, -1, 4,does_not_raise()),
        ]
    )
    def test_add(self,x, y, res,expectation):
        assert calculator().add(x, y) == res



