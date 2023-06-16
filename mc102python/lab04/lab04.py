###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome:
# RA:
###################################################

# leitura da sequência de compras e vendas



estoque=0
i=0
pedido=True
L=[]
while pedido:
 pedido=int(input())
 if pedido+estoque>=0:
  if pedido<0 and pedido+estoque>=0: i+=1
  estoque=estoque+pedido 
  
 else:L.append(pedido)
   
  
# impressão da saída
j=0
while j<len(L):
 print("Quantidade indisponível para a venda de",-L[j],  "unidades.")
 j+=1
print("Quantidade de vendas realizadas:",i)
print("Quantidade em estoque:", estoque)
