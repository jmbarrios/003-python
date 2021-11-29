import pytest
import homework


@pytest.mark.parametrize('test_input, expected',[
    ([1,1,1,1,1,1,1,1], 0),
    ([1,0,1,0,1,0], 0.5477),
    ([0.5,0.5,1,1], 0.2886)
])
def test_desv_estandar(test_input, expected):
    assert homework.desv_estandar(test_input) == pytest.approx(expected, 0.0001)
