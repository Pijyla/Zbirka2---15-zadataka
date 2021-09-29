"""
Napisati kod koji provjerava da li je zbir cifara datog trocifrenog broja dvocifren broj.
"""

uneseni_broj = int(input('Unesite trocifreni broj '))

prva_cifra = uneseni_broj // 100
#print (prva_cifra)
druga_cifra = (uneseni_broj // 10) % 10
#print (druga_cifra)
treca_cifra = uneseni_broj % 10
#print (treca_cifra)

# Sabiraju se sve cifre trocifrenog broja
suma_svih_cifara_broja = prva_cifra + druga_cifra + treca_cifra

# Ispituje se da li je zbir cifara dvocifren broj
if suma_svih_cifara_broja > 9:
    if suma_svih_cifara_broja < 100:
        print ('Dvocifren broj.')
else:
    print ('Nije dvocifren broj.')
