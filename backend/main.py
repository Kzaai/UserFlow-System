from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
import json
import os
from passlib.context import CryptContext

#Konfiguracja szyfrowania
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")




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
        #Iniclalizacja jesli nie istnieje 
        with open(DB_PATH, "w", encoding="utf-8") as f:
            json.dump([], f)
        return[]
    
    with open(DB_PATH, "r", encoding="utf-8") as f:
        try:
            dane = json.load(f)
            return dane if isinstance(dane, list) else []
        except json.JSONDecodeError:
            return []
        
            
        

app = FastAPI()




@app.post("/rejestracja")
def register(user: User):
    baza = wczytaj_baze()


    if any(u["login"] == user.login for u in baza):
        raise HTTPException(status_code=400, detail="Użytkownik o podanym loginie już istnieje")
    #Zaczynamy szyforwac moze wyjdzie 
    hashed_password = pwd_context.hash(user.haslo)
    #slownik leci recznie zeby zahaszakokosakoa

    nowy_uzytkownik ={
        "login": user.login,
        "haslo": hashed_password, #Zadziała jak nic
        "firma": user.firma
    }

    baza.append(nowy_uzytkownik)

    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(baza, f , indent=4, ensure_ascii=False)
    return {"status": "success", "message": "Konto zostało zarejestrowane."}


@app.get("/uzytkownicy")
def get_users():
    baza = wczytaj_baze()
    
    # Dodajemy informację o ilości, żeby frontend wiedział co dostał
    return {
        "status": "success",
        "count": len(baza),
        "users": baza 
        }

@app.post("/logowanie")
def logowanie(user: User): # Używamy tego samego modelu User co przy rejestracji
    baza = wczytaj_baze()

    for uzytkownik in baza:
        if uzytkownik["login"] == user.login:
            if pwd_context.verify(user.haslo, uzytkownik["haslo"]):
                return {"status": "success", "message": "Zalogowano pomyslnie.", "user": uzytkownik["login"]}
            
    raise HTTPException(status_code=401, detail="Nieprawidłowe hasło lub login.")


@app.get("/ping")
def ping():
    return {"status": "success"}