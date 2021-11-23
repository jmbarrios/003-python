import pytest
import homework

@pytest.mark.parametrize('test_input, expected',[
    ([1,1,1,1,1,1,1,1], 1),
    ([1,0,1,0,1,0], 1/2),
    ([0.5,0.5,1,2], 1)
])
def test_media(test_input, expected):
    assert homework.media(test_input)==expected

@pytest.mark.parametrize('test_input, expected',[
    ([1,1,1,1,1,1,1,1], 0),
    ([1,0,1,0,1,0], 1/2),
    ([0.5,0.5,1,1], 0.25)
])
def test_desv_estandar(test_input, expected):
    assert homework.desv_estandar(test_input)==expected

@pytest.mark.parametrize('test_input, expected',[
    ([[1,2]],[-1,1]),
])
def test_normalizar(test_input, expected):
    assert homework.normalizar(test_input)==expected