##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Rumo a Marte
# Nome:Bernardo Bocchi
# RA:260376
###################################################

# Leitura de dados



D1=int(input()) #Distância da trajetória, em quilômetros (km), entre a Terra e Marte no lançamento da SpaceX
V1=int(input()) #Velocidade da espaçonave da SpaceX em quilômetros por hora (km/h)
T=int(input()) #Tempo passado, em dias, entre o lançamento da SpaceX e Blue Origin.
D2=int(input()) # Distância da trajetória, em quilômetros (km), entre a Terra e Marte no lançamento da Blue Origin.
V2=int(input()) #  Velocidade da espaçonave da Blue Origin em quilômetros por hora (km/h)

# Cálculo do tempo total gasto por cada espaçonave 
Th=T*24
Th1=D1/V1
Th2=D2/V2+Th


# Impressão da resposta
if Th2<Th1:print("False")
else: print("True")
