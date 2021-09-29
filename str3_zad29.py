"""
Data su 3 cijela broja A, B i C. Odrediti da li medju njima ima bar jedan paran broj i bar jedan neparan broj.
Ulaz: Prvi red ulaza sadrzi 3 cijela broja A, B i C (1 <= A <= 1000).
Izlaz: Stampati "YES" ili "NO".
"""

uneseni_broj_A = int(input('Unesite prvi broj '))
uneseni_broj_B = int(input('Unesite drugi broj '))
uneseni_broj_C = int(input('Unesite treci broj '))

if uneseni_broj_A % 2 == 0 or uneseni_broj_B % 2 == 0 or uneseni_broj_C % 2 == 0:
    if uneseni_broj_A % 2 != 0 or uneseni_broj_B % 2 != 0 or uneseni_broj_C % 2 != 0:
        print (True)
    else:
        print(False)
else:
    print(False)
