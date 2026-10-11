from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

from _kalkulator import obliczanie
from database import (utworz_baze,
                      zapisz_obliczenie,
                      pobierz_historie,
                      wyczysc_historie)
app = FastAPI()




class Obliczenie(BaseModel):
    liczba1: float
    dzialanie: str
    liczba2: float



@app.post('/oblicz')
def oblicz_post(dane: Obliczenie):

    try:
        wynik = obliczanie(dane.liczba1, dane.dzialanie, dane.liczba2)
        zapisz_obliczenie(dane.liczba1, dane.dzialanie, dane.liczba2, wynik)
        return {'wynik': wynik}

    except ZeroDivisionError:
        raise HTTPException(
            status_code=400,
            detail='serio? zero??'
        )
    except ValueError as blad:
        raise HTTPException(
            status_code=400,
            detail=blad
        )

@app.get("/historia")
def historia():
    return pobierz_historie()

@app.delete('/historia')
def usun_historie():
    wyczysc_historie()

    return {
        'message': 'historia zostala wyczysczona'
    }

app.mount(
"/",
StaticFiles(directory="frontend", html=True),
name="frontend"
)


## to start::    uvicorn main:app --reload