"""
Date su 2 promjenljive x i y istog tipa. Napisati kod koji mijenja mjesta vrijednostima u promjenljivim x i y.
Npr. ako je x = 5 i y = 10, nakon izvrsavanja koda treba da bude x = 10 i y = 5.
"""

x = int(input('Unesite vrijednost za x '))
y = int(input('Unesite vrijednost za y '))


# Zamjena vrijednosti promjenljivih pomocu ugradjene Python funkcije
#x, y = y, x
#print (x, y)

# Zamjena vrijednosti promjenljivih pomocu pomocne promjenljive z 
# (z cuva vrijednost promjenljive x, dok se ona ne dodijeli promjenljivoj y)

z = x
x = y 
y = z
print(x, y)



