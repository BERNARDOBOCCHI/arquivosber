#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Encaixe 2D
# Nome:
# RA:
#####################################################


'''
Dica: A criação das seguintes funções pode facilitar o desenvolvimento
do laboratório:
1) Uma função para rotacionar a peça em 90 graus para direita.
2) Uma função para verificar se é possível encaixar a peça a partir de
uma determinada linha e coluna do tabuleiro.
'''
def rodar(Py,Px,peca):

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
  return(rodar)
#Leitura do tabuleiro
Tx = int(input())
tabuleiro = []
for _ in range(Tx):
  tabuleiro.append(input().split())
Ty=len(tabuleiro[0])
  # Leitura da peça
Px = int(input())
peca = []
for _ in range(Px):
  peca.append(input().split())
Py=len(peca[0])
z=0
while z<4:  
  peca=rodar(Py,Px,peca)

  #print(tabuleiro)  
  #print(peca)
  #print(Tx,Ty)
  #print(Px,Py)
  cagavel=0
  nx=0
  ny=0
  I=0
  J=0
  teste=0
  r=0
  rtndx=0
  rtndy=0

  while r>4:   
        while I+nx<Tx:
          while J+ny<Ty:
            while nx<Px:
              while ny<Py:
                #print(I,J,nx,ny)
                if peca[nx][ny]==tabuleiro[nx][ny]:
                  teste+=1
                  if teste==Px*Py: cagavel+=1
                  #print("oi")
                ny+=1
              ny=0
              nx+=1
            nx=0
            J+=1
          J=0
          I+=1
  z+=1
print(cagavel)

          




  # Impressão do resultado
