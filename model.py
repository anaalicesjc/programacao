#Autor: Ana Alice

#TEMA: Trabalho realizado para levantar um avião.

#FÓRMULA: t = F * d * cos (°)
#O ângulo que será utilizado será COS (40°) = 0,77


def ajuda():
    print()
    print('1°: Este projeto tem a objetivo de te ajudar nos calculos repetitivos sobre o trabalho que será realizado pela aeronave \
no momento da decolagem;')
    print()
    print('2°: Para o melhor execução do usuário, é preciso seguir os passos que serão mostrados no decorrer da execução do programa;')
    print()
    print('Então vamos lá !!')
    print()

def opcao2():
    distancia = float(input("Digite a distância necessária para a decolagem [m]: "))
    trabalho = (distancia * 0.77) * 254000
    print ("O trabalho realizado pelo Boeing 787-10 é de: " + str(trabalho))
    print()

def opcao3():
    distancia = float(input("Digite a distância necessária para a decolagem [m]: "))
    trabalho = (distancia * 0.77) * 308000
    print ("O trabalho realizado pelo Airbus A350-900 é de: " + str(trabalho))
    print()

def opcao4():
    distancia = float(input("Digite a distância necessária para a decolagem [m]: "))
    trabalho = (distancia * 0.77) * 319000
    print ("O trabalho realizado pelo Airbus A350-1000 é de: " + str(trabalho))
    print()

def opcao5():
    distancia = float(input("Digite a distância necessária para a decolagem [m]: "))
    trabalho = (distancia * 0.77) * 975000
    print ("O trabalho realizado pelo Boeing 747-8 é de: " + str(trabalho))
    print()

def opcao6():
    distancia = float(input("Digite a distância necessária para a decolagem [m]: "))
    trabalho = (distancia * 0.77) * 575000
    print ("O trabalho realizado pelo Airbus A380 é de: " + str(trabalho))
    print()   

def opcao7():
    distancia = float(input("Digite a distância necessária para a decolagem [m]: "))
    trabalho = (distancia * 0.77) * 351500
    print ("O trabalho realizado pelo Boeing 777 é de: " + str(trabalho))
    print()  
