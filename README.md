FastAPI Calculator
Kalkulator internetowy zbudowany przy użyciu Pythona, FastAPI, JavaScriptu i SQLite.

Aplikacja wykonuje podstawowe działania matematyczne, zapisuje poprawne obliczenia w bazie danych oraz wyświetla historię ostatnich wyników.

Funkcje
dodawanie
odejmowanie
mnożenie
dzielenie
dzielenie całkowite
potęgowanie
reszta z dzielenia
obsługa liczb dziesiętnych
obsługa myszy i klawiatury
walidacja danych za pomocą Pydantic
obsługa błędów, na przykład dzielenia przez zero
zapisywanie historii w bazie SQLite
pobieranie historii obliczeń
czyszczenie historii
Technologie
Backend
Python
FastAPI
Pydantic
SQLite
Frontend
HTML
CSS
JavaScript
Narzędzia
Git
GitHub
Uvicorn
Struktura projektu
fastapi-calculator/
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── .gitignore
├── README.md
├── _kalkulator.py
├── database.py
└── main.py
Uruchomienie projektu
1. Pobranie repozytorium
git clone https://github.com/firo16/fastapi-calculator.git
2. Przejście do folderu projektu
cd fastapi-calculator
3. Utworzenie środowiska wirtualnego
Windows:

python -m venv .venv
.venv\Scripts\activate
4. Instalacja bibliotek
pip install -r requirements.txt
5. Uruchomienie aplikacji
uvicorn main:app --reload
6. Otwarcie aplikacji
W przeglądarce:

http://127.0.0.1:8000
Dokumentacja API:

http://127.0.0.1:8000/docs
Endpointy API
Wykonanie obliczenia
POST /oblicz
Przykładowe dane:

{
  "liczba1": 10,
  "dzialanie": "+",
  "liczba2": 5
}
Przykładowa odpowiedź:

{
  "wynik": 15
}
Pobranie historii
GET /historia
Usunięcie historii
DELETE /historia
Czego nauczyłem się podczas projektu
tworzenia API za pomocą FastAPI
rozróżniania metod GET, POST i DELETE
przesyłania danych w formacie JSON
walidacji danych za pomocą Pydantic
obsługi odpowiedzi i statusów HTTP
komunikacji frontendu z backendem za pomocą fetch()
używania async i await
obsługi zdarzeń w JavaScripcie
wykonywania zapytań SQL
zapisywania danych w bazie SQLite
organizowania kodu w osobnych modułach
używania Git i GitHub
Autor
Projekt wykonany jako pierwszy projekt full-stack do nauki backendu w Pythonie.