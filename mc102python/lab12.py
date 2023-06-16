###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Redimensionamento de Imagens
# Nome: Bernardo Boçchi
# RA: 260376
###################################################

def imprimir_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(int(x)) for x in imagem[i]))

def expansao(imagem_original):
    #etapa1
    print('ieieie')
    ie=0
    je=0
    while ie<n:
        print(n)
        while je<m-1:
            print(ie,je,n,m)
            imagem_original[ie].insert(2*je+1,(imagem_original[ie][2*je]+imagem_original[ie][2*je+1])//2)
            print(imagem_original)
            je+=1
            print(ie,je)
        je=0
        ie+=1
    print('olá')
    #etapa2
    Ie=0
    Je=0
    while Ie<n-1:
        imagem_original.insert(2*Ie+1,[])
        while Je<=(n//2)+1:
            print(Ie,Je,n,m)
            imagem_original[2*Ie+1].append((imagem_original[2*Ie][Je*2]+imagem_original[2*Ie+2][Je*2])//2)
            print(imagem_original[2*Ie+1])
            Je+=1
        Je=0
        Ie+=1
    #etapa3
    ief=1
    jef=0
    while ief<=n//2:
        while jef<m-1:
            imagem_original[ief+1].insert(jef+1,(imagem_original[ief][jef]+imagem_original[ief][jef+1]+imagem_original[ief+2][jef]+imagem_original[ief+2][jef+1])//4)
            jef+=1
            print(ief,jef,n,m)
            print(imagem_original)
        jef=0
        ief+=2
    #etapa4
        
    imagem=imagem_original
    return(imagem)

def retracao(imagem_original,n,m):
    from copy import deepcopy
    imagem=deepcopy(imagem_original)
    I=0
    J=0
    while I<n//2:
        while J<m//2:
            imagem[I][J]=(imagem_original[2*I][2*J]+imagem_original[2*I+1][2*J]+imagem_original[2*I][2*J+1]+imagem_original[2*I+1][2*J+1])//4
            J+=1
        I+=1
    print('olá')
    if n/2 is not int and m/2 is not int:
        imagem[n//2][m//2]=imagem_original[n-1][m-1]
    if n/2 is not int:
        while J<m//2: imagem[n//2][J]=(imagem_original[n//2][J]+imagem_original[n//2][J+1])//2
    if m/2 is not int:
        while I<n//2: imagem[I][m//2]=(imagem_original[I][m//2]+imagem_original[I+1][m//2])//2
    return imagem
# leitura da imagem
o= input() #P2 - linha a ser ignorada

m, n = [int(x) for x in input().split()]
print (m,n)
o= input() #255 - linha a ser ignorada
o=False
imagem_original = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem_original.append(linha)
print ("oi")
# leitura do tipo de redimensionamento
tipodeprocessamento=input()
print('vaicarai')
if tipodeprocessamento=="retração":
    print('retraça')
    imagem=retracao(imagem_original,n,m)
    print('oi')
if tipodeprocessamento=="expansao":
    print('spand')
    imagem=expansao(imagem_original)
    print('oi')
# impressão da imagem final
imprimir_imagem(imagem)
