import pytest
import homework


@pytest.mark.parametrize('test_input, expected',[
    ('002010077777777771', True),
    ('0a2298016003269411',False),
    ('002010077777777773', False),
    ('000010077777777771', False),
    ('002000077777777771', False),
])
def test_plaza(test_input, expected):
    assert homework.valida_clabe(test_input)==expected
