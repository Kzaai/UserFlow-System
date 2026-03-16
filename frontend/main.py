import customtkinter as ctk
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")






class Dashboard(ctk.CTkFrame):
    def __init__(self, master, title , **kwargs):
        #Kolor tło obramowanie
        super().__init__(master, fg_color="#2b2b2b", corner_radius=15, border_width=1,
        border_color="#3d3d3d", **kwargs)
    #Ustawmy kolumne z indksem 0 zeby wypelmnialo caly ekrans
        self.grid_columnconfigure(0, weight=1)


        #Umieszczamy to w pierwszym rzedzie 
        self.label_title = ctk.CTkLabel(self, text = title.upper() , font = ("Arial", 12))
        self.label_title.grid(row = 0, column = 0, pady=(10, 0))

        #Głowna zawartośc
        self.label_content = ctk.CTkLabel(self, text = "--", font = ("Arial", 32))
        self.label_content.grid(row = 1, column = 0, pady=(15, 5))

        #Stopka
        self.label_footer = ctk.CTkLabel(self, text = "Ładowanie...", font = ("Arial", 11))
        self.label_footer.grid(row = 2, column = 0, pady=(5, 15))

    def aktualizuj_dane(self, wartosc ,opis , kolor= "#ffffff"):
        self.label_content.configure (text=wartosc, text_color=kolor)
        self.label_footer.configure(text=opis)

    def ustaw_pogode(self,temp,miasto):
        self.label_content.configure (text=f"{temp}°C", text_color="#2ecc71")
        self.label_footer.configure(text=f"Lokalizacja : {miasto}")


        



