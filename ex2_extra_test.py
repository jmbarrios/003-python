import pytest
import homework


@pytest.mark.parametrize('test_input',[
    ([1,1,1,1,1,1,1,1,None])
])
def test_media(test_input):
    with pytest.raises(ValueError):
        homework.media(test_input)


@pytest.mark.parametrize('test_input',[
    ([None,None,None])
])
def test_desv_estandar(test_input):
    with pytest.raises(ValueError):
        homework.desv_estandar(test_input)


@pytest.mark.parametrize('test_input',[
    ([None,2]),
])
def test_normalizar(test_input):
    with pytest.raises(ValueError):
        homework.normalizar(test_input)
