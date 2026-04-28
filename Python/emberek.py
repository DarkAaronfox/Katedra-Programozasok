def meter(magasság):
    m = magasság // 100
    cm = magasság - m * 100
    return str(m) + ' méter ' + str(cm) + ' centiméter'

for i in range(3):
    név = input('Add meg a játékos nevét! ')
    height = int(input('Mennyi a magassága? '))
    print(név, meter(height), 'magas.')
