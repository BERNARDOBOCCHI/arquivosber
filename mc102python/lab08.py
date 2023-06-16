###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: Bernardo Bocchi
# RA: 260376
###################################################
palavra  =list( input())
palavra1="0"
strpalavra="".join(palavra)
i=0
l=len(palavra)
strpalavra1="0"
k=6
while strpalavra1!=strpalavra.upper() and k>0:
    palavra1= list(input())    
    
    while i<l :
        print(i,l)
        if palavra[i]==palavra1[i]: 
            #print("cristorei")
            palavra1[i]=palavra1[i].upper()
            #print(palavra1)
        elif palavra1[i] in palavra:
            palavra1[i]=palavra1[i]
        elif palavra[i]!=palavra1[i]:
            palavra1[i]="_"
        elif palavra1[i] in palavra:
            palavra1[i]=palavra1[i]
        i+=1
    i=0    
    k-=1
    strpalavra1="".join(palavra1)
    print(strpalavra1)
    print("oi")
    print(strpalavra,strpalavra1)
    #print(k)
strpalavra1="".join(palavra1)
print(strpalavra1,2)

if strpalavra.upper()==palavra1:


# Impressão da linha final
# ...
    print("Resposta correta")
elif strpalavra1!=strpalavra.upper:
    print("Palavra correta:", strpalavra)
