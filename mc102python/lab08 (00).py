###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: 
# RA: 
###################################################

# Leitura da palavra
palavra  =list( input())
palavra1  =list( input())
palavra2 = list(input())
palavra3 = list(input())
palavra4 = list(input())
palavra5 = list(input())
palavra6 = list(input())
l=len(palavra)
i=0
#print(palavra[0].upper())
while i<l :
    if palavra[i]==palavra1[i]: 
        #print("cristorei")
        palavra1[i]=palavra1[i].upper()
        #print(palavra1)
    elif palavra[i]!=palavra1[i]:
        palavra1[i]="_"
    elif palavra1[i] in palavra:
        palavra1[i]=palavra1[i]
    i+=1
l=len(palavra)
i=0
while i<l :
    if palavra[i]==palavra2[i]: 
        #print("cristorei")
        palavra2[i]=palavra2[i].upper()
        #print(palavra2)
    elif palavra[i]!=palavra2[i]:
        palavra2[i]="_"
    elif palavra2[i] in palavra:
        palavra2[i]=palavra2[i]
    i+=1
l=len(palavra)
i=0

while i<l :
    if palavra[i]==palavra3[i]: 
        #print("cristorei")
        palavra3[i]=palavra3[i].upper()
        #print(palavra3)
    elif palavra[i]!=palavra3[i]:
        palavra3[i]="_"
    elif palavra3[i] in palavra:
        palavra3[i]=palavra3[i]
    i+=1
    
    l=len(palavra)
    i=0

while i<l :
    if palavra[i]==palavra4[i]: 
        #print("cristorei")
        palavra4[i]=palavra4[i].upper()
        #print(palavra4)
    elif palavra[i]!=palavra4[i]:
        palavra4[i]="_"
    elif palavra4[i] in palavra:
        palavra4[i]=palavra4[i]
    i+=1
l=len(palavra)
i=0

while i<l :
    if palavra[i]==palavra5[i]: 
        #print("cristorei")
        palavra5[i]=palavra5[i].upper()
        #print(palavra5)
    elif palavra[i]!=palavra5[i]:
            palavra5[i]="_"
    elif palavra5[i] in palavra:
            palavra5[i]=palavra5[i]
    i+=1
    print("".join(palavra6))
    l=len(palavra)
    i=0

while i<l :
    if palavra[i]==palavra6[i]: 
        #print("cristorei")
        palavra6[i]=palavra6[i].upper()
        #print(palavra6)
    elif palavra[i]!=palavra6[i]:
        palavra6[i]="_"
    elif palavra6[i] in palavra:
        palavra6[i]=palavra6[i]
    i+=1
strpalavra="".join(palavra)
strpalavra1="".join(palavra1)
strpalavra2="".join(palavra2)
strpalavra3="".join(palavra3)
strpalavra4="".join(palavra4)
strpalavra5="".join(palavra5)
strpalavra6="".join(palavra6)
print(strpalavra1)
if strpalavra1!=strpalavra: 
    print(strpalavra2)
    if strpalavra2!=strpalavra:
        print(strpalavra3)
        if strpalavra3!=strpalavra:
            print(strpalavra4)
            if strpalavra4!=strpalavra:
                print(strpalavra5)
                if strpalavra5!=strpalavra:
                    print(strpalavra6)
                    if strpalavra6!=strpalavra:
                        print("Palavra correta:", strpalavra)
                    else: print("Resposta correta")  
                else: print("Resposta correta")
            else: print("Resposta correta")   
        else: print("Resposta correta")
    else: print("Resposta correta")               
else: print("Resposta correta")
# Leitura dos palpites e impressão do resultado para cada palpite



# Impressão da linha final
# ...
#    print("Resposta correta")
# ...
#    print("Palavra correta:", palavra)
