import pytest
import homework


@pytest.mark.parametrize('test_input, expected',[
    ([1,1,1,1,1,1,1,1], 0),
    ([1,0,1,0,1,0], 0.5477225575051661),
    ([0.5,0.5,1,1], 0.28867513459481287)
])
def test_desv_estandar(test_input, expected):
    assert homework.desv_estandar(test_input)==expected
