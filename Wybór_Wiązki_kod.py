#
# from collections import OrderedDict
# import textwrap
#
#
# def generuj_numer_katalogowy_tylko_kod():
#     """
#     Generuje Numer Katalogowy Kabla. Wymaga od użytkownika bezpośredniego wprowadzania KODU
#     z wyświetlanej tabeli w każdym kroku.
#     """
#
#     # 1. Mapowania (bez zmian)
#
#     # A. Orientacja Złącza (O1, O2)
#     mapowanie_orientacji = {
#         '1': ('85', 'Proste (Straight)'),
#         '2': ('84', 'Kątowe (Angled)'),
#         '3': ('00', 'Brak złącza')
#     }
#
#     # B. Typ Kabla (K) - Kody 2-cyfrowe
#     mapowanie_kabla = {
#         '1': ('05', 'RG58'),
#         '2': ('06', 'RG174'),
#         '3': ('07', 'H155')
#     }
#
#     # C. Typ Złącza (T1: 100-143, T2: 500-543) - Pełna lista
#     mapowanie_zlaczy = {
#         '100': 'FAKRA Cod. E (F)', '101': 'FAKRA Cod. E (M)', '102': 'FME (F)', '103': 'FME (M)',
#         '104': 'BNC (F)', '105': 'BNC (M)', '106': 'SMA (F)', '107': 'SMA (M)',
#         '108': 'R-SMA (F)', '109': 'R-SMA (M)', '110': 'SMB (F)', '111': 'SMB (M)',
#         '112': 'UHF (F)', '113': 'UHF (M)', '114': 'mini UHF (F)', '115': 'mini UHF (M)',
#         '116': 'FAKRA Cod. A (F)', '117': 'FAKRA Cod. A (M)', '118': 'FAKRA Cod. B (F)', '119': 'FAKRA Cod. B (M)',
#         '120': 'FAKRA Cod. C (F)', '121': 'FAKRA Cod. C (M)', '122': 'FAKRA Cod. D (F)', '123': 'FAKRA Cod. D (M)',
#         '124': 'FAKRA Cod. M (F)', '125': 'FAKRA Cod. M (M)', '126': 'FAKRA Cod. N (F)', '127': 'FAKRA Cod. N (M)',
#         '128': 'FAKRA Cod. Z (F)', '129': 'FAKRA Cod. Z (M)', '130': 'M10 (F)', '131': 'M10 (M)',
#         '132': 'FAKRA Cod. F (F)', '133': 'FAKRA Cod. F (M)', '134': 'FAKRA Cod. G (F)', '135': 'FAKRA Cod. G (M)',
#         '136': 'FAKRA Cod. H (F)', '137': 'FAKRA Cod. H (M)', '138': 'FAKRA Cod. I (F)', '139': 'FAKRA Cod. I (M)',
#         '140': 'FAKRA Cod. K (F)', '141': 'FAKRA Cod. K (M)', '142': 'FAKRA Cod. L (F)', '143': 'FAKRA Cod. L (M)',
#
#         # Kody dla Złącza 2 (500-543)
#         '500': 'FAKRA Cod. M (F)', '501': 'FAKRA Cod. M (M)', '502': 'FAKRA Cod. N (F)', '503': 'FAKRA Cod. N (M)',
#         '504': 'FAKRA Cod. Z (F)', '505': 'FAKRA Cod. Z (M)', '506': 'M10 (F)', '507': 'M10 (M)',
#         '508': 'FAKRA Cod. F (F)', '509': 'FAKRA Cod. F (M)', '510': 'FAKRA Cod. G (F)', '511': 'FAKRA Cod. G (M)',
#         '512': 'FAKRA Cod. H (F)', '513': 'FAKRA Cod. H (M)', '514': 'FAKRA Cod. I (F)', '515': 'FAKRA Cod. I (M)',
#         '516': 'FAKRA Cod. K (F)', '517': 'FAKRA Cod. K (M)', '518': 'FAKRA Cod. L (F)', '519': 'FAKRA Cod. L (M)',
#         '520': 'mini UHF (F)', '521': 'mini UHF (M)', '522': 'FAKRA Cod. A (F)', '523': 'FAKRA Cod. A (M)',
#         '524': 'FAKRA Cod. B (F)', '525': 'FAKRA Cod. B (M)', '526': 'FAKRA Cod. C (F)', '527': 'FAKRA Cod. C (M)',
#         '528': 'FAKRA Cod. D (F)', '529': 'FAKRA Cod. D (M)', '530': 'FAKRA Cod. E (F)', '531': 'FAKRA Cod. E (M)',
#         '532': 'FME (F)', '533': 'FME (M)', '534': 'BNC (F)', '535': 'BNC (M)',
#         '536': 'SMA (F)', '537': 'SMA (M)', '538': 'R-SMA (F)', '539': 'R-SMA (M)',
#         '540': 'SMB (F)', '541': 'SMB (M)', '542': 'UHF (F)', '543': 'UHF (M)',
#     }
#
#     # D. Długość Kabla (D)
#     mapowanie_dlugosci = {
#         '030': '3.0 m', '035': '3.5 m', '040': '4.0 m', '045': '4.5 m',
#         '050': '5.0 m', '055': '5.5 m', '060': '6.0 m', '065': '6.5 m',
#         '070': '7.0 m', '075': '7.5 m', '080': '8.0 m', '085': '8.5 m',
#         '090': '9.0 m', '095': '9.5 m', '100': '10.0 m', '105': '10.5 m',
#         '110': '11.0 m'
#     }
#
#     # Funkcja pomocnicza do drukowania list Złączy (KROKI 1, 2)
#     def drukuj_i_pobierz_kod_zlacza(numer, kody_start, kody_end):
#         print(f"\n--- KROK {numer}: Wybór Typu Złącza {numer} ({kody_start}-{kody_end}) ---")
#
#         dostepne_kody = {k: v for k, v in mapowanie_zlaczy.items()
#                          if kody_start <= k <= kody_end}
#
#         kody_posortowane = sorted(dostepne_kody.keys())
#
#         # Drukowanie w 4 kolumnach
#         kolumny = 4
#         wiersze = (len(kody_posortowane) + kolumny - 1) // kolumny
#
#         print("+" + "-" * 74 + "+")
#         print("| KOD | NAZWA ZŁĄCZA " + " " * 12 + "| KOD | NAZWA ZŁĄCZA " + " " * 12 + "|")
#         print("+" + "-" * 74 + "+")
#
#         for i in range(wiersze):
#             wiersz = []
#             for j in range(kolumny):
#                 indeks = i + j * wiersze
#                 if indeks < len(kody_posortowane):
#                     kod = kody_posortowane[indeks]
#                     nazwa = dostepne_kody[kod]
#
#                     if j % 2 == 0:
#                         wiersz.append(f"| {kod:<3} | {nazwa:<22}")
#                     else:
#                         wiersz.append(f"{kod:<3} | {nazwa:<22} |")
#
#                 else:
#                     if j % 2 == 0:
#                         wiersz.append("|" + " " * 30)
#                     else:
#                         wiersz.append(" " * 30 + "|")
#
#             print("".join(wiersz))
#
#         print("+" + "-" * 74 + "+")
#
#         while True:
#             kod = input(f"Wprowadź 3-cyfrowy KOD Złącza {numer}: ").strip()
#             if kod in dostepne_kody and len(kod) == 3:
#                 return kod, mapowanie_zlaczy[kod]
#             print(f"Nieprawidłowy KOD. Wprowadź kod z zakresu {kody_start}-{kody_end}.")
#
#     # Funkcja pomocnicza do drukowania list Orientacji i Kabli (KROKI 3, 4, 5)
#     def drukuj_i_pobierz_prosta_liste(numer, prompt, opcje_dict, kod_dlugosc):
#         print(f"\n--- KROK {numer}: Wybór {prompt} ---")
#         print("+" + "-" * (25 + kod_dlugosc) + "+")
#         print(f"| KOD {' ' * (kod_dlugosc - 3)} | NAZWA ODP. |")  # Nagłówek dynamicznej długości
#         print("+" + "-" * (25 + kod_dlugosc) + "+")
#
#         wybor_mapa = {}
#         for klucz, (kod, nazwa) in opcje_dict.items():
#             print(f"| {kod:<{kod_dlugosc}} | {nazwa:<20} |")
#             wybor_mapa[kod] = nazwa  # KOD jako klucz do wyboru
#
#         print("+" + "-" * (25 + kod_dlugosc) + "+")
#
#         while True:
#             kod_wybor = input(f"Wprowadź KOD {prompt}: ").strip()
#             if kod_wybor in wybor_mapa and len(kod_wybor) == kod_dlugosc:
#                 nazwa = wybor_mapa[kod_wybor]
#                 print(f"Wybrano: {nazwa} (Kod: {kod_wybor})")
#                 return kod_wybor, nazwa
#             print(f"Nieprawidłowy KOD. Musi mieć {kod_dlugosc} cyfry i być z listy.")
#
#     # Funkcja pomocnicza do drukowania listy Długości (KROK 6)
#     def drukuj_i_pobierz_dlugosc(numer, prompt):
#         print(f"\n--- KROK {numer}: Wybór {prompt} ---")
#         print("+" + "-" * 25 + "+")
#         print("| KOD | DŁUGOŚĆ |")
#         print("+" + "-" * 25 + "+")
#
#         kody_dlugosci = sorted(mapowanie_dlugosci.keys())
#         wybor_mapa = {}
#
#         for kod in kody_dlugosci:
#             nazwa = mapowanie_dlugosci[kod]
#             print(f"| {kod:<3} | {nazwa:<15} |")
#             wybor_mapa[kod] = nazwa
#
#         print("+" + "-" * 25 + "+")
#
#         while True:
#             kod = input("Wprowadź 3-cyfrowy KOD Długości: ").strip()
#             if kod in wybor_mapa and len(kod) == 3:
#                 nazwa = wybor_mapa[kod]
#                 print(f"Wybrano: {nazwa} (Kod: {kod})")
#                 return kod, nazwa
#             print("Nieprawidłowy KOD. Musi mieć 3 cyfry i być z listy.")
#
#     # --- PROCES BUDOWANIA KODU (T1, T2, O1, O2, K, D) ---
#
#     # 1. Typ Złącza 1 (T1)
#     kod_zlacza_1, nazwa_zlacza_1 = drukuj_i_pobierz_kod_zlacza(1, '100', '143')
#
#     # 2. Typ Złącza 2 (T2)
#     kod_zlacza_2, nazwa_zlacza_2 = drukuj_i_pobierz_kod_zlacza(2, '500', '543')
#
#     # 3. Orientacja Złącza 1 (O1)
#     kody_orientacji_do_druku = {k: mapowanie_orientacji[k] for k in sorted(mapowanie_orientacji.keys())}
#     kod_orientacji_1, nazwa_orientacji_1 = drukuj_i_pobierz_prosta_liste(3, "Orientacji Złącza 1",
#                                                                          kody_orientacji_do_druku, 2)
#
#     # 4. Orientacja Złącza 2 (O2)
#     kod_orientacji_2, nazwa_orientacji_2 = drukuj_i_pobierz_prosta_liste(4, "Orientacji Złącza 2",
#                                                                          kody_orientacji_do_druku, 2)
#
#     # 5. Typ Kabla (K)
#     kody_kabli_do_druku = {k: mapowanie_kabla[k] for k in sorted(mapowanie_kabla.keys())}
#     kod_kabla, nazwa_kabla = drukuj_i_pobierz_prosta_liste(5, "Typu Kabla", kody_kabli_do_druku, 2)
#
#     # 6. Długość Kabla (D)
#     kod_dlugosci, nazwa_dlugosci = drukuj_i_pobierz_dlugosc(6, "Długości Kabla")
#
#     # --- GENEROWANIE NUMERU KATALOGOWEGO ---
#
#     # Połączenie: T1 (3c) + T2 (3c) + O1 (2c) + O2 (2c) + K (2c) + D (3c) = 17 cyfr
#     numer_katalogowy = (
#             kod_zlacza_1 +
#             kod_zlacza_2 +
#             kod_orientacji_1 +
#             kod_orientacji_2 +
#             kod_kabla +
#             kod_dlugosci
#     )
#
#     # --- PODSUMOWANIE ---
#
#     print("\n" + "=" * 70)
#     print("### ✅ Zbudowany Numer Katalogowy Kabla:")
#     print(f"**{numer_katalogowy}** (17 cyfr)")
#     print("=" * 70)
#     print("\n**DETALE KONSTRUKCJI (T1 + T2 + O1 + O2 + K + D):**")
#     print("| Pole | Nazwa | Kod | Pełna Nazwa |")
#     print("|:---:|:---:|:---:|:---:|")
#     print(f"| T1 | Typ Złącza 1 | {kod_zlacza_1} | {nazwa_zlacza_1} |")
#     print(f"| T2 | Typ Złącza 2 | {kod_zlacza_2} | {nazwa_zlacza_2} |")
#     print(f"| O1 | Orientacja Złącza 1 | {kod_orientacji_1} | {nazwa_orientacji_1} |")
#     print(f"| O2 | Orientacja Złącza 2 | {kod_orientacji_2} | {nazwa_orientacji_2} |")
#     print(f"| K | Typ Kabla | {kod_kabla} | {nazwa_kabla} |")
#     print(f"| D | Długość Kabla | {kod_dlugosci} | {nazwa_dlugosci} |")
#     print(
#         f"\n**STRUKTURA KOŃCOWA:** {kod_zlacza_1}{kod_zlacza_2}{kod_orientacji_1}{kod_orientacji_2}{kod_kabla}{kod_dlugosci}")
#
#
# # Uruchomienie programu
# generuj_numer_katalogowy_tylko_kod()
#
# -----------------------------------------------------------------------------------------------------------------------------------

