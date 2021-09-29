"""
Napisati kod koji izracunava vrijednos funkcije.
"""
x = int(input('Unesite vrijednost za x '))

a = - 2 * (x)**2
b = (2 * x) + 5

import math

if x <= 0:
    y = ((2 * a) + 7) / 2
    print (y)
else:
    y = math.sin (b)
    print (y)

