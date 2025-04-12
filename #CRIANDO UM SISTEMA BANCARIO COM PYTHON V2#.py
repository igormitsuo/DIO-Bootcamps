#CRIANDO UM SISTEMA BANCARIO COM PYTHON V2#

#COMENTARIOS DO CODIGO#
'''Variavel menu com as opções de opeação'''
menu='''
********** BANCO PYTHON **********

****** ESCOLHA A OPERAÇÃO DESEJADA ******
[0] SAIR
[1] DEPOSITOS
[2] SAQUES
[3] EXTRATO DETALHADO

**************************************
'''
''' Declaração de variaveis e importações de funções'''
from time import sleep
from datetime import datetime
import pytz
saldo=0.0
deposito=0.0
saque=0.0
cont_deposito=0
cont_saque=0
data_hora_deposito=[]
extrato_deposito=[]
data_hora_saque=[]
extrato_saque=[]
cont_saque_diario=0
cont_operação_max=0

'''Loop infinito, aguardando a  opção "0" para parar.'''
while True:
    if cont_operação_max>9: #Contagem max de operações no dia
        print("## NUMERO MAXIMO DE TRANSAÇÃO DIARIA EXCESSIDA ##")
        print("## OPERAÇÃO FINALIZADA ##")
        sleep(1)
        break
    operação=int(input(menu)) #Escolha da opção pelo usuario
    if operação not in [0,1,2,3]:     #Validação do menu#
        print('''##  OPÇÃO INVALIDA ##
                ESCOLHA UMA OPÇÃO NO MENU''')
        sleep(2.0)
    if operação==0: # 1º bloco - opção sair, encerrando o loop infinito.
        sleep(1)
        print("Opção Sair")       
        sleep(2) 
        print('''Obrigado por utilizar nosso banco 
         Volte sempre.''')
        sleep (3.5)
        break
    if operação==1: # 2º bloco - opção deposito - usuario informa o valor que é guardado na variavel deposito e exibido no extrato.
        print("Opção Deposito")
        deposito=float(input("Digite o valor do deposito \n"))
        print("Processando.....")
        sleep(1.5)
        if deposito>0:
            print(f"O valor do deposito é de R$ {deposito :.2f}")
            saldo+=deposito  
            data_hora=datetime.now()
            data_hora_deposito.append(data_hora.strftime('%d/%m/%y %H:%M:%S'))
            extrato_deposito.append(deposito)
            sleep(1.5)
            print(f"Seu saldo atual é de R$ {saldo :.2f}")
            sleep(1.5)
            cont_operação_max+=1
            opção=str(input('''Deseja realizar outra operação? [s]\[n]\n''')).upper() #estrutura de decisão - usuario decide se deseja realizar outra operação.   
            if opção not in ["S","N"]:           
                print("### OPÇÃO INVALIDA - RETORNANDO AO MENU PRINCIPAL ###")          
            if opção=="N":
                sleep(1.5) 
                print('''Obrigado por utilizar nosso banco 
                 Volte sempre.''')
                sleep (1.5)
                break            
            print("Processando...")
            sleep(1.5)
        else:
            print("### OPERAÇÃO INVALIDA ###")
            sleep(3.0)
    if  operação==2: #3º bloco - opção saque - usuario informa o valor de saque,que é salvo em uma variavel e exibido no extrato
        print("Opção Saque\n")
        print(f'*** Seu saldo é de R$ {saldo :.2f}****')
        print("Limite de saque por operação ***R$ 500,00***")
        print("Limite de saque diario ***R$ 1500,00***\n")
        saque=float(input("Digite o valor de saque desejado\n"))
        print("Processando.....")
        sleep(1.5)
        if cont_saque_diario ==2:
            print("### NUMERO DE SAQUES DIARIOS EXCEDIDO ###")
            print("## OPERAÇÃO FINALIZADA ##")
            sleep(1)
            break                
        if  saque<= 500 and saldo>=0 and saldo>=saque and saque>0:
            saldo-=saque
            data_hora=datetime.now()
            data_hora_saque.append(data_hora.strftime('%d/%m/%y %H:%M:%S'))
            extrato_saque.append(saque)
            cont_saque_diario+=1
            cont_operação_max+=1
            print(f"### VALOR SOLICITADO R$ {saque :.2f} ###\n")
            sleep(2)
            print(f"### RETIRE O VALOR SOLICITADO ### \n")
            sleep(2)
            print(f"Seu saldo atual é de R$ {saldo :.2f}\n")
            opção=str(input('''Deseja realizar outra operação? [s]\[n]\n''')).upper()
            if opção not in ["S","N"]:           
                print("### OPÇÃO INVALIDA - RETORNANDO AO MENU PRINCIPAL ###") 
            if opção=="N":
                sleep(1.5) 
                print('''Obrigado por utilizar nosso banco 
                 Volte sempre.''')
                sleep (1.5)
                break
            print("Processando...")
            sleep(1.5)  
            
        else:    
            if saque>500:
                print("### LIMITE DE SAQUE DIARIO EXCEDIDO ### ")
                sleep(3.0)
            if saldo<0 or saldo<saque:
                print("### SALDO INSUFICIENTE ### ")        
                print(f"Seu saldo atual é de R$ {saldo :.2f}")
                sleep(3.0)
            if saque<0:
                print("### OPERAÇÃO INVALIDA ###")
                sleep(3.0)
            opção=str(input('''Deseja realizar outra operação? [s]\[n]\n''')).upper()
            if opção not in ["S","N"]:           
                print("### OPÇÃO INVALIDA - RETORNANDO AO MENU PRINCIPAL ###") 
            if opção=="N":
                sleep(1.5) 
                print('''Obrigado por utilizar nosso banco 
                Volte sempre.''')
                sleep (1.5)
                break
            print("Processando...")
            sleep(1.5)
                   
    if operação==3: #4º bloco - opção extrato - exibe o historico de movimentações realizadas pelo usuario.  
            print("*"*40)
            texto="## Extrato Bancario ##"
            print(f'{texto:^40}')
            print("")             
            for numero in extrato_deposito:
               print(f'Data\Hora               {data_hora_deposito[cont_deposito]}')
               cont_deposito+=1
               print(f'Deposito.....................R$ {numero:.2f}')
            print("*"*40)
            print("")
            for numero in extrato_saque:
                print(f'Data\Hora              {data_hora_saque[cont_saque]}')
                cont_saque+=1
                print(f'saque........................R$ {numero:.2f}') 
            print("*"*40)
            print("")      
            print(f"Seu saldo atual é de ........R$ {saldo :.2f}")
            cont_operação_max+=1
            print("*"*40)
            print("")
            opção=str(input('''Deseja realizar outra operação? [s]\[n]\n''')).upper()
            if opção not in ["S","N"]:           
                print("### OPÇÃO INVALIDA - RETORNANDO AO MENU PRINCIPAL ###") 
            if opção=="N":
                sleep(1.5) 
                print('''Obrigado por utilizar nosso banco 
                Volte sempre.''')
                sleep (1.5)
                break
            print("Processando...")
            sleep(1.5)
    
    
        
    
    
