from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserRegistration(BaseModel):
    login: str
    haslo: str
    firma: str

@app.post("/rejestracja")
def register(user: UserRegistration):
    # Logika: Tutaj serwer "łapie" paczkę z frontendu
    print(f"Próba rejestracji: {user.login} z firmy {user.firma}")
    return {"status": "Sukces", "wiadomosc": f"Witaj {user.login} w systemie!"}
