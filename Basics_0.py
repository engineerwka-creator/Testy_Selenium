#---------------------------------------------------------------------------------------
Przykładowe typy zmiennych:

Liczby całkowite (int)
wiek = 25
temperatura = -3

Liczby zmiennoprzecinkowe (float)
waga = 72.5
cena = 19.99

Tekst - String (str)
imie = "Ola"
powitanie = 'Cześć!'

Wartości logiczne (bool)
czy_student = True
czy_pada = False
#---------------------------------------------------------------------------------------
Listy (list) (zbiór wielu wartości, które można dowolnie rozszerzać lub zmniejszać)
liczby = [1, 2, 3, 4]
imiona = ["Ala", "Bartek", "Celina"]

Krotki (tuple) - nie możemy ich modyfikować
koordynaty = (108, 320)

Słowniki (dict) == (para to - klucz: wartość)
osoba = {"imie": "Ola", "wiek": 25}

Zbiory (set) - możemy dodawać lub wyjmować ze zbiorów, przy czym nie mogą się powtarzać obiekty.
liczby = {1, 2, 3, 4}

| Typ danych  | Składnia           | Kolejność                    | Zmiana wartości | Duplikaty                   | Przykład                           |
| ----------- | ------------------ | ---------------------------- | --------------- | --------------------------- | ---------------------------------- |
| **Lista**   | `[]`               | ✅ Tak                        | ✅ Tak           | ✅ Tak                       | `owoce = ["jabłko", "banan"]`      |
| **Krotka**  | `()`               | ✅ Tak                        | ❌ Nie           | ✅ Tak                       | `kolory = ("czerwony", "zielony")` |
| **Słownik** | `{klucz: wartość}` | ❌ (od Pythona 3.7 zachowana) | ✅ Tak           | ❌ Klucze muszą być unikalne | `osoba = {"imię": "Amelka"}`       |
| **Zbiór**   | `{}`               | ❌ Nie                        | ✅ Tak           | ❌ Nie                       | `liczby = {1, 2, 3}`               |

#---------------------------------------------------------------------------------------

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

b = [11, 12, 13, 14, 15, 16,17, 18, 19]

a.append('Jaga')                    #wstawia liczbę lub tekst na końcu listy
a.insert(5, 99)      #wstawia w konkretnie wskazanym miejscu liczbę lub tekst
a.extend('ZMARTWYCHWSTANIE')        #wstawia tekst lub liczbę (tylko jako string) i po przecinku rozbija każdą cyfrę lub literę na końcu listy.
a.pop (10)                          #usuwa poszczególne pozycje, przy czym licząc od 0, 1, itd.
b.remove(19)                        #usuwa dowolnie wskazaną pozycję

print (a)
print (b)
#---------------------------------------------------------------------------------------

| Metoda         | Zachodzące wzorce | Łatwość | Najlepsze do               |
| -------------- | ----------------- | ------- | -------------------------- |
| `.count()`     | ❌                 | ✅✅✅     | szybkie, proste liczenie   |
| `find()`       | ✅                 | ✅✅      | ręczna kontrola pozycji    |
| `re.findall()` | ✅                 | ✅✅      | złożone wzorce, regex      |
| `Counter()`    | ❌                 | ✅✅      | liczenie liter, fragmentów |
| `split()`      | ❌                 | ✅       | proste dzielenie tekstu    |

#---------------------------------------------------------------------------------------
#Obliczamy resztę z dzielenia:
a = 6
b = 3
print (a % b) #0

c = 5
d = 2
print (c % d) #1

#Wskazujemy na typy liczb int (4) czy float (4.0).

print (type (a + b)) #int
print (type (a - b)) #int
print (type (a * b)) #int
print (type (a / b)) #float

#---------------------------------------------------------------------------------------

Przykładowe warunki (instrukcje):

if (jeśli): Python sprawdza pierwszy warunek. Jeśli warunek jest prawdziwy (True), wykonuje blok kodu znajdujący się pod if.

elif (w przeciwnym razie, jeśli): Jeśli warunek if był fałszywy, Python sprawdza pierwszy warunek elif. Jeśli jest on prawdziwy, wykonuje jego blok kodu i pomija resztę.

