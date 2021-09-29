"""
Za prirodan broj k stampati frazu "Na izletu smo ubrali k pecuraka", gdje zavrsetak rijeci "pecurka" prilagodite broju k.
Npr. 101 pecurku, 1204 pecurke, 506 pecuraka.
"""

broj_ubratih_pecurki = int(input('Unesite broj ubratih pecurki: '))

zadnja_cifra_broja_ubratih_pecurki = broj_ubratih_pecurki % 10
#print (zadnja_cifra_broja_ubratih_pecurki)

if zadnja_cifra_broja_ubratih_pecurki == 1:
    print (broj_ubratih_pecurki, "pecurku")
elif broj_ubratih_pecurki < 10 and zadnja_cifra_broja_ubratih_pecurki < 5:
    print (broj_ubratih_pecurki, "pecurke")
elif broj_ubratih_pecurki > 20 and zadnja_cifra_broja_ubratih_pecurki < 5:
    print (broj_ubratih_pecurki, "pecurke")
else:
    print (broj_ubratih_pecurki, "pecuraka")
