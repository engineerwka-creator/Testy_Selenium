# #Napisz program, który po wczytaniu trzech liczb całkowitych, wypisze największą.
# from Assert_Add_Pytest import divide
# from Lista_Krotki_Słownik_Zbiór import wynik
#
# liczby = (12, 8, 100)
# print (max(liczby))
# print (min(liczby))
# #-----------------------------------------------------------------------------------
# # Napisz program, który wczyta n liczb i obliczy ich sumę.
#
# import random
#
# def suma():
#     ilosc = int(input('Podaj ilość liczb do wylosowania: '))
#     n_liczba = [2, 4, 5, 6, 8, 9, 12, 14, 18, 22, 25, 27, 29, 34, 56]
#
#     wylosowane = random.sample(n_liczba, ilosc)
#     print("Wylosowane liczby:", wylosowane)
#
#     wynik = sum(wylosowane)
#     print("Suma liczb:", wynik)
#
# suma()
#
# #-----------------------------------------------------------------------------------
#
# x = [2, 4, 5, 6, 8, 9, 12, 14, 18, 22, 25, 27, 29, 34, 56]
# y = [2, 4, 5, 6, 0, 9, 2, 14, 8, 12, 45, 37, 19, 24, 36]
#
# for element in x:
#     if element in y:
#         print ('Mamy to:' , element)
#
# #-----------------------------------------------------------------------------------
# # Napisz program, który wczyta podaną liczbe "liczb" i obliczy ich sumę.
# import random
#
# digit = [2, 4, 5, 6, 8, 9, 12, 14, 18, 22, 25, 27, 29, 34, 56]
#
# wylosowane = int(input('Podaj ilość liczb:  '))
#
# losuj = random.sample(digit, wylosowane)
#
# suma = sum(losuj)
#
# print (losuj)
# print (suma)

# #-----------------------------------------------------------------------------------
#Napisz program, wczyta liczbę wierszy oraz liczbę kolumn i na podstawie tych wartości wygeneruje na ekranie prostokąt złożony z gwiazdek.
#
# szerokość = 20
# długość = 10
#
# for i in range(długość):
#     if i == 0 or i == długość -1:
#         print('*' * szerokość)
#     else:
#         print('*' + ' ' * (szerokość - 2) + '*')
#
#
# szerokość = 20
# długość = 10
#
# for i in range(długość):
#     if i == 0 or i == długość -5:
#         print('*' * szerokość)
#     elif i == 0 or i == długość -1:
#         print ('*' * szerokość)
#     else:
#         print('*' + ' ' * (szerokość - 2) + '*')

#----------------------------------------------------------------

# bok = 10
# i = 1

# while i <= bok:
#     print('*' * i)
#     i = i + 1
#
# i = 10 - 1
#
# while i >= 1:
#     print('*' * i)
#     i = i - 1
#
# for i in range(1, bok):
#      print ('*' * i)

# for i in range(1, bok):
#     spacja = ' ' * (bok -i)
#     gwiazdki = '*' * (2 * i -1)
#     print (spacja + gwiazdki)


# bok = 10  # długość prostokąta
# wysokosc = 5
#
# for i in range(wysokosc):
#     if i == 0 or i == wysokosc - 1:
#         print('*' * bok)  # górna i dolna linia
#     else:
#         print('*' + ' ' * (bok - 2) + '*')  # środek

#----------------------------------------------------------------
# Napisz program, który będzie wczytywał liczby całkowite do momentu wczytania liczby dwa poraz trzeci.

# logs_a = (1,2,3,4,5,6,7,8,9)
# logs_b = (10,11,12,13,14,15,16,17,18,19)
# logs_c = (2,9,1,8,3,7,6,5,2,5,4,3,9,0,20)
#
# logs_all = logs_a + logs_b + logs_c
#
# count = 0
# for x in logs_all:
#     if x == 2:
#         count += 1
#     if count == 3:
#         print('Liczba 2 pojawiła się trzeci raz')
#         break

#----------------------------------------------------------------
# Napisz program, który będzie wczytywał nazwiska do momentu wczytania nazwiska poraz drugi.

# klasa_1 = ('bambik', 'jury', 'rambo', 'nowak', 'kalisz', 'malina')
# klasa_2 = ('rony', 'bajek', 'dycha', 'kafel', 'maniek', 'ryś','bambik')
# klasa_3 = ('stachu', 'koral', 'calina', 'klama', 'bambik')
#
# klasa_all = klasa_1 + klasa_2 + klasa_3
#
# widziane = set()
# powtorzenia = set()
#
# for z in klasa_all:
#     if z in widziane:
#         powtorzenia.add(z)
#     else:
#         widziane.add(z)
#
# print("Powtarzające się imiona:", powtorzenia)
# print("Liczba powtórzeń:", len(powtorzenia))
#
# #---------------------------------------------------------------
# from collections import Counter
#
# zbior = (1,2,2,3,4,5,6,2,7,8,2,9)
#
# licznik = Counter(zbior)
#
# for liczba, policz in licznik.items():
#     if policz > 3:
#         print (f'w zbiorze mamy trzy takie same liczby: {liczba}')
# #-------------------------------------------------------------------
# Napisz program, który wczyta dwie liczby a i b i następnie wypisze wszystkie liczby z przedziału
#a <= b
# """a,b,a + 1, b -1, a + 2, b -2"""
# a = 2
# b = 4
#
# x = a,b,a +1
# y = b -1
# z = a + 2
# w = b -2
#
# q = a,b,a +1, b -1, a + 2, b -2
# print (q)

# #-------------------------------------------------------------------
#Napisz program, który po wczytaniu zdania zamieni wszystkie litery na duże.
# x = 'Ala ma kota'
# o = x.upper()
#
# print (o)

# #-------------------------------------------------------------------
# Napisz program, który policzy liczbę wystąpień frazy "oko" w zadanym tekście.
#
# a = 'otookokookotookooko'
#
# licznik = a.count('oko')
# print (licznik)

## ------------------------------------------------------------------------
