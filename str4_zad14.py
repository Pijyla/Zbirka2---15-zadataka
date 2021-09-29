"""
Dat je trocifren broj. Odrediti broj koji se dobija zamjenom prve i poslednje cifre.
"""

uneseni_trocifreni_broj = int(input('Unesite trocifren broj '))

prva_cifra = uneseni_trocifreni_broj // 100
druga_cifra = (uneseni_trocifreni_broj // 10) % 10
treca_cifra = uneseni_trocifreni_broj % 10

cuvar_vrijednosti_prve_cifre = prva_cifra

prva_cifra = treca_cifra
treca_cifra = cuvar_vrijednosti_prve_cifre

novi_trocifreni_broj = (prva_cifra * 100) + (druga_cifra * 10) + treca_cifra
print(novi_trocifreni_broj)

