import customtkinter as ctk
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class Register(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("UserFlow System v1.0")
        self.geometry("450x550")
        
         #---------Rama Okna -------------
        self.auth_frame = ctk.CTkFrame(self)
        self.dash_frame = ctk.CTkFrame(self)
        self.admin_placeholder = ctk.CTkFrame(self.dash_frame, fg_color="transparent")



        #Robimy Zakładki 

        self.tabview = ctk.CTkTabview(self.auth_frame, width = 400, height = 300)
        self.tabview.pack(padx = 20, pady = 20)
        self.tabview.add("Rejestracja")
        self.tabview.add("Logowanie")
        self.tabview.add("Admin")
       
        
        
       

        #---------Zakładka Rejestracja ---------------

        self.podajlogin = ctk.CTkLabel(self.tabview.tab("Rejestracja"), text = "Podaj login: ")
        self.podajlogin.pack(pady = 10)

        self.login_entry = ctk.CTkEntry(self.tabview.tab("Rejestracja"), width = 200)
        self.login_entry.pack(pady = 10)

        self.podajhaslo = ctk.CTkLabel(self.tabview.tab("Rejestracja"), text = "Podaj hasło: ")
        self.podajhaslo.pack(pady = 10)

        self.haslo_entry = ctk.CTkEntry(self.tabview.tab("Rejestracja"), width = 200)
        self.haslo_entry.pack(pady = 10)

        self.podajfirme = ctk.CTkLabel(self.tabview.tab("Rejestracja"), text = "Podaj nazwę firmy: ")
        self.podajfirme.pack(pady = 10)

        self.firma_entry = ctk.CTkEntry(self.tabview.tab("Rejestracja"), width = 200)
        self.firma_entry.pack(pady = 10)

        self.register_button = ctk.CTkButton(self.tabview.tab("Rejestracja"), text = "Zarejestruj", command = self.zaloz_konto)
        self.register_button.pack(pady = 10)




        #----------Ukyrwamy Admina-------------
        self.tabview.delete("Admin")
        self.admin_tab_active = False

        #-----------Zakładka Logowania------------------
        self.podajlogin = ctk.CTkLabel(self.tabview.tab("Logowanie"), text = "Podaj login: ")
        self.podajlogin.pack(pady = 10)

        self.logowanie_entry = ctk.CTkEntry(self.tabview.tab("Logowanie"), width = 200)
        self.logowanie_entry.pack(pady = 10)

        self.zaloguj_haslo =  ctk.CTkLabel(self.tabview.tab("Logowanie"), text = "Podaj hasło: ")
        self.zaloguj_haslo.pack(pady = 10)

        self.zaloguj_haslo_entry = ctk.CTkEntry(self.tabview.tab("Logowanie"), width = 200)
        self.zaloguj_haslo_entry.pack(pady = 10)

        self.zaloguj_button = ctk.CTkButton(self.tabview.tab("Logowanie"), text = "Zaloguj", command = self.zaloguj)
        self.zaloguj_button.pack(pady = 10)
        
        #Dajemy Drugą rame
        self.welcome_label = ctk.CTkLabel(self.dash_frame, text = "Witamy w UserFlow System v1.0", font = ("Arial", 20))
        self.welcome_label.pack(pady = 20)

        self.logout_button = ctk.CTkButton(self.dash_frame, text = "Wyloguj", command = self.wyloguj)
        self.logout_button.pack(pady = 10)


        # Pakuje tylko logowanie

        self.auth_frame.pack(fill="both", expand=True  )

        
        self.status_dot = ctk.CTkLabel(self, text="●", text_color="grey", font=("Arial", 20))
        self.status_dot.pack(pady=10) # pack() doda to na samym dole pod tabview

        # 2. NA SAMYM KOŃCU URUCHAMIAMY STATUS
        self.check_api_status()
    

    #musi byc wyloguj 
    def wyloguj(self):
        self.admin_placeholder.pack_forget()
        self.dash_frame.pack_forget() 
        self.auth_frame.pack(fill="both", expand=True)

    def pobierz_uzytkowników(self):
        url = "http://127.0.0.1:8000/uzytkownicy"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                odpowidz_z_serwera = response.json()

                #Wyciagamy userds
                lista_uzytkownikow = odpowidz_z_serwera["users"]
                self.textbox.configure(state = "normal")
                self.textbox.delete("1.0", "end")

                #Petla idzie po liscie slownikow
                for user in lista_uzytkownikow:
                    tekst = f"Login: {user['login']}, Firma: {user['firma']}\n"
                    self.textbox.insert("end", tekst)   

                self.textbox.configure(state = "disabled")

                print(f"Pobrano {len(lista_uzytkownikow)} uzytkowników.")
                

            else:
                print("Serwer odrzucił prośbę. Kod:{response.status_code}")
        except requests.exceptions.ConnectionError:
            print("Brak połączenia z serwerem.")
        
    def zaloz_konto(self):
        login = self.login_entry.get()
        haslo = self.haslo_entry.get()
        firma = self.firma_entry.get()

        url = "http://127.0.0.1:8000/rejestracja"
        data = {"login": login, "haslo": haslo, "firma": firma}
        try:
            response = requests.post(url, json=data, timeout=5)
            if response.status_code == 200:
                print("Konto zostało zarejestrowane.")

                self.login_entry.delete("0", "end")
                self.haslo_entry.delete("0", "end")
                self.firma_entry.delete("0", "end")
            else:
                print("Serwer odrzucił paczke. Kod:{response.status_code}")
        except requests.exceptions.ConnectionError:
            print("Brak połączenia z serwerem.")
    def zaloguj(self):
        login = self.logowanie_entry.get()
        haslo = self.zaloguj_haslo_entry.get()
        
        url = "http://127.0.0.1:8000/logowanie"
        data = {"login": login, "haslo": haslo, "firma": ""} # Firma może być pusta przy logowaniu

        try:
            response = requests.post(url, json=data, timeout=5)
            
            if response.status_code == 200:
                print("Zalogowano pomyslnie.")

                #Pokazujemy po sukcisie
                self.auth_frame.pack_forget() #Znika logowanie
                self.dash_frame.pack(fill="both", expand=True) #Pojawia się dashboard
                self.welcome_label.configure(text = f"Witamy w UserFlow System v1.0, {login}!")
                #Sprawdany czy to admin
                if login.lower() =="admin":
                    self.admin_placeholder.pack(pady=20, fill="x")
                    self.stworz_panel_admina()

                
                    
                else:
                    self.admin_placeholder.pack_forget()
                 
            elif response.status_code == 401:
                print("Błąd: Niepoprawne dane logowania.")
            else:
                print(f"Błąd serwera: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print("Brak połączenia z serwerem.")


    def stworz_panel_admina(self):
        #-----------Panel Admina------------------
        for widget in self.admin_placeholder.winfo_children():
            widget.destroy()

        #dodajemy elemnty to panelu
        lab = ctk.CTkLabel(self.admin_placeholder, text = "Panel Admina", font = ("Arial", 20))
        lab.pack(pady = 10)
        
        self.textbox = ctk.CTkTextbox(self.admin_placeholder, width = 400, height = 150)
        self.textbox.pack(pady = 10)

        self.pobierz_uzytkowników_button = ctk.CTkButton(self.admin_placeholder, text = "Pobierz uzytkowników", command = self.pobierz_uzytkowników)
        self.pobierz_uzytkowników_button.pack(pady = 10)


    def check_api_status(self):
        url = "http://127.0.0.1:8000/ping"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                self.status_dot.configure(text = "●", text_color = "green")
            else:
                self.status_dot.configure(text = "●", text_color = "red")
        except requests.exceptions.ConnectionError:
            self.status_dot.configure(text = "●", text_color = "red")
        self.after(5000, self.check_api_status)
            


if __name__ == "__main__":
    app = Register()
    app.mainloop()