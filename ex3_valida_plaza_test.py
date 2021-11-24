import pytest
import homework


@pytest.mark.parametrize('test_input, expected', [
    ('000000000000000000', False),
    ('002298016003269411',True),
    ('0000a0000000000000', False)
])
def test_valida_plaza(test_input, expected):
    assert homework.valida_plaza(test_input)==expected
