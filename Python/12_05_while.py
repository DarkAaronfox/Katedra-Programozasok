szam = 1
while szam <= 10:
    print(szam)
    szam = szam + 1

szamlalo = 1
while szamlalo <= 5:
    print('Programozni jó!')
    szamlalo = szamlalo + 1

folytatja = True
while folytatja:
    print('Vidd ki a szemetet!')
    valasz = input('Mondjam még egyszer? (i/n)')
    if valasz == 'n':
        folytatja = False
print('>> Program vége! <<')

# 0 -> 9
for i in range(10):
    print(i)
# 5 -> 8
for i in range(5,9):
    print(i)
# 3 -> 20-ig 6-osával
for i in range(3,21,6):
    print(i)
 
szavak = ['lámpa', 'ablak', 'kutya', 'Attila', 'kukta']
for szo in szavak:
    print(szo)
    
for karakter in 'almafa':
    print(karakter)
