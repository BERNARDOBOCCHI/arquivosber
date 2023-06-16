###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Bernardo Bocchi
# RA: 260376
###################################################
estoque={}
entra=0
impressão=[]
produtos={}
# Leitura de dadosw
while entra!="FIM":
    entra=input()
    if entra!="FIM":
        key=entra[0:entra.find(":")-1]
        quantidade=int(entra[entra.rfind(":")+1:])
        if key not in estoque:
            if quantidade>0:
                #print(key)
                #print(entra)
                estoque[key]=quantidade
                produtos[key]=([quantidade,1,0])
                #print: estoque
            elif quantidade<0:
                print("Quantidade indisponivel para a venda de " + str(-quantidade) + " unidade(s) do produto " + key + ".")
        elif key in estoque: 
            #print(key)
            #print(entra)
            if estoque[key]+quantidade>=0:
                #print("oi")
                estoque[key]+=quantidade
                produtos[key][0]=estoque[key]
                if quantidade>0:
                    #print("oi2")    
                    produtos[key][1]+=1
                elif quantidade<0:
                   # print("oi3")
                    
                    produtos[key][2]+=1
            elif estoque[key]+quantidade<0:
                print("Quantidade indisponivel para a venda de " + str(-quantidade) + " unidade(s) do produto " + key + ".")
# Processamento
#print(estoque)
predutos=sorted(produtos.items(), reverse = False)
#print(predutos)
prudutos=dict(predutos)
for x in prudutos:
    #print(produtos)
    "Produto:{}\nQuantidade em Estoque:{}\nPedidos de Compra:{}\nPedidos de Venda:{}"
    #print(x)
    #print(produtos[x][0])
    #print(produtos[x][1])
    #print(produtos[x][2])
    prudutos[x][0]=str(prudutos[x][0])
    prudutos[x][1]=str(prudutos[x][1])
    prudutos[x][2]=str(prudutos[x][2])
    print(f"Produto: {x}\nQuantidade em Estoque: {prudutos[x][0]}\nPedidos de Compra: {prudutos[x][1]}\nPedidos de Venda: {prudutos[x][2]}")
    
#print("Quantidade indisponivel para a venda de " + X + " unidade(s) do produto " + N + ".")

# Impressão da saída
# ...
  #p
  #
  #print("Pedidos de Compra: " + C)
  #print("Pedidos de Venda: " + V)