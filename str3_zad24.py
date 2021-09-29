"""
Napisati kod koji za datu godinu odredjuje da li je prestupna i stampa odgovarajucu poruku.
"""

unesena_godina = int(input('Unesite godinu '))

if unesena_godina % 4 == 0:
    if unesena_godina % 100 != 0:
        print ('Prestupna godina.')
    elif unesena_godina % 400 == 0:
        print ('Prestupna godina.')
    else:
        print ('Nije prestupna godina.')
else:
    print ('Nije prestupna godina.')

