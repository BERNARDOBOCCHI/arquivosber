##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome: Bernardo Bocchi
# RA: 260376
##################################################
torre = [int(panqueca) for panqueca in input().split()]
torre.insert(0,0)
#print(torre)
# Leitura e processamento dos movimentos
i="okaido"
while i!=0:
    i=int(input())
    torre[1:i+1]=torre[i:0:-1]
k=0
#print(torre)
#print(len(torre))
while k<len(torre)-2 and torre[k]<=torre[k+1]:
    k+=1
    #print(k)
if k<len(torre)-2: print("Torre instavel")
else: print("Torre estavel")
#Impressão da saída
