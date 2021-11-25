import pytest
import homework


@pytest.mark.parametrize('test_input, expected',[
    ([1,2],[-0.7071067811865475, 0.7071067811865475]),
])
def test_normalizar(test_input, expected):
    assert homework.normalizar(test_input)==expected
