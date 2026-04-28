import operator

class aruk:
    def __init__(self, nev, ar):
        self.nev = nev
        self.ar = int(ar)

aru = []
szum = 0
fbe=open('bolt.txt', 'r')
print('A fájl tartama:')
for sor in fbe:
    sor=sor.strip().split(' ')
    aru.append(aruk(sor[0],sor[1]))
    print(sor[0],sor[1],'Ft',sep=' ')
    szum=szum+int(sor[1])
fbe.close()

print('Az áruk átlagos ára:',round(szum/len(aru),1),'Ft')

aru.sort(key=operator.attrgetter('ar'),reverse=True)

print('A legdrágább árú adatai:',aru[0].nev,aru[0].ar,'Ft')

fki=open('legdragabb.txt','w')
print('A legdrágább áru adatai:',aru[0].nev,aru[0].ar,'Ft',file=fki)
fki.close()
