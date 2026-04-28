elso = int(input('Adj meg egy számot! '))
print('A beadott szám:', elso)
if(elso%3!=0) and (elso%11!=2):
    print('A szám nem osztható sem 3-mal sem 2-vel.')
if(elso%3==0):
    print('A szám osztható 3-mal.')
if(elso%2==0):
    print('A szám osztható 2-vel.')
