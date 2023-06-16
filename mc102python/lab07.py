###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Disconnect
# Nome:Bernardo Bocchi
# RA:260376
###################################################

# Leitura das tropas de defesa
i=int(input())
jogador1=[]
jogador2=[]
pontuacao=0
n=i+0

while i>0: 
  jogador1.append(int(input()))
  i-=1
k=int(input())
m=k+0
while k>0: 
  jogador2.append(int(input()))
  k-=1
#print(jogador1)  
#print(jogador2)
q=0
c=0
while pontuacao<=0 and c+m<=n :
  pontuacao=0
  #print("oi")
  #print(q,m,c,n)
  while q<=m-1 and c+m<=n :
    #print(c,q) 
    if jogador1[q+c]<jogador2[q]: pontuacao+=1
    elif jogador1[q+c]>jogador2[q]: pontuacao-=1
    q+=1
  #print("pontuaçao:",pontuacao)
  if pontuacao <=0 and c+m<=n : c+=1
  q=0
#print(pontuacao)
if pontuacao<=0:
  print('Derrota')
else:
  print('Vitória posicionando as tropas a partir da posição', c+1)