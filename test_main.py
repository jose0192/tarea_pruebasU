import pytest
from main import suma,resta,multiplicacion,division

def test_sumar1():
    assert suma(3, 2) == 5

def test_sumar2():
    assert suma(-3, -2) == -5

def test_restar1():
    assert resta(5, 3) == 2

def test_restar2():
    assert resta(-5, -3) == -2

def test_multiplicar1():
    assert multiplicacion(3, 2) == 6

def test_multiplicar2():
    assert multiplicacion(-3, -2) == 6

def test_dividir1():
    assert division(6, 3) == 2

def test_dividir2():
    assert division(-6, -3) == 2

if __name__=='__main__':
    test_sumar1()
    test_sumar2()
    test_restar1()
    test_restar2()
    test_multiplicar1()
    test_multiplicar2()
    test_dividir1()
    test_dividir2()