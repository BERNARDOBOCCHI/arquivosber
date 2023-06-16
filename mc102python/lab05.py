##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome:Bernardo Bocchi
# RA: 260376
##################################################

# Leitura do valor da hora
V = int(input()) #salario/hora

# Leitura do numero de dias trabalhados na semana
D = int(input())

# Leitora e processamento dos periodos de trabalho de cada dia
i=D+0
horas_trabalhadas=0
horas_extras=0
horas_extrasdiarias=0
horas_extrassemanas=0
turno=0
while i>0:
    nperiodosdia=int(input())
    turno=0
    
    while nperiodosdia>0:
        
        horarioinicio=int(input())
        horariofim=int(input())
        #print("oi")
        turno+=horariofim-horarioinicio
        #print("turno",turno)
        horas_trabalhadas+=horariofim-horarioinicio
        nperiodosdia-=1
    if turno>8: horas_extrasdiarias+=turno-8
    #print("horas extras diarias",horas_extrasdiarias)
    
    i-=1
    #print(nperiodosdia,horarioinicio,horariofim,horas_trabalhadas,horas_extrasdiarias)
if horas_trabalhadas-horas_extrasdiarias>44: horas_extrassemanas=horas_trabalhadas-44-horas_extrasdiarias
horas_extras=horas_extrasdiarias+horas_extrassemanas
# Calculo do valor devido ao funcionário

valor=V*horas_trabalhadas+(V/2)*horas_extras

# Impressão da saída
print("Horas trabalhadas:", horas_trabalhadas)
print("Horas extras:", horas_extras)
print("Valor devido: R$ {:0.2f}".format(valor))
