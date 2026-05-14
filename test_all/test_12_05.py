#пайтест, фикстуры маркеры,фикстуры параметризации, параметризация ошибок,
import pytest
from contextlib import nullcontext as does_not_raise
@pytest.fixture
def print_mod():
    print("прогнал тестик")


@pytest.mark.usefixtures("print_mod")
class TestCalculator:

    @pytest.mark.parametrize(
        "x,y,res,expected",
        [
            (1, 2, 3,does_not_raise()),
            (4, 5, 9,does_not_raise()),
            (7, 8, "15",pytest.raises(AssertionError)),
        ]
    )
    def test_calculator_add(self,x, y, res,expected):
        with expected:
            assert x + y == res

    @pytest.mark.parametrize(
        "x,y,res,expected",
        [
            (1, 2, -1,does_not_raise()),
            (4, 5, -1,does_not_raise()),
            (7, 8, -1,does_not_raise()),
        ]
    )
    def test_calculator_minus(self,x, y, res,expected):
        with expected:
            assert x - y == res


