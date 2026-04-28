elso = int(input('Adj meg a számot! '))
print('A beadott szám:', elso)
if (elso%3!=0) and (elso%5!=0):
    print('A szám nem osztható sem 3-mal sem 5-tel.')
if (elso%3==0):
    print('A szám osztható 3-mal.')
if (elso%5==0):
    print('A szám osztható 5-tel.')
