#Autor: Ana Alice

#MENU - Trabalho realizado para levantar um avião.

import model
opcao = 1
while opcao != '8':
    opcao = input ("Escolha o modelo do avião: [1] Ajuda, [2] Boeing 787-10, [3]Airbus A350-900, [4] Airbus A350-1000, \
[5] Boeing 747-8, [6] Airbus A380, [7] Boeing 777, [8] Sair : ")

    if opcao == '1':
        model.ajuda()
        
    elif opcao == '2':
        model.opcao2()
        
    elif opcao == '3':
        model.opcao3()
  
    elif opcao == '4':
        model.opcao4()

    elif opcao == '5':
        model.opcao5()

    elif opcao == '6':
        model.opcao6()

    elif opcao == '7':
        model.opcao7()

    elif opcao == '8':
        print ("Saindo do programa..")

    else:
        print("Opção inválida")
    
