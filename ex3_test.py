import pytest
import homework

@pytest.mark.parametrize('test_input, expected',[
    ('000000000000000000', False),
    ('002539016003269411',True),
    ('a00000000000000000', False)
])
def test_valida_banco(test_input, expected):
    assert homework.valida_banco(test_input)==expected

@pytest.mark.parametrize('test_input, expected',[
    ('000000000000000000', False),
    ('002298016003269411',True),
    ('0000a0000000000000', False)
])
def test_valida_plaza(test_input, expected):
    assert homework.valida_plaza(test_input)==expected

@pytest.mark.parametrize('banco, plaza, nu_cuenta, expected',[
    ('002','010','07777777777', '002010077777777771'),
    ('014','028','00000555555','014028000005555557')
])
def test_calcula_clabe(banco, plaza, nu_cuenta, expected):
    assert homework.calcula_clabe(banco, plaza, nu_cuenta)==expected

@pytest.mark.parametrize('test_input, expected',[
    ('002010077777777771', True),
    ('0a2298016003269411',False),
    ('002010077777777773', False),
    ('000010077777777771', False),
    ('002000077777777771', False),
])
def test_plaza(test_input, expected):
    assert homework.valida_clabe(test_input)==expected