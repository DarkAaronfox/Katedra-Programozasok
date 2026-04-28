elso = int(input('Adj meg egy számot! '))
print('A beadott szám:', elso)
if(elso%7!=0) and (elso%11!=0):
    print('A szám nem osztható sem 7-el sem 11-el.')
if(elso%7==0):
    print('A szám osztható 7-el.')
if(elso%11==0):
    print('A szám osztható 11-el.')
