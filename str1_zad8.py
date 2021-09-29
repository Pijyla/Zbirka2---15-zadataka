"""
Napisati kod koji učitava 2 cijela broja m i n i štampa poruku "m je djeljivo sa n" ili "m nije djeljivo sa n". 
Npr. "15 je djeljiv sa 3" ili "15 nije djeljiv sa 4".
"""

m = int(input('Unesite prvi broj '))
n = int(input('Unesite drugi broj '))

if m % n == 0:
    print (m, 'je djeljiv sa ', n)
else:
    print (m, 'nije djeljiv sa ', n)

