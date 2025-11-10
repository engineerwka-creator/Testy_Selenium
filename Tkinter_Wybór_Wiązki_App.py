# # import tkinter as tk
# # from tkinter import ttk, messagebox
# #
# # # ====================================================================
# # # I. PEŁNE MAPOWANIA DANYCH
# # # (Pobrane z Twojego ostatniego kodu konsolowego)
# # # ====================================================================
# #
# # # A. Orientacja Złącza (O1, O2) - Opcje do RĘCZNEGO wyboru
# # MAPOWANIE_ORIENTACJI_DO_WYBORU = {
# #     '85': 'Proste (Straight)',
# #     '84': 'Kątowe (Angled)',
# # }
# #
# # # B. Typ Kabla (K) - Kody 2-cyfrowe
# # MAPOWANIE_KABLA = {
# #     '00': 'Brak Kabla',
# #     '05': 'RG58',
# #     '06': 'RG174',
# #     '07': 'H155'
# # }
# #
# # # C1. Typ Złącza 1 (T1)
# # MAPOWANIE_ZLACZY_T1 = {
# #     '000': 'Brak Złącza',
# #     '100': 'FAKRA Cod. E (F)', '101': 'FAKRA Cod. E (M)', '102': 'FME (F)', '103': 'FME (M)',
# #     '104': 'BNC (F)', '105': 'BNC (M)', '106': 'SMA (F)', '107': 'SMA (M)',
# #     '108': 'R-SMA (F)', '109': 'R-SMA (M)', '110': 'SMB (F)', '111': 'SMB (M)',
# #     '112': 'UHF (F)', '113': 'UHF (M)', '114': 'mini UHF (F)', '115': 'mini UHF (M)',
# #     '116': 'FAKRA Cod. A (F)', '117': 'FAKRA Cod. A (M)', '118': 'FAKRA Cod. B (F)', '119': 'FAKRA Cod. B (M)',
# #     '120': 'FAKRA Cod. C (F)', '121': 'FAKRA Cod. C (M)', '122': 'FAKRA Cod. D (F)', '123': 'FAKRA Cod. D (M)',
# #     '124': 'FAKRA Cod. M (F)', '125': 'FAKRA Cod. M (M)', '126': 'FAKRA Cod. N (F)', '127': 'FAKRA Cod. N (M)',
# #     '128': 'FAKRA Cod. Z (F)', '129': 'FAKRA Cod. Z (M)', '130': 'M10 (F)', '131': 'M10 (M)',
# #     '132': 'FAKRA Cod. F (F)', '133': 'FAKRA Cod. F (M)', '134': 'FAKRA Cod. G (F)', '135': 'FAKRA Cod. G (M)',
# #     '136': 'FAKRA Cod. H (F)', '137': 'FAKRA Cod. H (M)', '138': 'FAKRA Cod. I (F)', '139': 'FAKRA Cod. I (M)',
# #     '140': 'FAKRA Cod. K (F)', '141': 'FAKRA Cod. K (M)', '142': 'FAKRA Cod. L (F)', '143': 'FAKRA Cod. L (M)',
# # }
# #
# # # C2. Typ Złącza 2 (T2)
# # MAPOWANIE_ZLACZY_T2 = {
# #     '000': 'Brak Złącza',
# #     '500': 'FAKRA Cod. M (F)', '501': 'FAKRA Cod. M (M)', '502': 'FAKRA Cod. N (F)', '503': 'FAKRA Cod. N (M)',
# #     '504': 'FAKRA Cod. Z (F)', '505': 'FAKRA Cod. Z (M)', '506': 'M10 (F)', '507': 'M10 (M)',
# #     '508': 'FAKRA Cod. F (F)', '509': 'FAKRA Cod. F (M)', '510': 'FAKRA Cod. G (F)', '511': 'FAKRA Cod. G (M)',
# #     '512': 'FAKRA Cod. H (F)', '513': 'FAKRA Cod. H (M)', '514': 'FAKRA Cod. I (F)', '515': 'FAKRA Cod. I (M)',
# #     '516': 'FAKRA Cod. K (F)', '517': 'FAKRA Cod. K (M)', '518': 'FAKRA Cod. L (F)', '519': 'FAKRA Cod. L (M)',
# #     '520': 'mini UHF (F)', '521': 'mini UHF (M)', '522': 'FAKRA Cod. A (F)', '523': 'FAKRA Cod. A (M)',
# #     '524': 'FAKRA Cod. B (F)', '525': 'FAKRA Cod. B (M)', '526': 'FAKRA Cod. C (F)', '527': 'FAKRA Cod. C (M)',
# #     '528': 'FAKRA Cod. D (F)', '529': 'FAKRA Cod. D (M)', '530': 'FAKRA Cod. E (F)', '531': 'FAKRA Cod. E (M)',
# #     '532': 'FME (F)', '533': 'FME (M)', '534': 'BNC (F)', '535': 'BNC (M)',
# #     '536': 'SMA (F)', '537': 'SMA (M)', '538': 'R-SMA (F)', '539': 'R-SMA (M)',
# #     '540': 'SMB (F)', '541': 'SMB (M)', '542': 'UHF (F)', '543': 'UHF (M)',
# # }
# #
# # # D. Długość Kabla (D)
# # MAPOWANIE_DLUGOSCI = {
# #     '030': '3.0 m', '035': '3.5 m', '040': '4.0 m', '045': '4.5 m',
# #     '050': '5.0 m', '055': '5.5 m', '060': '6.0 m', '065': '6.5 m',
# #     '070': '7.0 m', '075': '7.5 m', '080': '8.0 m', '085': '8.5 m',
# #     '090': '9.0 m', '095': '9.5 m', '100': '10.0 m', '105': '10.5 m',
# #     '110': '11.0 m'
# # }
# #
# #
# # # ====================================================================
# # # II. KLASA GENERATORA Z LOGIKĄ TKINTER
# # # ====================================================================
# #
# # class GeneratorKabliApp:
# #     def __init__(self, master):
# #         self.master = master
# #         master.title("Generator Numerów Katalogowych Kabli")
# #
# #         # Słownik do przechowywania aktywnych mapowań dla łatwego dostępu
# #         self.mapy = {
# #             'T1': MAPOWANIE_ZLACZY_T1,
# #             'T2': MAPOWANIE_ZLACZY_T2,
# #             'O': MAPOWANIE_ORIENTACJI_DO_WYBORU,
# #             'K': MAPOWANIE_KABLA,
# #             'D': MAPOWANIE_DLUGOSCI
# #         }
# #
# #         # Inicjalizacja zmiennych Tkinter
# #         self.kod_t1 = tk.StringVar(master);
# #         self.kod_o1 = tk.StringVar(master)
# #         self.kod_t2 = tk.StringVar(master);
# #         self.kod_o2 = tk.StringVar(master)
# #         self.kod_k = tk.StringVar(master);
# #         self.kod_d = tk.StringVar(master)
# #
# #         self.utworz_interfejs()
# #         self.przypisz_domyslne_wartosci()
# #
# #         # Ustawienie powiązań (binding) do uruchamiania logiki sprawdzającej
# #         self.pole_t1.bind("<<ComboboxSelected>>", lambda event: self.sprawdz_orientacje('T1'))
# #         self.pole_t2.bind("<<ComboboxSelected>>", lambda event: self.sprawdz_orientacje('T2'))
# #         self.pole_k.bind("<<ComboboxSelected>>", lambda event: self.sprawdz_kabel())
# #
# #         # Wywołanie wstępne, aby ustawić stan pól D i O (jeśli domyślne to 000/00)
# #         self.sprawdz_orientacje('T1')
# #         self.sprawdz_orientacje('T2')
# #         self.sprawdz_kabel()
# #
# #     def utworz_interfejs(self):
# #         # Użycie ramki dla lepszego zarządzenia układem i odstępami
# #         frame = ttk.Frame(self.master, padding="10")
# #         frame.grid(row=0, column=0, sticky="nsew")
# #
# #         # --- Sekcja 1: Złącze T1 i Orientacja O1 ---
# #         ttk.Label(frame, text="1. Typ Złącza T1:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
# #         self.pole_t1 = ttk.Combobox(frame, textvariable=self.kod_t1, values=list(self.mapy['T1'].keys()),
# #                                     state='readonly', width=5)
# #         self.pole_t1.grid(row=0, column=1, padx=5, pady=5, sticky='w')
# #         ttk.Label(frame, text=" | ").grid(row=0, column=2, sticky='w')
# #         self.label_nazwa_t1 = ttk.Label(frame, text="", width=30)
# #         self.label_nazwa_t1.grid(row=0, column=3, sticky='w')
# #         self.pole_t1.bind("<<ComboboxSelected>>",
# #                           lambda event: self.aktualizuj_nazwe(self.kod_t1.get(), self.mapy['T1'], self.label_nazwa_t1))
# #
# #         self.label_o1 = ttk.Label(frame, text="3. Orientacja O1:")
# #         self.label_o1.grid(row=1, column=0, padx=5, pady=5, sticky='w')
# #         self.pole_o1 = ttk.Combobox(frame, textvariable=self.kod_o1, values=list(self.mapy['O'].keys()),
# #                                     state='readonly', width=5)
# #         self.pole_o1.grid(row=1, column=1, padx=5, pady=5, sticky='w')
# #         self.pole_o1.bind("<<ComboboxSelected>>",
# #                           lambda event: self.aktualizuj_nazwe(self.kod_o1.get(), self.mapy['O'], self.label_nazwa_o1))
# #         ttk.Label(frame, text=" | ").grid(row=1, column=2, sticky='w')
# #         self.label_nazwa_o1 = ttk.Label(frame, text="", width=30)
# #         self.label_nazwa_o1.grid(row=1, column=3, sticky='w')
# #
# #         ttk.Separator(frame, orient='horizontal').grid(row=2, columnspan=4, sticky="ew", pady=5)
# #
# #         # --- Sekcja 2: Złącze T2 i Orientacja O2 ---
# #         ttk.Label(frame, text="2. Typ Złącza T2:").grid(row=3, column=0, padx=5, pady=5, sticky='w')
# #         self.pole_t2 = ttk.Combobox(frame, textvariable=self.kod_t2, values=list(self.mapy['T2'].keys()),
# #                                     state='readonly', width=5)
# #         self.pole_t2.grid(row=3, column=1, padx=5, pady=5, sticky='w')
# #         self.pole_t2.bind("<<ComboboxSelected>>",
# #                           lambda event: self.aktualizuj_nazwe(self.kod_t2.get(), self.mapy['T2'], self.label_nazwa_t2))
# #         ttk.Label(frame, text=" | ").grid(row=3, column=2, sticky='w')
# #         self.label_nazwa_t2 = ttk.Label(frame, text="", width=30)
# #         self.label_nazwa_t2.grid(row=3, column=3, sticky='w')
# #
# #         self.label_o2 = ttk.Label(frame, text="4. Orientacja O2:")
# #         self.label_o2.grid(row=4, column=0, padx=5, pady=5, sticky='w')
# #         self.pole_o2 = ttk.Combobox(frame, textvariable=self.kod_o2, values=list(self.mapy['O'].keys()),
# #                                     state='readonly', width=5)
# #         self.pole_o2.grid(row=4, column=1, padx=5, pady=5, sticky='w')
# #         self.pole_o2.bind("<<ComboboxSelected>>",
# #                           lambda event: self.aktualizuj_nazwe(self.kod_o2.get(), self.mapy['O'], self.label_nazwa_o2))
# #         ttk.Label(frame, text=" | ").grid(row=4, column=2, sticky='w')
# #         self.label_nazwa_o2 = ttk.Label(frame, text="", width=30)
# #         self.label_nazwa_o2.grid(row=4, column=3, sticky='w')
# #
# #         ttk.Separator(frame, orient='horizontal').grid(row=5, columnspan=4, sticky="ew", pady=5)
# #
# #         # --- Sekcja 3: Kabel K i Długość D ---
# #         ttk.Label(frame, text="5. Typ Kabla K:").grid(row=6, column=0, padx=5, pady=5, sticky='w')
# #         self.pole_k = ttk.Combobox(frame, textvariable=self.kod_k, values=list(self.mapy['K'].keys()), state='readonly',
# #                                    width=5)
# #         self.pole_k.grid(row=6, column=1, padx=5, pady=5, sticky='w')
# #         self.pole_k.bind("<<ComboboxSelected>>",
# #                          lambda event: self.aktualizuj_nazwe(self.kod_k.get(), self.mapy['K'], self.label_nazwa_k))
# #         ttk.Label(frame, text=" | ").grid(row=6, column=2, sticky='w')
# #         self.label_nazwa_k = ttk.Label(frame, text="", width=30)
# #         self.label_nazwa_k.grid(row=6, column=3, sticky='w')
# #
# #         self.label_d = ttk.Label(frame, text="6. Długość Kabla D:")
# #         self.label_d.grid(row=7, column=0, padx=5, pady=5, sticky='w')
# #         self.pole_d = ttk.Combobox(frame, textvariable=self.kod_d, values=list(self.mapy['D'].keys()), state='readonly',
# #                                    width=5)
# #         self.pole_d.grid(row=7, column=1, padx=5, pady=5, sticky='w')
# #         self.pole_d.bind("<<ComboboxSelected>>",
# #                          lambda event: self.aktualizuj_nazwe(self.kod_d.get(), self.mapy['D'], self.label_nazwa_d))
# #         ttk.Label(frame, text=" | ").grid(row=7, column=2, sticky='w')
# #         self.label_nazwa_d = ttk.Label(frame, text="", width=30)
# #         self.label_nazwa_d.grid(row=7, column=3, sticky='w')
# #
# #         ttk.Separator(frame, orient='horizontal').grid(row=8, columnspan=4, sticky="ew", pady=5)
# #
# #         # --- Sekcja Wyniku ---
# #         ttk.Button(frame, text="Generuj Numer Katalogowy", command=self.generuj_numer_katalogowy).grid(row=9, column=0,
# #                                                                                                        columnspan=4,
# #                                                                                                        pady=10)
# #
# #         ttk.Label(frame, text="ZBUDOWANY NUMER:").grid(row=10, column=0, sticky='w')
# #         self.wynik_label = ttk.Label(frame, text="---", font=("Arial", 14, "bold"), foreground="navy")
# #         self.wynik_label.grid(row=10, column=1, columnspan=3, sticky='w')
# #
# #     def aktualizuj_nazwe(self, kod, mapa, etykieta):
# #         """Aktualizuje etykietę nazwy obok Comboboxa."""
# #         nazwa = mapa.get(kod, "Wybierz...")
# #         etykieta.config(text=nazwa)
# #
# #     def przypisz_domyslne_wartosci(self):
# #         """Ustawia domyślne wybrane wartości (pierwsze z listy) i aktualizuje nazwy."""
# #
# #         def set_and_update(var, mapa, etykieta):
# #             pierwszy_klucz = list(mapa.keys())[0]
# #             var.set(pierwszy_klucz)
# #             self.aktualizuj_nazwe(pierwszy_klucz, mapa, etykieta)
# #
# #         set_and_update(self.kod_t1, self.mapy['T1'], self.label_nazwa_t1)
# #         set_and_update(self.kod_o1, self.mapy['O'], self.label_nazwa_o1)
# #         set_and_update(self.kod_t2, self.mapy['T2'], self.label_nazwa_t2)
# #         set_and_update(self.kod_o2, self.mapy['O'], self.label_nazwa_o2)
# #         set_and_update(self.kod_k, self.mapy['K'], self.label_nazwa_k)
# #         set_and_update(self.kod_d, self.mapy['D'], self.label_nazwa_d)
# #
# #     def sprawdz_orientacje(self, zlacze_num):
# #         """Logika blokowania O1/O2, jeśli T1/T2 to '000'."""
# #         if zlacze_num == 'T1':
# #             kod_zlacza = self.kod_t1.get()
# #             pole_orientacji = self.pole_o1
# #             kod_orientacji = self.kod_o1
# #         else:  # T2
# #             kod_zlacza = self.kod_t2.get()
# #             pole_orientacji = self.pole_o2
# #             kod_orientacji = self.kod_o2
# #
# #         if kod_zlacza == '000':
# #             pole_orientacji.config(state='disabled')
# #             # Usuń wartość z Comboboxa, ale nie ruszaj StringVar (StringVara nie dodamy do numeru)
# #             pole_orientacji.set("")
# #         else:
# #             pole_orientacji.config(state='readonly')
# #             # Ustaw domyślną wartość, jeśli jest pusta
# #             if not kod_orientacji.get() in self.mapy['O']:
# #                 kod_orientacji.set(list(self.mapy['O'].keys())[0])
# #             self.aktualizuj_nazwe(kod_orientacji.get(), self.mapy['O'],
# #                                   self.label_nazwa_o1 if zlacze_num == 'T1' else self.label_nazwa_o2)
# #
# #     def sprawdz_kabel(self):
# #         """Logika blokowania D, jeśli K to '00'."""
# #         kod_kabla = self.kod_k.get()
# #
# #         if kod_kabla == '00':
# #             self.pole_d.config(state='disabled')
# #             self.pole_d.set("")  # Usuń wartość z Comboboxa
# #         else:
# #             self.pole_d.config(state='readonly')
# #             # Ustaw domyślną wartość, jeśli jest pusta
# #             if not self.kod_d.get() in self.mapy['D']:
# #                 self.kod_d.set(list(self.mapy['D'].keys())[0])
# #             self.aktualizuj_nazwe(self.kod_d.get(), self.mapy['D'], self.label_nazwa_d)
# #
# #     def generuj_numer_katalogowy(self):
# #         """
# #         Główna logika generowania numeru na podstawie wartości z GUI.
# #         Implementuje zasady: T jest zawsze, O pomijane gdy T=000. K i D pomijane gdy K=00.
# #         """
# #
# #         T1 = self.kod_t1.get()
# #         T2 = self.kod_t2.get()
# #         K = self.kod_k.get()
# #
# #         # Weryfikacja, czy wszystkie wymagane pola są wybrane
# #         if T1 not in self.mapy['T1'] or T2 not in self.mapy['T2'] or K not in self.mapy['K']:
# #             messagebox.showerror("Błąd", "Wybierz prawidłowe kody dla wszystkich obowiązkowych pól (T1, T2, K).")
# #             return
# #
# #         segmenty = []
# #
# #         # 1. T1 (3c) i O1 (2c)
# #         segmenty.append(T1)
# #         if T1 != '000':
# #             O1 = self.kod_o1.get()
# #             if O1 not in self.mapy['O']:
# #                 messagebox.showerror("Błąd", "Wymagana orientacja O1.")
# #                 return
# #             segmenty.append(O1)
# #
# #         # 2. T2 (3c) i O2 (2c)
# #         segmenty.append(T2)
# #         if T2 != '000':
# #             O2 = self.kod_o2.get()
# #             if O2 not in self.mapy['O']:
# #                 messagebox.showerror("Błąd", "Wymagana orientacja O2.")
# #                 return
# #             segmenty.append(O2)
# #
# #         # 3. K (2c) i D (3c)
# #         if K != '00':
# #             segmenty.append(K)
# #             D = self.kod_d.get()
# #             if D not in self.mapy['D']:
# #                 messagebox.showerror("Błąd", "Wymagana jest długość kabla D.")
# #                 return
# #             segmenty.append(D)
# #
# #         numer_katalogowy = "".join(segmenty)
# #         dlugosc_numeru = len(numer_katalogowy)
# #
# #         # Wyświetlenie wyniku
# #         self.wynik_label.config(text=f"{numer_katalogowy} ({dlugosc_numeru} cyfr)")
# #         messagebox.showinfo("Numer Wygenerowany",
# #                             f"Numer Katalogowy: {numer_katalogowy}\nDługość: {dlugosc_numeru} cyfr")
# #
# #
# # # ====================================================================
# # # III. URUCHOMIENIE APLIKACJI
# # # ====================================================================
# #
# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     app = GeneratorKabliApp(root)
# #     # Konfiguracja kolumn, aby były skalowalne (opcjonalne, dla lepszego wyglądu)
# #     root.columnconfigure(0, weight=1)
# #     root.rowconfigure(0, weight=1)
# #     root.mainloop()
#
# #-----------------------------------------------------------------------------------------------------------------------
#
# # import tkinter as tk
# # from tkinter import ttk, messagebox
# #
# # # ====================================================================
# # # I. PEŁNE MAPOWANIA DANYCH
# # # ====================================================================
# #
# # MAPOWANIE_ORIENTACJI_DO_WYBORU = {
# #     '85': 'Proste (Straight)', '84': 'Kątowe (Angled)',
# # }
# # MAPOWANIE_KABLA = {
# #     '00': 'Brak Kabla', '05': 'RG58', '06': 'RG174', '07': 'H155'
# # }
# # MAPOWANIE_ZLACZY_T1 = {
# #     '000': 'Brak Złącza', '100': 'FAKRA Cod. E (F)', '101': 'FAKRA Cod. E (M)',
# #     '102': 'FME (F)', '103': 'FME (M)', '104': 'BNC (F)', '105': 'BNC (M)',
# #     '106': 'SMA (F)', '107': 'SMA (M)', '108': 'R-SMA (F)', '109': 'R-SMA (M)',
# #     '110': 'SMB (F)', '111': 'SMB (M)', '112': 'UHF (F)', '113': 'UHF (M)',
# #     '114': 'mini UHF (F)', '115': 'mini UHF (M)', '116': 'FAKRA Cod. A (F)',
# #     '117': 'FAKRA Cod. A (M)', '118': 'FAKRA Cod. B (F)', '119': 'FAKRA Cod. B (M)',
# #     '120': 'FAKRA Cod. C (F)', '121': 'FAKRA Cod. C (M)', '122': 'FAKRA Cod. D (F)',
# #     '123': 'FAKRA Cod. D (M)', '124': 'FAKRA Cod. M (F)', '125': 'FAKRA Cod. M (M)',
# #     '126': 'FAKRA Cod. N (F)', '127': 'FAKRA Cod. N (M)', '128': 'FAKRA Cod. Z (F)',
# #     '129': 'FAKRA Cod. Z (M)', '130': 'M10 (F)', '131': 'M10 (M)', '132': 'FAKRA Cod. F (F)',
# #     '133': 'FAKRA Cod. F (M)', '134': 'FAKRA Cod. G (F)', '135': 'FAKRA Cod. G (M)',
# #     '136': 'FAKRA Cod. H (F)', '137': 'FAKRA Cod. H (M)', '138': 'FAKRA Cod. I (F)',
# #     '139': 'FAKRA Cod. I (M)', '140': 'FAKRA Cod. K (F)', '141': 'FAKRA Cod. K (M)',
# #     '142': 'FAKRA Cod. L (F)', '143': 'FAKRA Cod. L (M)',
# # }
# # MAPOWANIE_ZLACZY_T2 = {
# #     '000': 'Brak Złącza', '500': 'FAKRA Cod. M (F)', '501': 'FAKRA Cod. M (M)',
# #     '502': 'FAKRA Cod. N (F)', '503': 'FAKRA Cod. N (M)', '504': 'FAKRA Cod. Z (F)',
# #     '505': 'FAKRA Cod. Z (M)', '506': 'M10 (F)', '507': 'M10 (M)', '508': 'FAKRA Cod. F (F)',
# #     '509': 'FAKRA Cod. F (M)', '510': 'FAKRA Cod. G (F)', '511': 'FAKRA Cod. G (M)',
# #     '512': 'FAKRA Cod. H (F)', '513': 'FAKRA Cod. H (M)', '514': 'FAKRA Cod. I (F)',
# #     '515': 'FAKRA Cod. I (M)', '516': 'FAKRA Cod. K (F)', '517': 'FAKRA Cod. K (M)',
# #     '518': 'FAKRA Cod. L (F)', '519': 'FAKRA Cod. L (M)', '520': 'mini UHF (F)',
# #     '521': 'mini UHF (M)', '522': 'FAKRA Cod. A (F)', '523': 'FAKRA Cod. A (M)',
# #     '524': 'FAKRA Cod. B (F)', '525': 'FAKRA Cod. B (M)', '526': 'FAKRA Cod. C (F)',
# #     '527': 'FAKRA Cod. C (M)', '528': 'FAKRA Cod. D (F)', '529': 'FAKRA Cod. D (M)',
# #     '530': 'FAKRA Cod. E (F)', '531': 'FAKRA Cod. E (M)', '532': 'FME (F)',
# #     '533': 'FME (M)', '534': 'BNC (F)', '535': 'BNC (M)', '536': 'SMA (F)',
# #     '537': 'SMA (M)', '538': 'R-SMA (F)', '539': 'R-SMA (M)', '540': 'SMB (F)',
# #     '541': 'SMB (M)', '542': 'UHF (F)', '543': 'UHF (M)',
# # }
# # MAPOWANIE_DLUGOSCI = {
# #     '030': '3.0 m', '035': '3.5 m', '040': '4.0 m', '045': '4.5 m',
# #     '050': '5.0 m', '055': '5.5 m', '060': '6.0 m', '065': '6.5 m',
# #     '070': '7.0 m', '075': '7.5 m', '080': '8.0 m', '085': '8.5 m',
# #     '090': '9.0 m', '095': '9.5 m', '100': '10.0 m', '105': '10.5 m',
# #     '110': '11.0 m'
# # }
# #
# #
# # # ====================================================================
# # # II. KLASA GENERATORA Z LOGIKĄ TKINTER I TREEVIEW
# # # ====================================================================
# #
# # class GeneratorKabliApp:
# #     def __init__(self, master):
# #         self.master = master
# #         master.title("Generator Numerów Katalogowych Kabli")
# #
# #         # DODANIE KONFIGURACJI STYLU DLA ZABLOKOWANEGO Treeview
# #         style = ttk.Style()
# #         style.configure('Disabled.Treeview', background='#e0e0e0', foreground='#999999')
# #         style.map('Disabled.Treeview',
# #                   background=[('selected', '#e0e0e0')],
# #                   foreground=[('selected', '#999999')])
# #         style.configure('Enabled.Treeview', background='white', foreground='black')
# #
# #         self.mapy = {
# #             'T1': MAPOWANIE_ZLACZY_T1, 'T2': MAPOWANIE_ZLACZY_T2,
# #             'O': MAPOWANIE_ORIENTACJI_DO_WYBORU, 'K': MAPOWANIE_KABLA, 'D': MAPOWANIE_DLUGOSCI
# #         }
# #
# #         # Zmienne do przechowywania WYBRANYCH KODÓW
# #         self.kod_t1 = None;
# #         self.kod_o1 = None
# #         self.kod_t2 = None;
# #         self.kod_o2 = None
# #         self.kod_k = None;
# #         self.kod_d = None
# #
# #         self.utworz_interfejs()
# #         self.przypisz_domyslne_wartosci()
# #
# #         # Ustawienie stanu GUI po inicjalizacji
# #         self.aktualizuj_stan_gui()
# #
# #     def tworz_treeview_wyboru(self, frame, label_text, mapa_danych, variable_name, row):
# #         """Tworzy sekcję Treeview dla pojedynczego wyboru."""
# #
# #         # 1. Tytuł sekcji
# #         ttk.Label(frame, text=f"{label_text}", font=('Arial', 10, 'bold')).grid(row=row, column=0, columnspan=3,
# #                                                                                 sticky='w', pady=(10, 0))
# #
# #         # 2. Treeview (Tabela)
# #         # selectmode='browse' pozwala na zaznaczenie tylko jednego elementu
# #         tree = ttk.Treeview(frame, columns=('Kod', 'Nazwa'), show='headings', height=min(len(mapa_danych), 8),
# #                             selectmode='browse', style='Enabled.Treeview')
# #         tree.heading('Kod', text='KOD', anchor=tk.CENTER)
# #         tree.heading('Nazwa', text='NAZWA / OPIS')
# #         tree.column('Kod', width=60, anchor=tk.CENTER)
# #         tree.column('Nazwa', width=300)
# #
# #         # Wypełnienie danymi
# #         for kod, nazwa in sorted(mapa_danych.items()):
# #             tag = ('brak',) if kod == '000' or kod == '00' else ()
# #             tree.insert('', tk.END, values=(kod, nazwa), tags=tag)
# #
# #         tree.tag_configure('brak', background='#ffe0e0', font=('Arial', 8, 'bold'))
# #
# #         tree.grid(row=row + 1, column=0, columnspan=2, padx=5, sticky='ew')
# #
# #         # Scrollbar
# #         vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
# #         vsb.grid(row=row + 1, column=2, sticky='ns')
# #         tree.configure(yscrollcommand=vsb.set)
# #
# #         # 3. Pole do wyświetlania WYBRANEJ opcji
# #         ttk.Label(frame, text="Wybrany KOD:").grid(row=row + 2, column=0, sticky='w', padx=5, pady=2)
# #         wybrany_kod_label = ttk.Label(frame, text="---", font=('Arial', 10, 'bold'), foreground="blue")
# #         wybrany_kod_label.grid(row=row + 2, column=1, columnspan=2, sticky='w', padx=5, pady=2)
# #
# #         # 4. Ustawienie powiązania (Po kliknięciu) - używamy add=True i unikalnej nazwy, aby móc to potem usunąć
# #         # Powiązanie jest domyślnie dodawane w __init__
# #         tree.bind('<<TreeviewSelect>>',
# #                   lambda event: self.obsluz_wybor_treeview(tree, variable_name, wybrany_kod_label))
# #
# #         # Zapisanie referencji
# #         setattr(self, f'tree_{variable_name}', tree)
# #         setattr(self, f'label_kod_{variable_name}', wybrany_kod_label)
# #
# #         return tree, wybrany_kod_label
# #
# #     def utworz_interfejs(self):
# #         main_frame = ttk.Frame(self.master, padding="10")
# #         main_frame.grid(row=0, column=0, sticky="nsew")
# #
# #         # Użycie ramek do sekcji
# #         left_frame = ttk.LabelFrame(main_frame, text=" Złącze 1 ", padding="10")
# #         left_frame.grid(row=0, column=0, padx=10, pady=5, sticky='n')
# #
# #         right_frame = ttk.LabelFrame(main_frame, text=" Złącze 2 ", padding="10")
# #         right_frame.grid(row=0, column=1, padx=10, pady=5, sticky='n')
# #
# #         bottom_frame = ttk.LabelFrame(main_frame, text=" Kabel i Długość ", padding="10")
# #         bottom_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='ew')
# #
# #         # Tworzenie Treeview dla T1, O1
# #         self.tworz_treeview_wyboru(left_frame, "1. Typ Złącza T1 (3c):", self.mapy['T1'], 't1', 0)
# #         self.tworz_treeview_wyboru(left_frame, "3. Orientacja O1 (2c):", self.mapy['O'], 'o1', 3)
# #
# #         # Tworzenie Treeview dla T2, O2
# #         self.tworz_treeview_wyboru(right_frame, "2. Typ Złącza T2 (3c):", self.mapy['T2'], 't2', 0)
# #         self.tworz_treeview_wyboru(right_frame, "4. Orientacja O2 (2c):", self.mapy['O'], 'o2', 3)
# #
# #         # Tworzenie Treeview dla K, D
# #         self.tworz_treeview_wyboru(bottom_frame, "5. Typ Kabla K (2c):", self.mapy['K'], 'k', 0)
# #         self.tworz_treeview_wyboru(bottom_frame, "6. Długość Kabla D (3c):", self.mapy['D'], 'd', 3)
# #
# #         # --- Sekcja Wyniku ---
# #         ttk.Separator(main_frame, orient='horizontal').grid(row=2, columnspan=2, sticky="ew", pady=10)
# #
# #         ttk.Button(main_frame, text="Generuj Numer Katalogowy", command=self.generuj_numer_katalogowy).grid(row=3,
# #                                                                                                             column=0,
# #                                                                                                             columnspan=2,
# #                                                                                                             pady=10)
# #
# #         ttk.Label(main_frame, text="ZBUDOWANY NUMER:").grid(row=4, column=0, sticky='w')
# #         self.wynik_label = ttk.Label(main_frame, text="---", font=("Arial", 16, "bold"), foreground="navy")
# #         self.wynik_label.grid(row=4, column=1, sticky='w')
# #
# #     def przypisz_domyslne_wartosci(self):
# #         """Ustawia domyślne wartości na pierwszy element listy i wizualnie go zaznacza."""
# #
# #         domyslne_wybory = {
# #             't1': list(self.mapy['T1'].keys())[0],
# #             'o1': list(self.mapy['O'].keys())[0],
# #             't2': list(self.mapy['T2'].keys())[0],
# #             'o2': list(self.mapy['O'].keys())[0],
# #             'k': list(self.mapy['K'].keys())[0],
# #             'd': list(self.mapy['D'].keys())[0],
# #         }
# #
# #         for name, kod in domyslne_wybory.items():
# #             tree = getattr(self, f'tree_{name}')
# #
# #             # --- POPRAWIONA LOGIKA MAPOWANIA KLUCZY ---
# #             map_key = name.upper()
# #             if map_key.startswith(('O', 'K', 'D')):
# #                 map_key = map_key[0]  # Używa 'O', 'K', 'D' zamiast 'O1', 'D1' itd.
# #             # -------------------------------------------
# #
# #             # Znajduje i zaznacza wiersz z domyślnym kodem
# #             for item_id in tree.get_children():
# #                 if tree.item(item_id, 'values')[0] == kod:
# #                     tree.selection_set(item_id)
# #
# #                     setattr(self, f'kod_{name}', kod)
# #
# #                     # Aktualizuje etykietę kodu, używając poprawnego klucza mapy
# #                     getattr(self, f'label_kod_{name}').config(text=f"{kod} - {self.mapy[map_key].get(kod)}")
# #                     break
# #
# #     def obsluz_wybor_treeview(self, tree, variable_name, label_kod):
# #         """Aktualizuje kod po kliknięciu w Treeview."""
# #         wybrane_itemy = tree.selection()
# #         if not wybrane_itemy:
# #             setattr(self, f'kod_{variable_name}', None)
# #             label_kod.config(text="---")
# #             return
# #
# #         wybrany_kod = tree.item(wybrane_itemy[0], 'values')[0]
# #         wybrana_nazwa = tree.item(wybrane_itemy[0], 'values')[1]
# #
# #         setattr(self, f'kod_{variable_name}', wybrany_kod)
# #         label_kod.config(text=f"{wybrany_kod} - {wybrana_nazwa}")
# #
# #         # Uruchomienie logiki sprawdzającej stan (blokowanie/odblokowanie)
# #         self.aktualizuj_stan_gui()
# #
# #     def aktualizuj_stan_gui(self):
# #         """Aktualizuje stan Treeview (blokowanie/odblokowanie) poprzez zarządzanie powiązaniami i stylami."""
# #
# #         # --- Funkcja pomocnicza do ustawiania Orientacji O1/O2 ---
# #         def ustaw_orientacje(kod_zlacza_name, tree_o, label_o, kod_o_name):
# #             kod_zlacza = getattr(self, kod_zlacza_name)
# #             variable_name = kod_o_name.replace('kod_', '')
# #
# #             # Jeśli wybrano 'Brak Złącza', BLOKUJEMY Treeview
# #             if kod_zlacza == '000':
# #                 tree_o.unbind('<<TreeviewSelect>>')  # USUŃ WSZYSTKIE POWIĄZANIA
# #                 tree_o.selection_remove(tree_o.selection())
# #                 setattr(self, kod_o_name, None)
# #
# #                 # Zmiana wyglądu: styl i wyłączenie możliwości wyboru
# #                 tree_o.config(selectmode='none', style='Disabled.Treeview')
# #
# #                 label_o.config(text="--- POMINIĘTE (Brak Złącza) ---", foreground="red")
# #             else:
# #                 # ODBLOKUJ Treeview
# #                 # PRZYWRÓĆ POWIĄZANIE! (Musimy ponownie zdefiniować akcję)
# #                 tree_o.bind('<<TreeviewSelect>>',
# #                             lambda event: self.obsluz_wybor_treeview(tree_o, variable_name, label_o))
# #
# #                 # Zmiana wyglądu: styl i włączenie możliwości wyboru
# #                 tree_o.config(selectmode='browse', style='Enabled.Treeview')
# #                 label_o.config(foreground="blue")
# #
# #                 # Jeśli po odblokowaniu nic nie jest wybrane, ustaw domyślne (zabezpieczenie)
# #                 if not tree_o.selection() or getattr(self, kod_o_name) is None:
# #                     for item_id in tree_o.get_children():
# #                         if tree_o.item(item_id, 'values')[0] == list(self.mapy['O'].keys())[0]:
# #                             tree_o.selection_set(item_id)
# #                             # Wywołujemy obsługę wyboru, aby zaktualizować zmienną kodu
# #                             self.obsluz_wybor_treeview(tree_o, variable_name, label_o)
# #                             break
# #
# #         ustaw_orientacje('kod_t1', self.tree_o1, self.label_kod_o1, 'kod_o1')
# #         ustaw_orientacje('kod_t2', self.tree_o2, self.label_kod_o2, 'kod_o2')
# #
# #         # --- Logika Kabla D (blokowanie) ---
# #         tree_d = self.tree_d
# #         label_d = self.label_kod_d
# #         kod_k = self.kod_k
# #
# #         if kod_k == '00':
# #             tree_d.unbind('<<TreeviewSelect>>')  # USUŃ POWIĄZANIE
# #             tree_d.selection_remove(tree_d.selection())
# #             self.kod_d = None
# #             tree_d.config(selectmode='none', style='Disabled.Treeview')
# #             label_d.config(text="--- POMINIĘTE (Brak Kabla) ---", foreground="red")
# #         else:
# #             tree_d.bind('<<TreeviewSelect>>',
# #                         lambda event: self.obsluz_wybor_treeview(tree_d, 'd', label_d))  # PRZYWRÓĆ POWIĄZANIE
# #             tree_d.config(selectmode='browse', style='Enabled.Treeview')
# #             label_d.config(foreground="blue")
# #
# #             # Jeśli po odblokowaniu nic nie jest wybrane, ustaw domyślne
# #             if not tree_d.selection() or self.kod_d is None:
# #                 for item_id in tree_d.get_children():
# #                     if tree_d.item(item_id, 'values')[0] == list(self.mapy['D'].keys())[0]:
# #                         tree_d.selection_set(item_id)
# #                         self.obsluz_wybor_treeview(tree_d, 'd', label_d)
# #                         break
# #
# #     def generuj_numer_katalogowy(self):
# #         """Główna logika generowania numeru."""
# #
# #         T1 = self.kod_t1
# #         O1 = self.kod_o1
# #         T2 = self.kod_t2
# #         O2 = self.kod_o2
# #         K = self.kod_k
# #         D = self.kod_d
# #
# #         segmenty = []
# #
# #         # Weryfikacja podstawowa (czy wybrano cokolwiek, nawet 'Brak')
# #         if T1 is None or T2 is None or K is None:
# #             messagebox.showerror("Błąd", "Wybierz kody dla Złącza 1, Złącza 2 i Typu Kabla (T1, T2, K).")
# #             return
# #
# #         # 1. T1 (3c) i O1 (2c)
# #         segmenty.append(T1)
# #         if T1 != '000':
# #             if O1 is None:
# #                 messagebox.showerror("Błąd", "Wymagana orientacja O1. Wybierz kod.")
# #                 return
# #             segmenty.append(O1)
# #
# #         # 2. T2 (3c) i O2 (2c)
# #         segmenty.append(T2)
# #         if T2 != '000':
# #             if O2 is None:
# #                 messagebox.showerror("Błąd", "Wymagana orientacja O2. Wybierz kod.")
# #                 return
# #             segmenty.append(O2)
# #
# #         # 3. K (2c) i D (3c)
# #         if K != '00':
# #             segmenty.append(K)
# #             if D is None:
# #                 messagebox.showerror("Błąd", "Wymagana jest długość kabla D. Wybierz kod.")
# #                 return
# #             segmenty.append(D)
# #
# #         numer_katalogowy = "".join(segmenty)
# #         dlugosc_numeru = len(numer_katalogowy)
# #
# #         # Wyświetlenie wyniku
# #         self.wynik_label.config(text=f"{numer_katalogowy} ({dlugosc_numeru} cyfr)")
# #         messagebox.showinfo("Numer Wygenerowany",
# #                             f"Numer Katalogowy: {numer_katalogowy}\nDługość: {dlugosc_numeru} cyfr")
# #
# #
# # # ====================================================================
# # # III. URUCHOMIENIE APLIKACJI
# # # ====================================================================
# #
# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     app = GeneratorKabliApp(root)
# #     root.columnconfigure(0, weight=1)
# #     root.rowconfigure(0, weight=1)
# #     root.mainloop()
#
# import tkinter as tk
# from tkinter import ttk, messagebox
#
# # ====================================================================
# # I. PEŁNE MAPOWANIA DANYCH (Bez zmian)
# # ====================================================================
#
# MAPOWANIE_ORIENTACJI_DO_WYBORU = {
#     '85': 'Proste (Straight)', '84': 'Kątowe (Angled)',
# }
# MAPOWANIE_KABLA = {
#     '00': 'Brak Kabla', '05': 'RG58', '06': 'RG174', '07': 'H155'
# }
# MAPOWANIE_ZLACZY_T1 = {
#     '000': 'Brak Złącza', '100': 'FAKRA Cod. E (F)', '101': 'FAKRA Cod. E (M)',
#     '102': 'FME (F)', '103': 'FME (M)', '104': 'BNC (F)', '105': 'BNC (M)',
#     '106': 'SMA (F)', '107': 'SMA (M)', '108': 'R-SMA (F)', '109': 'R-SMA (M)',
#     '110': 'SMB (F)', '111': 'SMB (M)', '112': 'UHF (F)', '113': 'UHF (M)',
#     '114': 'mini UHF (F)', '115': 'mini UHF (M)', '116': 'FAKRA Cod. A (F)',
#     '117': 'FAKRA Cod. A (M)', '118': 'FAKRA Cod. B (F)', '119': 'FAKRA Cod. B (M)',
#     '120': 'FAKRA Cod. C (F)', '121': 'FAKRA Cod. C (M)', '122': 'FAKRA Cod. D (F)',
#     '123': 'FAKRA Cod. D (M)', '124': 'FAKRA Cod. M (F)', '125': 'FAKRA Cod. M (M)',
#     '126': 'FAKRA Cod. N (F)', '127': 'FAKRA Cod. N (M)', '128': 'FAKRA Cod. Z (F)',
#     '129': 'FAKRA Cod. Z (M)', '130': 'M10 (F)', '131': 'M10 (M)', '132': 'FAKRA Cod. F (F)',
#     '133': 'FAKRA Cod. F (M)', '134': 'FAKRA Cod. G (F)', '135': 'FAKRA Cod. G (M)',
#     '136': 'FAKRA Cod. H (F)', '137': 'FAKRA Cod. H (M)', '138': 'FAKRA Cod. I (F)',
#     '139': 'FAKRA Cod. I (M)', '140': 'FAKRA Cod. K (F)', '141': 'FAKRA Cod. K (M)',
#     '142': 'FAKRA Cod. L (F)', '143': 'FAKRA Cod. L (M)',
# }
# MAPOWANIE_ZLACZY_T2 = {
#     '000': 'Brak Złącza', '500': 'FAKRA Cod. M (F)', '501': 'FAKRA Cod. M (M)',
#     '502': 'FAKRA Cod. N (F)', '503': 'FAKRA Cod. N (M)', '504': 'FAKRA Cod. Z (F)',
#     '505': 'FAKRA Cod. Z (M)', '506': 'M10 (F)', '507': 'M10 (M)', '508': 'FAKRA Cod. F (F)',
#     '509': 'FAKRA Cod. F (M)', '510': 'FAKRA Cod. G (F)', '511': 'FAKRA Cod. G (M)',
#     '512': 'FAKRA Cod. H (F)', '513': 'FAKRA Cod. H (M)', '514': 'FAKRA Cod. I (F)',
#     '515': 'FAKRA Cod. I (M)', '516': 'FAKRA Cod. K (F)', '517': 'FAKRA Cod. K (M)',
#     '518': 'FAKRA Cod. L (F)', '519': 'FAKRA Cod. L (M)', '520': 'mini UHF (F)',
#     '521': 'mini UHF (M)', '522': 'FAKRA Cod. A (F)', '523': 'FAKRA Cod. A (M)',
#     '524': 'FAKRA Cod. B (F)', '525': 'FAKRA Cod. B (M)', '526': 'FAKRA Cod. C (F)',
#     '527': 'FAKRA Cod. C (M)', '528': 'FAKRA Cod. D (F)', '529': 'FAKRA Cod. D (M)',
#     '530': 'FAKRA Cod. E (F)', '531': 'FAKRA Cod. E (M)', '532': 'FME (F)',
#     '533': 'FME (M)', '534': 'BNC (F)', '535': 'BNC (M)', '536': 'SMA (F)',
#     '537': 'SMA (M)', '538': 'R-SMA (F)', '539': 'R-SMA (M)', '540': 'SMB (F)',
#     '541': 'SMB (M)', '542': 'UHF (F)', '543': 'UHF (M)',
# }
# MAPOWANIE_DLUGOSCI = {
#     '030': '3.0 m', '035': '3.5 m', '040': '4.0 m', '045': '4.5 m',
#     '050': '5.0 m', '055': '5.5 m', '060': '6.0 m', '065': '6.5 m',
#     '070': '7.0 m', '075': '7.5 m', '080': '8.0 m', '085': '8.5 m',
#     '090': '9.0 m', '095': '9.5 m', '100': '10.0 m', '105': '10.5 m',
#     '110': '11.0 m'
# }
#
#
# # ====================================================================
# # II. KLASA GENERATORA Z LOGIKĄ TKINTER I TREEVIEW
# # ====================================================================
#
# class GeneratorKabliApp:
#     def __init__(self, master):
#         self.master = master
#         master.title("Generator Numerów Katalogowych Kabli")
#
#         style = ttk.Style()
#         style.configure('Disabled.Treeview', background='#e0e0e0', foreground='#999999')
#         style.map('Disabled.Treeview',
#                   background=[('selected', '#e0e0e0')],
#                   foreground=[('selected', '#999999')])
#         style.configure('Enabled.Treeview', background='white', foreground='black')
#
#         style.configure('Treeview.Heading', font=('Arial', 10, 'bold'))
#         style.configure('Treeview', font=('Arial', 9))
#
#         self.mapy = {
#             'T1': MAPOWANIE_ZLACZY_T1, 'T2': MAPOWANIE_ZLACZY_T2,
#             'O': MAPOWANIE_ORIENTACJI_DO_WYBORU, 'K': MAPOWANIE_KABLA, 'D': MAPOWANIE_DLUGOSCI
#         }
#
#         selfvariables = ['kod_t1', 'kod_o1', 'kod_t2', 'kod_o2', 'kod_k', 'kod_d']
#         for var in selfvariables:
#             setattr(self, var, None)
#
#         self.utworz_interfejs()
#         self.przypisz_domyslne_wartosci()
#
#     def tworz_treeview_wyboru(self, frame, label_text, mapa_danych, variable_name, start_row, start_column, row_span=1):
#         """Tworzy sekcję Treeview bezpośrednio w main_frame."""
#
#         # Etykieta nagłówka
#         ttk.Label(frame, text=f"{label_text}", font=('Arial', 10, 'bold')).grid(row=start_row, column=start_column,
#                                                                                 columnspan=3, sticky='w', pady=(10, 0),
#                                                                                 padx=(5, 0))
#
#         # Okno Treeview
#         tree = ttk.Treeview(frame, columns=('Kod', 'Nazwa'), show='headings', height=min(len(mapa_danych), 10),
#                             selectmode='browse', style='Enabled.Treeview')
#         tree.heading('Kod', text='KOD', anchor=tk.CENTER)
#         tree.heading('Nazwa', text='NAZWA / OPIS')
#         tree.column('Kod', width=70, anchor=tk.CENTER)
#         tree.column('Nazwa', stretch=tk.YES, minwidth=100)  # Rozciąga nazwę
#
#         for kod, nazwa in sorted(mapa_danych.items()):
#             tag = ('brak',) if kod == '000' or kod == '00' else ()
#             tree.insert('', tk.END, values=(kod, nazwa), tags=tag)
#
#         tree.tag_configure('brak', background='#ffe0e0', font=('Arial', 8, 'bold'))
#
#         # Wiersz z Treeview. Używamy 'nsew' dla rozszerzania wewnątrz Grid.
#         tree.grid(row=start_row + 1, column=start_column, columnspan=2, rowspan=row_span, padx=5, sticky='nsew')
#
#         vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
#         vsb.grid(row=start_row + 1, column=start_column + 2, rowspan=row_span, sticky='ns')
#         tree.configure(yscrollcommand=vsb.set)
#
#         # Etykieta wybranego kodu (pod Treeview)
#         ttk.Label(frame, text="Wybrany KOD:").grid(row=start_row + 1 + row_span, column=start_column, sticky='w',
#                                                    padx=5, pady=(5, 10))
#         wybrany_kod_label = ttk.Label(frame, text="---", font=('Arial', 10, 'bold'), foreground="blue")
#         wybrany_kod_label.grid(row=start_row + 1 + row_span, column=start_column + 1, columnspan=2, sticky='w', padx=5,
#                                pady=(5, 10))
#
#         tree.bind('<<TreeviewSelect>>',
#                   lambda event: self.obsluz_wybor_treeview(tree, variable_name, wybrany_kod_label))
#
#         setattr(self, f'tree_{variable_name}', tree)
#         setattr(self, f'label_kod_{variable_name}', wybrany_kod_label)
#
#         # Ustawienie wagi wiersza dla elementu Treeview
#         frame.grid_rowconfigure(start_row + 1, weight=1)
#
#         return tree, wybrany_kod_label
#
#     def utworz_interfejs(self):
#         main_frame = ttk.Frame(self.master, padding="10")
#         main_frame.grid(row=0, column=0, sticky="nsew")
#
#         # --- SEKCJA GÓRNA (Złącza i Orientacje) ---
#
#         # Ustawienie wag dla kolumn main_frame, by równo się rozciągały
#         main_frame.grid_columnconfigure(0, weight=1)
#         main_frame.grid_columnconfigure(1, weight=1)
#         main_frame.grid_columnconfigure(2, weight=1)
#         main_frame.grid_columnconfigure(3, weight=1)
#
#         # 1. Typ Złącza T1 (Wiersze 0-2, Kolumna 0)
#         self.tworz_treeview_wyboru(main_frame, "1. Typ Złącza T1 (3c):", self.mapy['T1'], 't1', 0, 0, row_span=1)
#
#         # 2. Typ Złącza T2 (Wiersze 0-2, Kolumna 2)
#         self.tworz_treeview_wyboru(main_frame, "2. Typ Złącza T2 (3c):", self.mapy['T2'], 't2', 0, 2, row_span=1)
#
#         # 3. Orientacja O1 (Wiersze 3-5, Kolumna 0)
#         self.tworz_treeview_wyboru(main_frame, "3. Orientacja O1 (2c):", self.mapy['O'], 'o1', 3, 0, row_span=1)
#
#         # 4. Orientacja O2 (Wiersze 3-5, Kolumna 2)
#         self.tworz_treeview_wyboru(main_frame, "4. Orientacja O2 (2c):", self.mapy['O'], 'o2', 3, 2, row_span=1)
#
#         # Wiersz 1 i 4 (Treeviews) dostają wagę, by zajęły większość przestrzeni pionowej
#         main_frame.grid_rowconfigure(1, weight=2)
#         main_frame.grid_rowconfigure(4, weight=1)
#
#         # --- SEPARATOR ---
#         ttk.Separator(main_frame, orient='horizontal').grid(row=6, columnspan=4, sticky="ew", pady=(10, 5))
#
#         # --- SEKCJA DOLNA (Kabel i Długość) ---
#
#         # 5. Typ Kabla K (Wiersze 7-9, Kolumna 0)
#         self.tworz_treeview_wyboru(main_frame, "5. Typ Kabla K (2c):", self.mapy['K'], 'k', 7, 0, row_span=1)
#
#         # 6. Długość Kabla D (Wiersze 7-9, Kolumna 2)
#         self.tworz_treeview_wyboru(main_frame, "6. Długość Kabla D (3c):", self.mapy['D'], 'd', 7, 2, row_span=1)
#
#         # Wiersz 8 (Treeview Kabla/Długości) dostaje wagę
#         main_frame.grid_rowconfigure(8, weight=1)
#
#         # --- SEKCJA WYNIKU ---
#         # Separator
#         ttk.Separator(main_frame, orient='horizontal').grid(row=10, columnspan=4, sticky="ew", pady=(10, 5))
#
#         # Etykieta stała (Wiersz 11)
#         ttk.Label(main_frame, text="NUMER PRODUKTU:", font=("Arial", 12, "bold")).grid(row=11, column=0, columnspan=4,
#                                                                                        sticky='w', pady=(5, 0))
#
#         # Etykieta wyniku (Wiersz 12)
#         self.wynik_label = ttk.Label(main_frame, text="---", font=("Arial", 18, "bold"), foreground="navy")
#         self.wynik_label.grid(row=12, column=0, columnspan=4, sticky='w', pady=(0, 5))
#
#         # Konfiguracja głównego okna
#         self.master.columnconfigure(0, weight=1)
#         self.master.rowconfigure(0, weight=1)
#
#     # --- Logika Aplikacji (Bez zmian, ponieważ jest poprawna) ---
#
#     def przypisz_domyslne_wartosci(self):
#         domyslne_wybory_names = ['t1', 't2', 'k', 'o1', 'o2', 'd']
#         for name in domyslne_wybory_names:
#             tree = getattr(self, f'tree_{name}')
#             if tree.get_children():
#                 first_item_id = tree.get_children()[0]
#                 tree.selection_set(first_item_id)
#                 self.obsluz_wybor_treeview(tree, name, getattr(self, f'label_kod_{name}'))
#
#     def obsluz_wybor_treeview(self, tree, variable_name, label_kod):
#         wybrane_itemy = tree.selection()
#         wybrany_kod = None
#         wybrana_nazwa = "---"
#
#         if wybrane_itemy:
#             wybrany_kod_values = tree.item(wybrane_itemy[0], 'values')
#             wybrany_kod = wybrany_kod_values[0]
#             wybrana_nazwa = wybrany_kod_values[1]
#
#         setattr(self, f'kod_{variable_name}', wybrany_kod)
#
#         if wybrany_kod:
#             label_kod.config(text=f"{wybrany_kod} - {wybrana_nazwa}", foreground="blue")
#         else:
#             label_kod.config(text="---", foreground="black")
#
#         self.aktualizuj_stan_gui()
#         self.generuj_numer_katalogowy()
#
#     def aktualizuj_stan_gui(self):
#         def ustaw_orientacje(kod_zlacza_name, tree_o, label_o, kod_o_name):
#             kod_zlacza = getattr(self, kod_zlacza_name)
#             variable_name = kod_o_name.replace('kod_', '')
#
#             if kod_zlacza == '000':
#                 tree_o.unbind('<<TreeviewSelect>>')
#                 tree_o.selection_remove(tree_o.selection())
#                 setattr(self, kod_o_name, None)
#
#                 tree_o.config(selectmode='none', style='Disabled.Treeview')
#                 label_o.config(text="--- POMINIĘTE (Brak Złącza) ---", foreground="red")
#             else:
#                 tree_o.bind('<<TreeviewSelect>>',
#                             lambda event: self.obsluz_wybor_treeview(tree_o, variable_name, label_o))
#                 tree_o.config(selectmode='browse', style='Enabled.Treeview')
#                 label_o.config(foreground="blue")
#
#                 if not tree_o.selection() or getattr(self, kod_o_name) is None:
#                     if tree_o.get_children():
#                         first_item_id = tree_o.get_children()[0]
#                         tree_o.selection_set(first_item_id)
#                         self.obsluz_wybor_treeview(tree_o, variable_name, label_o)
#
#         ustaw_orientacje('kod_t1', self.tree_o1, self.label_kod_o1, 'kod_o1')
#         ustaw_orientacje('kod_t2', self.tree_o2, self.label_kod_o2, 'kod_o2')
#
#         tree_d = self.tree_d
#         label_d = self.label_kod_d
#         kod_k = self.kod_k
#
#         if kod_k == '00':
#             tree_d.unbind('<<TreeviewSelect>>')
#             tree_d.selection_remove(tree_d.selection())
#             self.kod_d = None
#             tree_d.config(selectmode='none', style='Disabled.Treeview')
#             label_d.config(text="--- POMINIĘTE (Brak Kabla) ---", foreground="red")
#         else:
#             tree_d.bind('<<TreeviewSelect>>', lambda event: self.obsluz_wybor_treeview(tree_d, 'd', label_d))
#             tree_d.config(selectmode='browse', style='Enabled.Treeview')
#             label_d.config(foreground="blue")
#
#             if not tree_d.selection() or self.kod_d is None:
#                 if tree_d.get_children():
#                     first_item_id = tree_d.get_children()[0]
#                     tree_d.selection_set(first_item_id)
#                     self.obsluz_wybor_treeview(tree_d, 'd', label_d)
#
#     def generuj_numer_katalogowy(self):
#         T1 = self.kod_t1;
#         O1 = self.kod_o1
#         T2 = self.kod_t2;
#         O2 = self.kod_o2
#         K = self.kod_k;
#         D = self.kod_d
#         segmenty = []
#
#         if T1 is not None:
#             segmenty.append(T1)
#             if T1 != '000' and O1 is not None:
#                 segmenty.append(O1)
#         if T2 is not None:
#             segmenty.append(T2)
#             if T2 != '000' and O2 is not None:
#                 segmenty.append(O2)
#         if K is not None:
#             segmenty.append(K)
#             if K != '00' and D is not None:
#                 segmenty.append(D)
#
#         numer_katalogowy = "".join(segmenty)
#         dlugosc_numeru = len(numer_katalogowy)
#
#         if numer_katalogowy:
#             self.wynik_label.config(text=f"{numer_katalogowy} ({dlugosc_numeru} cyfr)")
#         else:
#             self.wynik_label.config(text="--- BRAK DANYCH ---")
#
#
# # ====================================================================
# # III. URUCHOMIENIE APLIKACJI
# # ====================================================================
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = GeneratorKabliApp(root)
#     root.mainloop()
#