def generuj_numer_katalogowy_finalny_v12():
    """
    Generuje Numer Katalogowy Kabla ze zmienną długością, zgodnie z precyzyjnymi regułami.
    Dodano opcję 'Brak Kabla' (kod '00') w Kroku 5, co pomija segmenty K i D w numerze.
    """

    # 1. Mapowania Danych

    # A. Orientacja Złącza (O1, O2) - Tylko opcje do RĘCZNEGO wyboru
    mapowanie_orientacji_do_wyboru = {
        '85': 'Proste (Straight)',
        '84': 'Kątowe (Angled)',
    }

    # B. Typ Kabla (K) - Kody 2-cyfrowe - ZAKTUALIZOWANE
    mapowanie_kabla = {
        '00': 'Brak Kabla',  # NOWOŚĆ: Pomija K i D w numerze
        '05': 'RG58',
        '06': 'RG174',
        '07': 'H155'
    }

    # C. Typ Złącza (T1, T2)
    mapowanie_zlaczy = {
        '000': 'Brak Złącza',
        '100': 'FAKRA Cod. E (F)', '101': 'FAKRA Cod. E (M)', '102': 'FME (F)', '103': 'FME (M)',
        '104': 'BNC (F)', '105': 'BNC (M)', '106': 'SMA (F)', '107': 'SMA (M)',
        '108': 'R-SMA (F)', '109': 'R-SMA (M)', '110': 'SMB (F)', '111': 'SMB (M)',
        '112': 'UHF (F)', '113': 'UHF (M)', '114': 'mini UHF (F)', '115': 'mini UHF (M)',
        '116': 'FAKRA Cod. A (F)', '117': 'FAKRA Cod. A (M)', '118': 'FAKRA Cod. B (F)', '119': 'FAKRA Cod. B (M)',
        '120': 'FAKRA Cod. C (F)', '121': 'FAKRA Cod. C (M)', '122': 'FAKRA Cod. D (F)', '123': 'FAKRA Cod. D (M)',
        '124': 'FAKRA Cod. M (F)', '125': 'FAKRA Cod. M (M)', '126': 'FAKRA Cod. N (F)', '127': 'FAKRA Cod. N (M)',
        '128': 'FAKRA Cod. Z (F)', '129': 'FAKRA Cod. Z (M)', '130': 'M10 (F)', '131': 'M10 (M)',
        '132': 'FAKRA Cod. F (F)', '133': 'FAKRA Cod. F (M)', '134': 'FAKRA Cod. G (F)', '135': 'FAKRA Cod. G (M)',
        '136': 'FAKRA Cod. H (F)', '137': 'FAKRA Cod. H (M)', '138': 'FAKRA Cod. I (F)', '139': 'FAKRA Cod. I (M)',
        '140': 'FAKRA Cod. K (F)', '141': 'FAKRA Cod. K (M)', '142': 'FAKRA Cod. L (F)', '143': 'FAKRA Cod. L (M)',

        '500': 'FAKRA Cod. M (F)', '501': 'FAKRA Cod. M (M)', '502': 'FAKRA Cod. N (F)', '503': 'FAKRA Cod. N (M)',
        '504': 'FAKRA Cod. Z (F)', '505': 'FAKRA Cod. Z (M)', '506': 'M10 (F)', '507': 'M10 (M)',
        '508': 'FAKRA Cod. F (F)', '509': 'FAKRA Cod. F (M)', '510': 'FAKRA Cod. G (F)', '511': 'FAKRA Cod. G (M)',
        '512': 'FAKRA Cod. H (F)', '513': 'FAKRA Cod. H (M)', '514': 'FAKRA Cod. I (F)', '515': 'FAKRA Cod. I (M)',
        '516': 'FAKRA Cod. K (F)', '517': 'FAKRA Cod. K (M)', '518': 'FAKRA Cod. L (F)', '519': 'FAKRA Cod. L (M)',
        '520': 'mini UHF (F)', '521': 'mini UHF (M)', '522': 'FAKRA Cod. A (F)', '523': 'FAKRA Cod. A (M)',
        '524': 'FAKRA Cod. B (F)', '525': 'FAKRA Cod. B (M)', '526': 'FAKRA Cod. C (F)', '527': 'FAKRA Cod. C (M)',
        '528': 'FAKRA Cod. D (F)', '529': 'FAKRA Cod. D (M)', '530': 'FAKRA Cod. E (F)', '531': 'FAKRA Cod. E (M)',
        '532': 'FME (F)', '533': 'FME (M)', '534': 'BNC (F)', '535': 'BNC (M)',
        '536': 'SMA (F)', '537': 'SMA (M)', '538': 'R-SMA (F)', '539': 'R-SMA (M)',
        '540': 'SMB (F)', '541': 'SMB (M)', '542': 'UHF (F)', '543': 'UHF (M)',
    }

    # D. Długość Kabla (D)
    mapowanie_dlugosci = {
        '030': '3.0 m', '035': '3.5 m', '040': '4.0 m', '045': '4.5 m',
        '050': '5.0 m', '055': '5.5 m', '060': '6.0 m', '065': '6.5 m',
        '070': '7.0 m', '075': '7.5 m', '080': '8.0 m', '085': '8.5 m',
        '090': '9.0 m', '095': '9.5 m', '100': '10.0 m', '105': '10.5 m',
        '110': '11.0 m'
    }

    # --- Funkcje Pomocnicze do Drukowania Tebel i Pobierania KODU ---

    def drukuj_i_pobierz_kod_zlacza(numer, kody_start, kody_end):
        print(f"\n--- KROK {numer}: Wybór Typu Złącza {numer} ({kody_start}-{kody_end} lub 000) ---")

        dostepne_kody = {}
        for k, v in mapowanie_zlaczy.items():
            if k == '000' or (kody_start <= k <= kody_end):
                dostepne_kody[k] = v

        kody_posortowane = sorted(dostepne_kody.keys())

        szerokosc_nazwy = 35
        szerokosc_tabeli = szerokosc_nazwy + 7

        print("+" + "-" * szerokosc_tabeli + "+")
        print(f"| KOD | NAZWA ZŁĄCZA " + " " * (szerokosc_nazwy - 15) + "|")
        print("+" + "-" * szerokosc_tabeli + "+")

        for kod in kody_posortowane:
            nazwa = dostepne_kody[kod]
            if kod == '000':
                print(f"| **{kod:<3}** | **{nazwa:<{szerokosc_nazwy}}** |")
            else:
                print(f"| {kod:<3} | {nazwa:<{szerokosc_nazwy}} |")

        print("+" + "-" * szerokosc_tabeli + "+")

        while True:
            kod = input(f"Wprowadź 3-cyfrowy KOD Złącza {numer} (Zakres: {kody_start}-{kody_end} lub 000): ").strip()

            if kod in dostepne_kody and len(kod) == 3:
                print(f"Wybrano: {dostepne_kody[kod]}")
                return kod, mapowanie_zlaczy[kod]
            print(f"Nieprawidłowy KOD. Wprowadź 3-cyfrowy kod z zakresu {kody_start}-{kody_end} lub 000.")

    def drukuj_i_pobierz_kod_prosty(numer, prompt, mapa_kodow, dlugosc_kodu, naglowek):
        print(f"\n--- KROK {numer}: Wybór {prompt} ---")

        dlugosc_nazwy = 20
        dlugosc_tabeli = dlugosc_nazwy + dlugosc_kodu + 7

        print("+" + "-" * dlugosc_tabeli + "+")
        print(f"| KOD | {naglowek:<{dlugosc_nazwy}} |")
        print("+" + "-" * dlugosc_tabeli + "+")

        # Wypisujemy najpierw kod '00' jeśli istnieje
        kody_posortowane = sorted(mapa_kodow.keys())
        wybor_mapa = {}

        if '00' in mapa_kodow:
            kod = '00'
            nazwa = mapa_kodow[kod]
            print(f"| **{kod:<{dlugosc_kodu}}** | **{nazwa:<{dlugosc_nazwy}}** |")
            wybor_mapa[kod] = nazwa
            kody_posortowane.remove('00')  # Usuwamy, by nie drukować drugi raz

        for kod in kody_posortowane:
            nazwa = mapa_kodow[kod]
            print(f"| {kod:<{dlugosc_kodu}} | {nazwa:<{dlugosc_nazwy}} |")
            wybor_mapa[kod] = nazwa

        print("+" + "-" * dlugosc_tabeli + "+")

        while True:
            kod = input(f"Wprowadź {dlugosc_kodu}-cyfrowy KOD {prompt}: ").strip()
            if kod in wybor_mapa and len(kod) == dlugosc_kodu:
                nazwa = wybor_mapa[kod]
                print(f"Wybrano: {nazwa} (Kod: {kod})")
                return kod, nazwa
            print(f"Nieprawidłowy KOD. Musi mieć {dlugosc_kodu} cyfry i być z listy.")

    # --- PROCES BUDOWANIA KODU ---

    segmenty_kodu = []
    detale_budowy = []

    # 1. Typ Złącza 1 (T1, 3c)
    kod_zlacza_1, nazwa_zlacza_1 = drukuj_i_pobierz_kod_zlacza(1, '100', '143')
    segmenty_kodu.append(kod_zlacza_1)

    # 3. Orientacja Złącza 1 (O1, 2c)
    if kod_zlacza_1 == '000':
        kod_orientacji_1, nazwa_orientacji_1 = '---', 'POMINIĘTY (Brak Złącza 1)'
        print("\n--- KROK 3: Pomięty. Orientacja O1 NIE JEST dodawana do numeru. ---")
    else:
        kod_orientacji_1, nazwa_orientacji_1 = drukuj_i_pobierz_kod_prosty(
            3, "Orientacji Złącza 1", mapowanie_orientacji_do_wyboru, 2, "NAZWA ORIENTACJI"
        )
        segmenty_kodu.append(kod_orientacji_1)

    detale_budowy.append({'Pole': 'T1', 'Nazwa': 'Typ Złącza 1', 'Kod': kod_zlacza_1, 'PelnaNazwa': nazwa_zlacza_1})
    detale_budowy.append({'Pole': 'O1', 'Nazwa': 'Orientacja Złącza 1', 'Kod': kod_orientacji_1,
                          'PelnaNazwa': nazwa_orientacji_1 if kod_orientacji_1 != '---' else 'POMINIĘTY'})

    # 2. Typ Złącza 2 (T2, 3c)
    kod_zlacza_2, nazwa_zlacza_2 = drukuj_i_pobierz_kod_zlacza(2, '500', '543')
    segmenty_kodu.append(kod_zlacza_2)

    # 4. Orientacja Złącza 2 (O2, 2c)
    if kod_zlacza_2 == '000':
        kod_orientacji_2, nazwa_orientacji_2 = '---', 'POMINIĘTY (Brak Złącza 2)'
        print("\n--- KROK 4: Pomięty. Orientacja O2 NIE JEST dodawana do numeru. ---")
    else:
        kod_orientacji_2, nazwa_orientacji_2 = drukuj_i_pobierz_kod_prosty(
            4, "Orientacji Złącza 2", mapowanie_orientacji_do_wyboru, 2, "NAZWA ORIENTACJI"
        )
        segmenty_kodu.append(kod_orientacji_2)

    detale_budowy.append({'Pole': 'T2', 'Nazwa': 'Typ Złącza 2', 'Kod': kod_zlacza_2, 'PelnaNazwa': nazwa_zlacza_2})
    detale_budowy.append({'Pole': 'O2', 'Nazwa': 'Orientacja Złącza 2', 'Kod': kod_orientacji_2,
                          'PelnaNazwa': nazwa_orientacji_2 if kod_orientacji_2 != '---' else 'POMINIĘTY'})

    # 5. Typ Kabla (K, 2c)
    kod_kabla, nazwa_kabla = drukuj_i_pobierz_kod_prosty(
        5, "Typu Kabla", mapowanie_kabla, 2, "NAZWA KABLA"
    )

    # 6. Długość Kabla (D, 3c)
    if kod_kabla == '00':
        kod_dlugosci, nazwa_dlugosci = '---', 'POMINIĘTY (Brak Kabla)'
        print("\n--- KROK 6: Pomięty. Wybrano Brak Kabla (00). Segmenty K i D NIE SĄ dodawane do numeru. ---")
        # WAŻNE: W tym przypadku nie dodajemy K ani D, więc cofamy dodanie K, jeśli byłby wcześniej dodany.

        # Specjalna reguła: jeśli wybrano '00', to K = '00' ma być dodany, ale D ma być pominięty?
        # Zgodnie z intencją 'Brak kabla' pomija oba (K i D). Zostawiam K i D pominięte.

        # Jeśli K='00' ma się pojawić w numerze, należy to zrobić tutaj:
        # segmenty_kodu.append(kod_kabla)
        pass  # Oba segmenty (K i D) są pominięte w numerze
    else:
        # Dodajemy K do numeru
        segmenty_kodu.append(kod_kabla)

        kod_dlugosci, nazwa_dlugosci = drukuj_i_pobierz_kod_prosty(
            6, "Długości Kabla", mapowanie_dlugosci, 3, "DŁUGOŚĆ"
        )
        # Dodajemy D do numeru
        segmenty_kodu.append(kod_dlugosci)

    detale_budowy.append({'Pole': 'K', 'Nazwa': 'Typ Kabla', 'Kod': kod_kabla, 'PelnaNazwa': nazwa_kabla})
    detale_budowy.append({'Pole': 'D', 'Nazwa': 'Długość Kabla', 'Kod': kod_dlugosci, 'PelnaNazwa': nazwa_dlugosci})

    # --- GENEROWANIE NUMERU KATALOGOWEGO ---

    numer_katalogowy = "".join(segmenty_kodu)
    dlugosc_numeru = len(numer_katalogowy)

    # --- PODSUMOWANIE ---

    print("\n" + "=" * 70)
    print("### ✅ Zbudowany Numer Katalogowy Kabla:")
    print(f"**{numer_katalogowy}** ({dlugosc_numeru} cyfr)")
    print("=" * 70)
    print("\n**DETALE KONSTRUKCJI:**")
    print("| Pole | Nazwa | Kod | Czy dodano do Numeru? | Pełna Nazwa |")
    print("|:---:|:---:|:---:|:---:|:---:|")

    for detal in detale_budowy:
        kod_wyswietlany = detal['Kod']
        nazwa_wyswietlana = detal['PelnaNazwa']

        # Logika do kolumny 'Czy dodano do Numeru?'
        dodano = "NIE"
        if (detal['Pole'] == 'T1' or detal['Pole'] == 'T2'):
            dodano = "TAK"  # T1 i T2 są zawsze dodawane
        elif detal['Pole'] in ['O1', 'O2'] and detal['Kod'] != '---':
            dodano = "TAK"  # O1/O2 dodane, jeśli T != 000
        elif detal['Pole'] == 'K' and detal['Kod'] != '00':
            dodano = "TAK"  # K dodany, jeśli K != 00
        elif detal['Pole'] == 'D' and detal['Kod'] != '---':
            dodano = "TAK"  # D dodany, jeśli K != 00

        # Specjalne formatowanie dla opcji pominiętych/wyjątkowych
        if detal['Kod'] == '000' or detal['Kod'] == '00':
            print(
                f"| {detal['Pole']} | **{detal['Nazwa']}** | **{kod_wyswietlany}** | **{dodano}** | **{nazwa_wyswietlana}** |")
        elif detal['Kod'] == '---':
            print(f"| {detal['Pole']} | {detal['Nazwa']} | {kod_wyswietlany} | {dodano} | {nazwa_wyswietlana} |")
        else:
            print(f"| {detal['Pole']} | {detal['Nazwa']} | {kod_wyswietlany} | {dodano} | {nazwa_wyswietlana} |")

    print(f"\n**SEKWENCJA ZŁĄCZEŃ W NUMERZE:** (T1) (O1)* (T2) (O2)* (K)* (D)*")
    print(f"* Segmenty (O1, O2) są pomijane, jeśli T1 lub T2 = '000'.")
    print(f"* Segmenty (K, D) są pomijane, jeśli K = '00'.")
    print(f"**STRUKTURA KOŃCOWA:** {numer_katalogowy}")


# Uruchomienie programu
generuj_numer_katalogowy_finalny_v12()