"""
Dat je cetvorocifeni prirodni broj. Napisati kod koji stampa zbir kvadrata cifara tog broja.
"""

uneseni_broj = int(input('Unesite cetvorocifreni broj '))

prva_cifra = uneseni_broj // 1000
#print (prva_cifra)
druga_cifra = (uneseni_broj // 100) % 10
#print (druga_cifra)
treca_cifra = (uneseni_broj // 10) % 10
#print (treca_cifra)
cetvrta_cifra = uneseni_broj % 10
#print (cetvrta_cifra)

zbir_kvadrata_svih_cifara = (prva_cifra)**2 + (druga_cifra)**2 + (treca_cifra)**2 + (cetvrta_cifra)**2
print (zbir_kvadrata_svih_cifara)
