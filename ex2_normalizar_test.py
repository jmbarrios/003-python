import pytest
import homework


@pytest.mark.parametrize('test_input, expected',[
    ([[1,2]], [-0.707106, 0.707106]),
])
def test_normalizar(test_input, expected):
    assert homework.normalizar(test_input) == pytest.approx(expected,
                                                            abs=0.000001)
