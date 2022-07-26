import pytest
from first_part import RomanNumberError

from romanos_funcional import entero_a_romano, romano_a_entero, RomanNumberError

"""
Casos de prueba
a) 1994 -> MCMXCIV
b) 4000 -> RomanNumberError("El valor debe ser menor de 4000")
c) "unacadena" -> RomanNumberError("Debe ser un entero")
d) 0 -> RomanNumberError("El valor debe ser mayor de cero")
e) -3 -> RomanNumberError("El valor debe ser mayor de cero")
f) 4.5 -> RomanNumberError("Debe ser un entero")


"""



def test_3_es_igual_a_2_mas_uno():
    assert 2 + 1 == 3


def test_error_si_entero_mayor_de_3999():
    assert entero_a_romano(1994) == 'MCMXCIV'

def test_336():
    assert entero_a_romano(336) == 'CCCXXXVI' #['0000', '300', '30', '6'] 

def test_1336():
    assert entero_a_romano(1336) == 'MCCCXXXVI'

def test_romano_a_entero_ordenados():
    assert romano_a_entero('I') == 1
    assert romano_a_entero('MDCCXIII') == 1713

def test_romano_a_entero_no_mas_de_tres():

    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero('LIIII')
    
    assert str(exceptionInfo.value) == "No se pueden dar más de tres repeticiones"

def test_romano_a_entero_resta_si_soy_mayor_que_anterior():
    assert romano_a_entero('IV') == 4

def test_romano_solo_hasta_un_orden_de_magnitud_en_la_resta():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero('IC')
    assert str(exceptionInfo.value) == "I solo se puede restar a V y X"
