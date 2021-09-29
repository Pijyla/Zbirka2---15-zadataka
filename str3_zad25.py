"""
Napisati kod koji za dati redni broj mjeseca (od 1 do 12) i datu godinu stampa broj dana u datom mjesecu.
"""

uneseni_broj_za_mjesec = int(input('Unesite broj od 1 do 12 za mjesec (1 za januar, 12 za decembar): '))
unesena_godina = int(input('Unesite godinu: '))

if uneseni_broj_za_mjesec == 1:
    print('31 dan')
if uneseni_broj_za_mjesec == 2:
    if unesena_godina % 4 == 0:
        if unesena_godina % 100 != 0:
            print ('29 dana')
        elif unesena_godina % 400 == 0:
            print ('29 dana')
        else:
            print ('28 dana')
    else:
        print ('28 dana')
if uneseni_broj_za_mjesec == 3:
    print ('31 dan')
if uneseni_broj_za_mjesec == 4:
    print ('30 dana')
if uneseni_broj_za_mjesec == 5:
    print ('31 dan')
if uneseni_broj_za_mjesec == 6:
    print ('30 dana')
if uneseni_broj_za_mjesec == 7:
    print ('31 dan')
if uneseni_broj_za_mjesec == 8:
    print ('31 dan')
if uneseni_broj_za_mjesec == 9:
    print ('30 dana')
if uneseni_broj_za_mjesec == 10:
    print ('31 dan')
if uneseni_broj_za_mjesec == 11:
    print ('30 dana')
if uneseni_broj_za_mjesec == 12:
    print ('31 dan')



