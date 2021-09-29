"""
Dat je cetvorocifreni prirodan broj. Ako su mu cifra jedinica i cifra hiljada jednake, 
stampati kvadrat dvocifrenog broja koji se dobije kada se uklone cifra jedinica i cifra hiljada.
Ako te dvije cifre nisu jednake stampati zbir kvadrata svih cifara.
"""

import math


uneseni_broj = int(input('Unesite cetvorocifreni broj '))

prva_cifra = uneseni_broj // 1000
#print (prva_cifra)
druga_cifra = (uneseni_broj // 100) % 10
#print (druga_cifra)
treca_cifra = (uneseni_broj // 10) % 10
#print (treca_cifra)
cetvrta_cifra = uneseni_broj % 10
#print (cetvrta_cifra)

dvocifren_broj = (uneseni_broj // 10) % 100
#print (dvocifren_broj)

kvadrat_dvocifrenog_broja = (dvocifren_broj)**2
#print (kvadrat_dvocifrenog_broja)

zbir_kvadrata_svih_cifara = (prva_cifra)**2 + (druga_cifra)**2 + (treca_cifra)**2 + (cetvrta_cifra)**2
#print (zbir_kvadrata_svih_cifara)

if prva_cifra == cetvrta_cifra:
    print (kvadrat_dvocifrenog_broja)
else:
    print (zbir_kvadrata_svih_cifara)