import tkinter as tk
from tkinter import ttk, messagebox

# ====================================================================
# I. PEŁNE MAPOWANIA DANYCH (Bez zmian)
# ====================================================================

MAPOWANIE_ORIENTACJI_DO_WYBORU = {
    '85': 'Proste (Straight)', '84': 'Kątowe (Angled)',
}
MAPOWANIE_KABLA = {
    '00': 'Brak Kabla', '05': 'RG58', '06': 'RG174', '07': 'H155'
}
MAPOWANIE_ZLACZY_T1 = {
    '000': 'Brak Złącza', '100': 'FAKRA Cod. E (F)', '101': 'FAKRA Cod. E (M)',
    '102': 'FME (F)', '103': 'FME (M)', '104': 'BNC (F)', '105': 'BNC (M)',
    '106': 'SMA (F)', '107': 'SMA (M)', '108': 'R-SMA (F)', '109': 'R-SMA (M)',
    '110': 'SMB (F)', '111': 'SMB (M)', '112': 'UHF (F)', '113': 'UHF (M)',
    '114': 'mini UHF (F)', '115': 'mini UHF (M)', '116': 'FAKRA Cod. A (F)',
    '117': 'FAKRA Cod. A (M)', '118': 'FAKRA Cod. B (F)', '119': 'FAKRA Cod. B (M)',
    '120': 'FAKRA Cod. C (F)', '121': 'FAKRA Cod. C (M)', '122': 'FAKRA Cod. D (F)',
    '123': 'FAKRA Cod. D (M)', '124': 'FAKRA Cod. M (F)', '125': 'FAKRA Cod. M (M)',
    '126': 'FAKRA Cod. N (F)', '127': 'FAKRA Cod. N (M)', '128': 'FAKRA Cod. Z (F)',
    '129': 'FAKRA Cod. Z (M)', '130': 'M10 (F)', '131': 'M10 (M)', '132': 'FAKRA Cod. F (F)',
    '133': 'FAKRA Cod. F (M)', '134': 'FAKRA Cod. G (F)', '135': 'FAKRA Cod. G (M)',
    '136': 'FAKRA Cod. H (F)', '137': 'FAKRA Cod. H (M)', '138': 'FAKRA Cod. I (F)',
    '139': 'FAKRA Cod. I (M)', '140': 'FAKRA Cod. K (F)', '141': 'FAKRA Cod. K (M)',
    '142': 'FAKRA Cod. L (F)', '143': 'FAKRA Cod. L (M)',
}
MAPOWANIE_ZLACZY_T2 = {
    '000': 'Brak Złącza', '500': 'FAKRA Cod. M (F)', '501': 'FAKRA Cod. M (M)',
    '502': 'FAKRA Cod. N (F)', '503': 'FAKRA Cod. N (M)', '504': 'FAKRA Cod. Z (F)',
    '505': 'FAKRA Cod. Z (M)', '506': 'M10 (F)', '507': 'M10 (M)', '508': 'FAKRA Cod. F (F)',
    '509': 'FAKRA Cod. F (M)', '510': 'FAKRA Cod. G (F)', '511': 'FAKRA Cod. G (M)',
    '512': 'FAKRA Cod. H (F)', '513': 'FAKRA Cod. H (M)', '514': 'FAKRA Cod. I (F)',
    '515': 'FAKRA Cod. I (M)', '516': 'FAKRA Cod. K (F)', '517': 'FAKRA Cod. K (M)',
    '518': 'FAKRA Cod. L (F)', '519': 'FAKRA Cod. L (M)', '520': 'mini UHF (F)',
    '521': 'mini UHF (M)', '522': 'FAKRA Cod. A (F)', '523': 'FAKRA Cod. A (M)',
    '524': 'FAKRA Cod. B (F)', '525': 'FAKRA Cod. B (M)', '526': 'FAKRA Cod. C (F)',
    '527': 'FAKRA Cod. C (M)', '528': 'FAKRA Cod. D (F)', '529': 'FAKRA Cod. D (M)',
    '530': 'FAKRA Cod. E (F)', '531': 'FAKRA Cod. E (M)', '532': 'FME (F)',
    '533': 'FME (M)', '534': 'BNC (F)', '535': 'BNC (M)', '536': 'SMA (F)',
    '537': 'SMA (M)', '538': 'R-SMA (F)', '539': 'R-SMA (M)', '540': 'SMB (F)',
    '541': 'SMB (M)', '542': 'UHF (F)', '543': 'UHF (M)',
}
MAPOWANIE_DLUGOSCI = {
    '030': '3.0 m', '035': '3.5 m', '040': '4.0 m', '045': '4.5 m',
    '050': '5.0 m', '055': '5.5 m', '060': '6.0 m', '065': '6.5 m',
    '070': '7.0 m', '075': '7.5 m', '080': '8.0 m', '085': '8.5 m',
    '090': '9.0 m', '095': '9.5 m', '100': '10.0 m', '105': '10.5 m',
    '110': '11.0 m'
}


