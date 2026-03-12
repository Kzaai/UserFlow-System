from fastapi import FastAPI
from pydantic import BaseModel
import json
import os




# 1. NAJPIERW definicja "Koperty" (Modelu)
class User(BaseModel):
    login: str
    haslo: str
    firma: str

# 1. Ścieżka do bazy (pamiętasz: os.path.join dla bezpieczeństwa)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "uzytkownicy.json")

# 2. Funkcja pomocnicza
def wczytaj_baze():
    if not os.path.exists(DB_PATH):
        return [] # Zwracamy listę, bo będziemy trzymać wielu użytkowników
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

app = FastAPI()




@app.post("/rejestracja")
def register(user: User):
    baza = wczytaj_baze()

    #Zamieniamy usera na słownik

    nowy_uzytkownik = user.dict()

    baza.append(nowy_uzytkownik) #Dodajemy do listy

    #Zapisujemy do pliku 

    with open(DB_PATH,"w", encoding="utf-8") as f:
        json.dump(baza, f , indent=4, ensure_ascii=False)

@app.get("/uzytkownicy")
def get_users():
    baza = wczytaj_baze()
    
    # Dodajemy informację o ilości, żeby frontend wiedział co dostał
    return {
        "status": "success",
        "count": len(baza),
        "users": baza 
        }