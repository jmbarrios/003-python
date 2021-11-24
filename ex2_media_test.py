import pytest
import homework


@pytest.mark.parametrize('test_input, expected',[
    ([1,1,1,1,1,1,1,1], 1),
    ([1,0,1,0,1,0], 1/2),
    ([0.5,0.5,1,2], 1)
])
def test_media(test_input, expected):
    assert homework.media(test_input)==expected