# ====================================================================
# II. KLASA GENERATORA Z LOGIKĄ TKINTER I TREEVIEW
# ====================================================================

class GeneratorKabliApp:
    def __init__(self, master):
        self.master = master
        master.title("Generator Numerów Katalogowych Kabli")

        style = ttk.Style()
        style.configure('Disabled.Treeview', background='#e0e0e0', foreground='#999999')
        style.map('Disabled.Treeview',
                  background=[('selected', '#e0e0e0')],
                  foreground=[('selected', '#999999')])
        style.configure('Enabled.Treeview', background='white', foreground='black')

        style.configure('Treeview.Heading', font=('Arial', 10, 'bold'))
        style.configure('Treeview', font=('Arial', 9))
        style.configure('Zamawiam.TButton', font=('Arial', 12, 'bold'), padding=10, background='green',
                        foreground='black')
        style.map('Zamawiam.TButton', background=[('active', '#00cc00')])

        self.mapy = {
            'T1': MAPOWANIE_ZLACZY_T1, 'T2': MAPOWANIE_ZLACZY_T2,
            'O': MAPOWANIE_ORIENTACJI_DO_WYBORU, 'K': MAPOWANIE_KABLA, 'D': MAPOWANIE_DLUGOSCI
        }

        selfvariables = ['kod_t1', 'kod_o1', 'kod_t2', 'kod_o2', 'kod_k', 'kod_d']
        for var in selfvariables:
            setattr(self, var, None)

        self.utworz_interfejs()
        self.przypisz_domyslne_wartosci()

    def tworz_treeview_wyboru(self, frame, label_text, mapa_danych, variable_name, start_row, start_column, row_span=1):
        """Tworzy sekcję Treeview bezpośrednio w main_frame."""

        # Etykieta nagłówka
        ttk.Label(frame, text=f"{label_text}", font=('Arial', 10, 'bold')).grid(row=start_row, column=start_column,
                                                                                columnspan=3, sticky='w', pady=(10, 0),
                                                                                padx=(5, 0))

        # Okno Treeview
        tree = ttk.Treeview(frame, columns=('Kod', 'Nazwa'), show='headings', height=min(len(mapa_danych), 10),
                            selectmode='browse', style='Enabled.Treeview')
        tree.heading('Kod', text='KOD', anchor=tk.CENTER)
        tree.heading('Nazwa', text='NAZWA / OPIS')
        tree.column('Kod', width=70, anchor=tk.CENTER)
        tree.column('Nazwa', stretch=tk.YES, minwidth=100)

        for kod, nazwa in sorted(mapa_danych.items()):
            tag = ('brak',) if kod == '000' or kod == '00' else ()
            tree.insert('', tk.END, values=(kod, nazwa), tags=tag)

        tree.tag_configure('brak', background='#ffe0e0', font=('Arial', 8, 'bold'))

        tree.grid(row=start_row + 1, column=start_column, columnspan=2, rowspan=row_span, padx=5, sticky='nsew')

        vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        vsb.grid(row=start_row + 1, column=start_column + 2, rowspan=row_span, sticky='ns')
        tree.configure(yscrollcommand=vsb.set)

        # Etykieta wybranego kodu (pod Treeview)
        ttk.Label(frame, text="Wybrany KOD:").grid(row=start_row + 1 + row_span, column=start_column, sticky='w',
                                                   padx=5, pady=(5, 10))
        wybrany_kod_label = ttk.Label(frame, text="---", font=('Arial', 10, 'bold'), foreground="blue")
        wybrany_kod_label.grid(row=start_row + 1 + row_span, column=start_column + 1, columnspan=2, sticky='w', padx=5,
                               pady=(5, 10))

        tree.bind('<<TreeviewSelect>>',
                  lambda event: self.obsluz_wybor_treeview(tree, variable_name, wybrany_kod_label))

        setattr(self, f'tree_{variable_name}', tree)
        setattr(self, f'label_kod_{variable_name}', wybrany_kod_label)

        # Ustawienie wagi wiersza dla elementu Treeview
        frame.grid_rowconfigure(start_row + 1, weight=1)

        return tree, wybrany_kod_label

    def utworz_interfejs(self):
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")

        # --- SEKCJA GÓRNA (Złącza i Orientacje) ---

        # Ustawienie wag dla kolumn main_frame, by równo się rozciągały
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=0)  # Kolumna suwaka
        main_frame.grid_columnconfigure(2, weight=1)
        main_frame.grid_columnconfigure(3, weight=0)  # Kolumna suwaka

        # 1. Typ Złącza T1
        self.tworz_treeview_wyboru(main_frame, "1. Typ Złącza T1 (3c):", self.mapy['T1'], 't1', 0, 0, row_span=1)

        # 2. Typ Złącza T2
        self.tworz_treeview_wyboru(main_frame, "2. Typ Złącza T2 (3c):", self.mapy['T2'], 't2', 0, 2, row_span=1)

        # 3. Orientacja O1
        self.tworz_treeview_wyboru(main_frame, "3. Orientacja O1 (2c):", self.mapy['O'], 'o1', 3, 0, row_span=1)

        # 4. Orientacja O2
        self.tworz_treeview_wyboru(main_frame, "4. Orientacja O2 (2c):", self.mapy['O'], 'o2', 3, 2, row_span=1)

        # Wiersz 1 i 4 (Treeviews) dostają wagę, by zajęły większość przestrzeni pionowej
        main_frame.grid_rowconfigure(1, weight=2)
        main_frame.grid_rowconfigure(4, weight=1)

        # --- SEPARATOR GÓRNY ---
        ttk.Separator(main_frame, orient='horizontal').grid(row=6, columnspan=4, sticky="ew", pady=(10, 5))

        # --- SEKCJA DOLNA (Kabel i Długość) ---

        # 5. Typ Kabla K
        self.tworz_treeview_wyboru(main_frame, "5. Typ Kabla K (2c):", self.mapy['K'], 'k', 7, 0, row_span=1)

        # 6. Długość Kabla D
        self.tworz_treeview_wyboru(main_frame, "6. Długość Kabla D (3c):", self.mapy['D'], 'd', 7, 2, row_span=1)

        # Wiersz 8 (Treeview Kabla/Długości) dostaje wagę
        main_frame.grid_rowconfigure(8, weight=1)

        # --- SEKCJA WYNIKU I PRZYCISK "ZAMAWIAM" ---

        # Separator Dolny
        ttk.Separator(main_frame, orient='horizontal').grid(row=10, columnspan=4, sticky="ew", pady=(10, 5))

        # Etykieta stała (Wiersz 11)
        ttk.Label(main_frame, text="NUMER PRODUKTU:", font=("Arial", 12, "bold")).grid(row=11, column=0, columnspan=2,
                                                                                       sticky='w', pady=(5, 0))

        # Etykieta wyniku (Wiersz 12, Kolumny 0-2)
        self.wynik_label = ttk.Label(main_frame, text="---", font=("Arial", 18, "bold"), foreground="navy")
        self.wynik_label.grid(row=12, column=0, columnspan=3, sticky='w', padx=5, pady=(0, 10))

        # 🌟 PRZYCISK "ZAMAWIAM" (Wiersz 12, Kolumna 3, w prawym dolnym rogu)
        ttk.Button(main_frame, text="ZAMAWIAM",
                   command=lambda: self.generuj_numer_katalogowy(pokaz_alert=True),
                   style='Zamawiam.TButton'
                   ).grid(row=12, column=3, sticky='se', padx=5,
                          pady=(0, 10))  # 'se' przypina do prawego dolnego rogu komórki

        # Konfiguracja głównego okna
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

    # --- Logika Aplikacji (Bez zmian) ---

    def przypisz_domyslne_wartosci(self):
        domyslne_wybory_names = ['t1', 't2', 'k', 'o1', 'o2', 'd']
        for name in domyslne_wybory_names:
            tree = getattr(self, f'tree_{name}')
            if tree.get_children():
                first_item_id = tree.get_children()[0]
                tree.selection_set(first_item_id)
                self.obsluz_wybor_treeview(tree, name, getattr(self, f'label_kod_{name}'))

    def obsluz_wybor_treeview(self, tree, variable_name, label_kod):
        wybrane_itemy = tree.selection()
        wybrany_kod = None
        wybrana_nazwa = "---"

        if wybrane_itemy:
            wybrany_kod_values = tree.item(wybrane_itemy[0], 'values')
            wybrany_kod = wybrany_kod_values[0]
            wybrana_nazwa = wybrany_kod_values[1]

        setattr(self, f'kod_{variable_name}', wybrany_kod)

        if wybrany_kod:
            label_kod.config(text=f"{wybrany_kod} - {wybrana_nazwa}", foreground="blue")
        else:
            label_kod.config(text="---", foreground="black")

        self.aktualizuj_stan_gui()
        self.generuj_numer_katalogowy()

    def aktualizuj_stan_gui(self):
        def ustaw_orientacje(kod_zlacza_name, tree_o, label_o, kod_o_name):
            kod_zlacza = getattr(self, kod_zlacza_name)
            variable_name = kod_o_name.replace('kod_', '')

            if kod_zlacza == '000':
                tree_o.unbind('<<TreeviewSelect>>')
                tree_o.selection_remove(tree_o.selection())
                setattr(self, kod_o_name, None)

                tree_o.config(selectmode='none', style='Disabled.Treeview')
                label_o.config(text="--- POMINIĘTE (Brak Złącza) ---", foreground="red")
            else:
                tree_o.bind('<<TreeviewSelect>>',
                            lambda event: self.obsluz_wybor_treeview(tree_o, variable_name, label_o))
                tree_o.config(selectmode='browse', style='Enabled.Treeview')
                label_o.config(foreground="blue")

                if not tree_o.selection() or getattr(self, kod_o_name) is None:
                    if tree_o.get_children():
                        first_item_id = tree_o.get_children()[0]
                        tree_o.selection_set(first_item_id)
                        self.obsluz_wybor_treeview(tree_o, variable_name, label_o)

        ustaw_orientacje('kod_t1', self.tree_o1, self.label_kod_o1, 'kod_o1')
        ustaw_orientacje('kod_t2', self.tree_o2, self.label_kod_o2, 'kod_o2')

        tree_d = self.tree_d
        label_d = self.label_kod_d
        kod_k = self.kod_k

        if kod_k == '00':
            tree_d.unbind('<<TreeviewSelect>>')
            tree_d.selection_remove(tree_d.selection())
            self.kod_d = None
            tree_d.config(selectmode='none', style='Disabled.Treeview')
            label_d.config(text="--- POMINIĘTE (Brak Kabla) ---", foreground="red")
        else:
            tree_d.bind('<<TreeviewSelect>>', lambda event: self.obsluz_wybor_treeview(tree_d, 'd', label_d))
            tree_d.config(selectmode='browse', style='Enabled.Treeview')
            label_d.config(foreground="blue")

            if not tree_d.selection() or self.kod_d is None:
                if tree_d.get_children():
                    first_item_id = tree_d.get_children()[0]
                    tree_d.selection_set(first_item_id)
                    self.obsluz_wybor_treeview(tree_d, 'd', label_d)

    def generuj_numer_katalogowy(self, pokaz_alert=False):
        T1 = self.kod_t1;
        O1 = self.kod_o1
        T2 = self.kod_t2;
        O2 = self.kod_o2
        K = self.kod_k;
        D = self.kod_d
        segmenty = []

        if pokaz_alert:
            if T1 is None or T2 is None or K is None:
                messagebox.showerror("Błąd Weryfikacji", "Musisz wybrać Złącze 1 (T1), Złącze 2 (T2) i Typ Kabla (K).")
                return
            if T1 != '000' and O1 is None:
                messagebox.showerror("Błąd Orientacji O1", "Wymagana jest Orientacja O1 dla wybranego Złącza T1.")
                return
            if T2 != '000' and O2 is None:
                messagebox.showerror("Błąd Orientacji O2", "Wymagana jest Orientacja O2 dla wybranego Złącza T2.")
                return
            if K != '00' and D is None:
                messagebox.showerror("Błąd Długości D", "Wymagana jest Długość Kabla D dla wybranego Typu Kabla K.")
                return

        if T1 is not None:
            segmenty.append(T1)
            if T1 != '000' and O1 is not None:
                segmenty.append(O1)
        if T2 is not None:
            segmenty.append(T2)
            if T2 != '000' and O2 is not None:
                segmenty.append(O2)
        if K is not None:
            segmenty.append(K)
            if K != '00' and D is not None:
                segmenty.append(D)

        numer_katalogowy = "".join(segmenty)
        dlugosc_numeru = len(numer_katalogowy)

        if numer_katalogowy:
            self.wynik_label.config(text=f"{numer_katalogowy} ({dlugosc_numeru} cyfr)")
        else:
            self.wynik_label.config(text="--- BRAK DANYCH ---")

        if pokaz_alert and numer_katalogowy:
            messagebox.showinfo("Potwierdzenie Zamówienia",
                                f"Złożono zamówienie na produkt:\n{numer_katalogowy}\nDługość kodu: {dlugosc_numeru} cyfr")


# ====================================================================
# III. URUCHOMIENIE APLIKACJI
# ====================================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = GeneratorKabliApp(root)
    root.mainloop()