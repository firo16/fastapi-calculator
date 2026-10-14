from fastapi.testclient import TestClient

import main



client = TestClient(main.app)

def test_endpoint_dodawania(monkeypatch):
    monkeypatch,setattr(
        main,
        'zapisz obliczenie',
        lambda liczba1, dzialanie, liczba2, wynik: None
    )

    odpowiedz = client.post(
        '/oblicz',
        json={
            'liczba1': 10,
            'dzialanie': '+',
            'liczba2': 5,
        }
    )

    assert odpowiedz.status_code == 200
    assert odpowiedz.json() == {'wynik':15}


def test_endpoint_dzielenia_przez_zero():
    odpowiedz = client.post(
        '/oblicz',
        json={
            'liczba1': 10,
            'dzialanie': '/',
            'liczba2': 0
        }
    )

    assert odpowiedz.status_code == 400
    assert odpowiedz.json() == {'detail':'serio? zero??'}

def test_brak_drugiej_liczby():
    odpowiedz = client.post(
        '/oblicz',
        json={
            'liczba1': 10,
            'dzialanie': '+'
        }
    )

    assert odpowiedz.status_code == 422

def test_nieprawidlowa_liczba():
    odpowiedz = client.post(
        "/oblicz",
        json={
            "liczba1": "ziemniak",
            "dzialanie": "+",
            "liczba2": 5
        }
    )

    assert odpowiedz.status_code == 422