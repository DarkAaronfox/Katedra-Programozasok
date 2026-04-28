def percms(másodpercek):
    perc = másodpercek // 60
    ms = másodpercek - perc * 60
    return str(perc) + ' perc ' + str(ms) + ' másodperc'

for i in range(3):
    cím = input('Add meg egy zene címét! ')
    hossz = int(input('Hány másodperc a zene? '))
    print('A(z)', cím, 'című zene', percms(hossz), 'hosszú.')