else (w przeciwnym razie): Jeśli żaden z poprzednich warunków if lub elif nie był prawdziwy, wykonywany jest blok kodu znajdujący się pod else.
#----------------------------------------------------------------------------------------

używaj print() – gdy chcesz zobaczyć wynik,

używaj return – gdy chcesz dalej pracować z wynikiem (np. użyć go w obliczeniach).

#----------------------------------------------------------------------------------------------

def przywitaj():
    print("Cześć!")
przywitaj()


def ...: → tworzy funkcję (definicja)
przywitaj() → uruchamia funkcję (wywołanie)

#Dlaczego w ogóle tworzymy funkcje? Bo funkcje pozwalają:

#Unikać powtórzeń — zamiast pisać 10 razy ten sam kod, piszesz go raz i wywołujesz wielokrotnie.
#Porządkować kod — dzielisz program na logiczne części.
#Łatwiej wprowadzać zmiany — poprawiasz coś raz, a działa wszędzie.
#Wykorzystywać dane — możesz przekazywać różne argumenty (np. różne ceny).

def nazwa_funkcji(argumenty):
    # ciało funkcji
    instrukcje
    return wynik
#----------------------------------------------------------------------------------------------
#Przykład z Argumentem (imie)
def przywitaj(imie):
    print(f"Cześć, {imie}!")

przywitaj('Karol')
przywitaj('Kate')
#Argumenty dodajesz wtedy, gdy chcesz, by funkcja działała na różnych danych!

#Przykład Bez Argumentu ()
def powitanie():
    print("Cześć wszystkim!")

powitanie()
#Gdy funkcja robi zawsze to samo, argumenty nie są potrzebne!

#----------------------------------------------------------------------------------------------
 assert służy do sprawdzenia, czy coś jest prawdą (czyli czy jakiś warunek zwraca True).
 Jeśli warunek jest prawdziwy, program działa dalej.
 Jeśli nie jest prawdziwy, Python zatrzymuje program i zgłasza błąd AssertionError.


def test_add():
    assert add(3, 5) == 15
    assert add(-1, 1) == -1
    assert add(0, 0) == 0
    assert add(5, 5) == 25

#----------------------------------------------------------------------------------------------
@Dekorator w Pythonie to funkcja, która modyfikuje działanie innej funkcji —
bez konieczności zmieniania jej kodu. Dekorator „owija” funkcję, dodając jej nowe możliwości.
Używa się go ze specjalnym symbolem @ umieszczonym nad definicją funkcji.

def log_decorator(func):
    def wrapper():
        print("➡️ Funkcja się zaraz wykona...")
        func()
        print("✅ Funkcja zakończyła działanie.")
    return wrapper

@log_decorator
def say_hello():
    print("Cześć!")

say_hello()

Co się dzieje:
@log_decorator to dekorator, który „opakowuje” funkcję say_hello.
Kiedy wywołujesz say_hello(), naprawdę wykonuje się wrapper() z dekoratora.
Dzięki temu można dodać nową funkcjonalność (np. logowanie) bez zmiany oryginalnej funkcji.


| Termin                | Znaczenie                                                       |
| --------------------- | --------------------------------------------------------------- |
| **Dekorator**         | Funkcja, która modyfikuje działanie innej funkcji               |
| **`@pytest.fixture`** | Dekorator z `pytest`, który tworzy funkcję pomocniczą (fixture) |
| **Cel dekoratorów**   | Dodanie logiki przed/po wywołaniu funkcji, bez zmiany jej kodu  |

#----------------------------------------------------------------------------------------------
*args → pozwala przekazać dowolną liczbę argumentów pozycyjnych (czyli takich bez nazw).

def suma(*args):
    print(args)
    return sum(args)

print(suma(1, 2, 3, 4, 5, 6))
print(suma(10, 20))

**kwargs → pozwala przekazać dowolną liczbę argumentów nazwanych (czyli takich z nazwami, np. x=5).

kwargs = {'name': 'Ala', 'age': 25, 'city': 'Warszawa'}

for (key, value) in kwargs.items():
    print(f"{key} = {value}")

#----------------------------------------------------------------------------------------------
