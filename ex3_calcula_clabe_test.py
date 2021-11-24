import pytest
import homework


@pytest.mark.parametrize('banco, plaza, nu_cuenta, expected',[
    ('002','010','07777777777', '002010077777777771'),
    ('014','028','00000555555','014028000005555557')
])
def test_calcula_clabe(banco, plaza, nu_cuenta, expected):
    assert homework.calcula_clabe(banco, plaza, nu_cuenta)==expected
