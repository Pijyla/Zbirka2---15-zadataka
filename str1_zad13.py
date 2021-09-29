"""
Dat je četvorocifreni prirodan broj abcd. Štampati poruku "Super" ako vazi a * c = b * d.
"""

uneseni_broj = int(input('Unesite cetvorocifreni broj '))

prva_cifra = uneseni_broj // 1000
#print (prva_cifra)
druga_cifra = (uneseni_broj // 100) % 10
#print (druga_cifra)
treca_cifra = (uneseni_broj // 10) % 10
#print (treca_cifra)
cetvrta_cifra = uneseni_broj % 10

if prva_cifra * treca_cifra == druga_cifra * cetvrta_cifra:
    print ('Super')
    