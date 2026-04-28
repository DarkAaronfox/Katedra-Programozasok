def deka(tomeg):
    dkg = tomeg // 10
    g = tomeg - dkg * 10
    return str(dkg) + ' dekagramm ' + str(g) + ' gramm'

for i in range(3):
    név = input('Add meg a zöldség nevét! ')
    súly = int(input('Mennyi a súlya? '))
    print('A(z)', név, deka(súly), 'súlyú.')
