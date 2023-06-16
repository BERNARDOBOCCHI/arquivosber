###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Eleições 2022
# Nome:Bernardo Bocchi
# RA:260376
###################################################

# Leitura de dados
a=input()
votados=[]
votos={}
Brancos=0
Nulos=0
while a!="0" :
    #print(a,"ola")
    if a=="Branco":
        Brancos+= 1
    elif a=="Nulo":
        Nulos+=1
    elif a not in votos:
        votados.append(a)
        votos[a]=1
    elif a in votos:
        votos[a]+=1
    a=input()
    #print(a,'oi')
#print("fimm")
#print(votos)
listavotos={}
listanumeros=[]
#print(votados)
for nome in votados:
    listavotos[votos[nome]]=nome
    listanumeros.append(votos[nome])
#print(listanumeros.sort(reverse=True))
listanumeros.sort(reverse=True)
for numero in listanumeros:
    print(listavotos[numero],numero)
print('Brancos',Brancos)
print('Nulos',Nulos)


        

# Saída de dados