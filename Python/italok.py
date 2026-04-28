def liter_ossz(mertek):
    liter = mertek // 100
    cl = mertek - liter * 100
    return str(liter) + ' liter ' + str(cl) + ' centiliter'

for i in range(3):
    nev = input('Add meg az ital nevét! ')
    mennyiseg = int(input('Mennyi van belőle? '))
    print(nev, ':', liter_ossz(mennyiseg))

