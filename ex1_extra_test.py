import pytest
import homework

@pytest.mark.parametrize('test_input',[
    ('https://www.inaturalist.org/observations/80657e3'),
    ('https://classroom.google.com/u/1/c/Mzc2ODAzMzQ3NDY5'),
    ('https://www.facebook.com/AAAAAA')
])
def test_obten_id(test_input):
    with pytest.raises(TypeError):
        homework.obten_id(test_input)