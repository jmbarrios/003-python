import pytest
import homework


@pytest.mark.parametrize('test_input, expected',[
    ('000000000000000000', False),
    ('002539016003269411',True),
    ('a00000000000000000', False)
])
def test_valida_banco(test_input, expected):
    assert homework.valida_banco(test_input)==expected
