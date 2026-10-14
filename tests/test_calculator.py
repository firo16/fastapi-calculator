import pytest
from _kalkulator import obliczanie



def test_dodawania():
    wynik = obliczanie(10,"+",5)

    assert wynik == 15

def test_odejmowania():
    wynik = obliczanie(80,'-',20)

    assert wynik == 60


def test_mnozenia():
    wynik = obliczanie(20,'*',6)

    assert wynik == 120


def test_dzielenia():
    wynik = obliczanie(25,'/',5)

    assert wynik == 5


def test_dzielenia_calkowitego():
    wynik = obliczanie(13,'//',2)

    assert wynik == 6


def test_test_reszty_z_dzielenia():
    wynik = obliczanie(27,'%',5)

    assert wynik == 2


def test_potegowania():
    wynik = obliczanie(2,"^",8)

    assert wynik == 256


def test_dzielenia_przez_zero():
    with pytest.raises(ZeroDivisionError):
        obliczanie(10,'/',0)
