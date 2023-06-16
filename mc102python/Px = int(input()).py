
Py = int(input())
peca = []
for _ in range(Py):
  peca.append(input().split())
Px=len(peca[0])
#print(Py,Px)
if Py<Px:
    P=Px
    peca.append([0]*(Py-Px))
    #print('oi')
if Py>Px:
    P=Py
    #print('la')
    #print(len(peca[Py-1]))
    while len(peca[Py-1])<Py:
        for x in peca:
            #print(x)
            x.append(0)
            #print('oioi')
#print(peca)


i=0
j=0
from copy import deepcopy
pecado=deepcopy(peca)
#print(peca)
#print(pecado)
while i<P:
    while j<P:
        #print(i,j)
        #print(Px-1-j,Py-1-i)
        #print("não é pra mudar",peca)
        #print(pecado)
        pecado[j][i]=peca[Py-1-i][j]
        #print(peca)
        #print (pecado[i][j])
        
        j+=1
    j=0
    i+=1
#print(pecado)
for lista in pecado:
    while lista.count(0)>0:
        lista.remove(0)
while pecado.count([]):
    pecado.remove([])
print(pecado)
