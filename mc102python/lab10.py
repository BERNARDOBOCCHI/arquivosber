#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome:
# RA:
#####################################################

# Leitura da matriz

n = int(input())
matriz = [input().split() for _ in range(n)]
#print( matriz)
time=input()
k=int(input())
azul=0
vermelho=0

while k>0:
    comando=input()
    i=0
    j=0    
    for x in comando:
        #print(time)
        #print(i,j)
        #print(matriz[i][j])
        if matriz[i][j]=="*":
         #   print(i,j,"coletado")
            matriz[i][j]="."
            if time=="azul":
                azul+=1
            if time=='vermelho':
                vermelho+=1
        if x=="N": i-=1
        elif x=="S": i+=1
        elif x=='L': j+=1
        elif x=='O': j-=1
        if matriz[i][j]=="*":
          #  print(i,j,"coletado")
            matriz[i][j]="."
            if time=="azul":
                azul+=1
            if time=='vermelho':
                vermelho+=1
        
    #print(time)
    if time=="azul":
        time="vermelho"
    elif time=='vermelho':
        time='azul'
    #print(time)
    k-=1
print('Tesouros encontrados pelo time azul:',azul)
print('Tesouros encontrados pelo time vermelho:',vermelho)
if vermelho>azul: print('Vitoria do time vermelho')
if vermelho<azul: print('Vitoria do time azul')
if vermelho==azul: print('Empate')





# Impressão da saída
