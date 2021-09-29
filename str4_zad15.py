"""
Dat je cetvorocifren broj. Odrediti broj koji se dobija zamjenom trece i druge cifre.
Npr. od 5804 dobija se 5084.
"""

uneseni_cetvorocifreni_broj = int(input('Unesite cetvorocifren broj '))

prva_cifra = uneseni_cetvorocifreni_broj // 1000
druga_cifra = (uneseni_cetvorocifreni_broj // 100) % 10
treca_cifra = (uneseni_cetvorocifreni_broj // 10) % 10
cetvrta_cifra = uneseni_cetvorocifreni_broj % 10

cuvar_vrijednosti_druge_cifre = druga_cifra

druga_cifra = treca_cifra
treca_cifra = cuvar_vrijednosti_druge_cifre

novi_cetvorocifreni_broj = (prva_cifra * 1000) + (druga_cifra * 100) + (treca_cifra * 10) + cetvrta_cifra
print(novi_cetvorocifreni_broj)
