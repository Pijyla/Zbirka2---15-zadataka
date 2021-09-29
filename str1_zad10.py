"""
Napisati kod koji za kvadratnu jednačinu ax2 + bx + c = 0 ispituje da li ima realna rješenja.
"""

import math

a = int(input('Unesite a: '))
b = int(input('Unesite b: '))
c = int(input('Unesite c: '))

# Računa se diskriminanta
d = b ** 2 - 4 * a * c

# Ispitujemo da li je vrijednost diskriminante veća od nule (tada ima 2 realna rješenja)

if d > 0:
    x1 = (- b + math.sqrt (d)) / 2 * a
    x2 = (- b - math.sqrt (d)) / 2 * a
    print ('Jednačina ima 2 realna rješenja pošto je d > 0 i iznosi: ', round(d, 2))
    print ('Prvo rješenje (x1) iznosi: ', round (x1, 2))
    print ('Drugo rješenje (x2) iznosi: ', round (x2, 2))
else:
    print ('Jednačina nema 2 realna rješenja jer je d < 0 ili je d = 0, d iznosi: ', round (d, 2))