class Register(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("UserFlow System v1.0")
        self.geometry("450x550")
        

        #----------------Powitanie uzytkownika/Ekran Startowy--------

        self.start_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.start_label = ctk.CTkLabel(self.start_frame, text = "Witamy w UserFlow System v1.0", font = ("Arial", 20))
        self.start_label.pack(pady = 20)


        #Przycisk do logowania 

        
        self.go_to_login_btn = ctk.CTkButton(self.start_frame, text="Zaloguj", width=200 ,height=50, command=lambda: self.show_frame(self.auth_frame, tab="Logowanie"))
        self.go_to_login_btn.pack(pady = 20)
        #Teraz rejestracja
        self.go_to_register_button = ctk.CTkButton(self.start_frame, text="Zarejestuj się ", width=200 ,height=50, command=lambda: self.show_frame(self.auth_frame, tab="Rejestracja"))
        self.go_to_register_button.pack(pady = 20)  
        
        
         #---------Rama Okna -------------
        self.auth_frame = ctk.CTkFrame(self)
        self.dash_frame = ctk.CTkFrame(self)
        self.user_frame = ctk.CTkFrame(self)
        self.admin_placeholder = ctk.CTkFrame(self.dash_frame, fg_color="transparent")
        self.user_placeholder = ctk.CTkFrame(self.dash_frame, fg_color="transparent")



        #Robimy Zakładki 

        self.tabview = ctk.CTkTabview(self.auth_frame, width = 400, height = 300)
        self.tabview.pack(padx = 20, pady = 20)
        self.tabview.add("Rejestracja")
        self.tabview.add("Logowanie")
        self.tabview.add("Admin")

        #Przycisk wstecz
        self.back_button = ctk.CTkButton(self.auth_frame, text = "Wstecz", command=lambda: self.show_frame(self.start_frame))
        self.back_button.pack(pady = 10)
       
        
        
       

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

        #--------Panel Uzytkownika-------------
        self.dash_frame = ctk.CTkFrame(self)
        

        #Napis powitalny 
        self.welcome_label = ctk.CTkLabel(self.dash_frame, text = "UserFlow System 1.0" , font = ("Arial", 20))
        self.welcome_label.pack(pady = 10)

        #Kontenery
        self.admin_placeholder = ctk.CTkFrame(self.dash_frame, fg_color="transparent")
        self.user_placeholder = ctk.CTkFrame(self.dash_frame, fg_color="transparent")

        #Jeden przycisk wyloguje ,a nie 100

        self.logout_button = ctk.CTkButton(self.dash_frame, text = "Wyloguj", command = self.wyloguj)
        self.logout_button.pack(pady = 10)

        #Moze przetani  sięnakładać 
        self.admin_placeholder.pack(side ="top", fill="both", expand = True )
        self.user_placeholder.pack(side = "top", fill="both", expand = True )

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
        
        


        # Pakuje tylko logowanie

        self.auth_frame.pack(fill="both", expand=True  )

        
        self.status_dot = ctk.CTkLabel(self, text="●", text_color="grey", font=("Arial", 20))
        self.status_dot.pack(pady=10) # pack() doda to na samym dole pod tabview

        # 2. NA SAMYM KOŃCU URUCHAMIAMY  I startujemy
        self.show_frame(self.start_frame)
        self.check_api_status()
    def show_frame(self, frame_to_show, tab=None):
        #Ukyrwamy całość
        self.start_frame.pack_forget()
        self.auth_frame.pack_forget()
        self.dash_frame.pack_forget()


        frame_to_show.pack(fill="both", expand=True)

        if tab :
            self.tabview.set(tab)

        if tab is not None and frame_to_show == self.auth_frame:
            try:
                self.tabview.set(tab)
            except Exception as e:
                print(f"Bład ustawinia zakłądki: {e} ")


    #musi byc wyloguj 
    def wyloguj(self):
        self.admin_placeholder.pack_forget()
        self.user_placeholder.pack_forget()

        #Czyszcz placeholder
        for widget in self.admin_placeholder.winfo_children():
            widget.destroy()
        for widget in self.user_placeholder.winfo_children():
            widget.destroy()

        #znowu logowanie
        self.dash_frame.pack_forget()
        self.show_frame(self.auth_frame, tab="Logowanie")


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
                self.show_frame(self.dash_frame)
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
                    self.user_placeholder.pack(pady = 20, fill="x")
                    self.stworz_panel_uzytkownika(login)
                 
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

    def stworz_panel_uzytkownika(self, login):
        for widget in self.user_placeholder.winfo_children():
            widget.destroy()

        #Tworzymt główną siatke

        container = ctk.CTkFrame(self.user_placeholder, fg_color="transparent")
        container.pack(fill= "both", expand=True, padx=20, pady=20)

        #definiujemy kolumny

        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)

        #Wstawiamy kafle z klasy która zrobiłem wyżej
        self.title_weather = Dashboard(container, title = "Pogoda")
        self.title_weather.grid(row = 0, column = 0, padx=10, pady=10, sticky="nsew")

        #Giełda

        self.title_stock = Dashboard(container, title="Giełda")
        self.title_stock.grid(row = 0, column = 1, padx=10, pady=10, sticky="nsew")


        #Pobieramy dane z pogody

        self.pobierz_pogode()
        #Pobieramy dane z giełdy

        self.pobierz_bitcoin()

    def pobierz_pogode(self):
        api_key = "557602d9a5272d4aecae0e56205dc0c0"
        miasto = "Szczecin"

        url = f"http://api.openweathermap.org/data/2.5/weather?q={miasto}&appid={api_key}&units=metric"
        try:
            
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                
                dane = r.json()
                temperatura = dane["main"]["temp"]
                self.title_weather.ustaw_pogode(round(temperatura), miasto)
            else:
                print(f"Błąd serwera: {r.status_code}")
                print(f"Informacja od serwera: {r.text}")

        except:
            print("Brak połączenia z serwerem.{e}")

        
    def pobierz_bitcoin(self):
       
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                dane = r.json()
                cena = r.json()["bitcoin"]["usd"]
                #Modta universalna moze zadziała

                self.title_stock.aktualizuj_dane(f"${cena:,}", "Kurs: BITCOIN (USD)" , "#f39c12")
                print(f"Kurs bitcoina: {cena}")
            else:
                print(f"Błąd serwera: {r.status_code}")
                print(f"Informacja od serwera: {r.text}")

        except:
            print("Brak połączenia z serwerem.{e}")

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