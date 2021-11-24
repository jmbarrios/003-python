import pytest
import homework


@pytest.mark.parametrize('test_input, expected',[
    ([[1,2]],[-1,1]),
])
def test_normalizar(test_input, expected):
    assert homework.normalizar(test_input)==expected
