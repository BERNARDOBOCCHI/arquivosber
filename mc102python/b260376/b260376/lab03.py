###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Bernardo Bocchi
# RA:260376
###################################################

# leitura de dados
dia=int(input())    #<Dia da semana>
horainicio=int(input())    #<Hora de início da sessão>
minutoinicio=int(input())    #<Minuto de início da sessão>
minutagemdiaria=horainicio*60+minutoinicio
estudante=input()    #<Estudante>
pagamento=input()    #<Método de pagamento>
# valor do ingresso inteiro
if dia==1: precobruto=30 # domingo
elif (dia==2 or dia==3) and (minutagemdiaria>=1110) : precobruto=20 # segunda e terça noturo
elif (dia==2 or dia==3 or dia==4) and (minutagemdiaria<1110) : precobruto=15 # segunda terça e quarta diurno
elif (dia==4 or dia==5) and (minutagemdiaria>=1110) : precobruto=30 # quarta e quinta noturno
elif (dia==5 or dia==6) and (minutagemdiaria<1110) : precobruto=20 # quinta e sexta diurno
elif (dia==6 or dia==7) and (hminutagemdiaria>=1110) : precobruto=40 # sexta e sabado noturno
elif (dia==7) and (minutagemdiaria<1110) : precobruto=30 # sabado diurno

if estudante=="S" : precobruto=precobruto/2
elif dia==1 and pagamento=="C": precobruto=precobruto*0.7 # 
elif dia==7 and pagamento=="C": precobruto=precobruto*0.8 # 
elif dia==6 and (minutagemdiaria>=1110) and pagamento=="C" : precobruto=precobruto=precobruto*0,7 # 
elif pagamento =="C" : precobruto=precobruto/2


# saída do valor do ingresso
print('Valor do ingresso: R$', format(precobruto, '.2f').replace('.', ','))