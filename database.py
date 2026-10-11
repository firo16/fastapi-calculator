import sqlite3

def utworz_baze():
    polaczenie = sqlite3.connect('calculator.db')
    kursor = polaczenie.cursor()

    kursor.execute("""
    CREATE TABLE IF NOT EXISTS calculations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    liczba1 REAL NOT NULL,
    dzialanie TEXT NOT NULL,
    liczba2 REAL NOT NULL,
    wynik REAL NOT NULL,
    utworzono TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)
    polaczenie.commit()
    polaczenie.close()

def zapisz_obliczenie(liczba1, dzialanie, liczba2, wynik):
    with sqlite3.connect("calculator.db") as polaczenie:
        kursor = polaczenie.cursor()

        kursor.execute("""
        INSERT INTO calculations (
        liczba1,
        dzialanie,
        liczba2,
        wynik
        )
        VALUES (?, ?, ?, ?)
        """, (liczba1, dzialanie, liczba2, wynik))

def pobierz_historie():
    with sqlite3.connect("calculator.db") as polaczenie:
        polaczenie.row_factory = sqlite3.Row

        kursor = polaczenie.cursor()

        kursor.execute("""
            SELECT
                id,
                liczba1,
                dzialanie,
                liczba2,
                wynik,
                utworzono
            FROM calculations
            ORDER BY id DESC
            LIMIT 10
        """)

        rekordy = kursor.fetchall()

        historia = []

        for rekord in rekordy:
            historia.append(dict(rekord))

        return historia

def wyczysc_historie():
    with sqlite3.connect("calculator.db") as polaczenie:
        kursor = polaczenie.cursor()

        kursor.execute("""
            DELETE FROM calculations
        """)


utworz_baze()
pobierz_historie()