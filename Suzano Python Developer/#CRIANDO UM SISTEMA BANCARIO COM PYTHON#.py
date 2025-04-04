#CRIANDO UM SISTEMA BANCARIO COM PYTHON#

menu='''
********** BANCO PYTHON **********

****** ESCOLHA A OPERAÇÃO DESEJADA ******
[0] SAIR
[1] DEPOSITOS
[2] SAQUES
[3] EXTRATO DETALHADO

**************************************
'''
from time import sleep
saldo=0.0
deposito=0.0
saque=0.0
extrato=" "
cont=0


while True:
    operação=int(input(menu))
    if operação==0:
        sleep(1)
        print("Opção Sair")       
        sleep(2) 
        print('''Obrigado por utilizar nosso banco 
         Volte sempre.''')
        sleep (3.5)
        break
    if operação==1:
        print("Opção Deposito")
        deposito=float(input("Digite o valor do deposito \n"))
       # print("Processando.....")
       # sleep(1.5)
        if deposito>0:
            print(f"O valor do deposito é de R$ {deposito :.2f}")
            saldo+=deposito  
            extrato + str(deposito)
            #sleep(1.5)
            print(f"Seu saldo atual é de R$ {saldo :.2f}")
           # sleep(1.5)
            opção=str(input('''Deseja realizar outra operação? [s]\[n]\n''')).upper()
            if opção=="N":
                sleep(1.5) 
                print('''Obrigado por utilizar nosso banco 
                 Volte sempre.''')
                sleep (1.5)
                break            
            #print("Processando...")
            #sleep(1.5)
    if cont<=2 and operação==2:
        print("Opção Saque\n")
        print(f'*** Seu saldo é de R$ {saldo :.2f}****')
        print("Limite de saque por operação ***R$ 500,00***")
        print("Limite de saque diario ***R$ 1500,00***\n")
        saque=float(input("Digite o valor de saque desejado\n"))
        #print("Processando.....")
        #sleep(1.5)
        if  saque<= 500 and saldo>-1 and saldo>=saque:
            saldo-=saque
            extrato=extrato+str(saque)
            cont+=1
            print(f"### VALOR SOLICITADO R$ {saque :.2f} ###\n")
            #sleep(2)
           # print(f"### RETIRE O VALOR SOLICITADO ### \n")
           # sleep(2)
            print(f"Seu saldo atual é de R$ {saldo :.2f}\n")
            opção=str(input('''Deseja realizar outra operação? [s]\[n]\n''')).upper()
            if opção=="N":
                sleep(1.5) 
                print('''Obrigado por utilizar nosso banco 
                 Volte sempre.''')
                sleep (1.5)
                break
            print("Processando...")
            #sleep(1.5)
        else:            
            if saque>500:
                print("### LIMITE DE SAQUE DIARIO EXCEDIDO ### ")
            if saldo<0 or saldo<saque:
                print("### SALDO INSUFICIENTE ### ")        
                print(f"Seu saldo atual é de R$ {saldo :.2f}")
            opção=str(input('''Deseja realizar outra operação? [s]\[n]\n''')).upper()
            if opção=="N":
                sleep(1.5) 
                print('''Obrigado por utilizar nosso banco 
                Volte sempre.''')
                sleep (1.5)
                break
            print("Processando...")
           # sleep(1.5)
    if operação==3:
            print(f"EXTRATO {extrato}")
            opção=str(input('''Deseja realizar outra operação? [s]\[n]\n''')).upper()
            if opção=="N":
                #sleep(1.5) 
                print('''Obrigado por utilizar nosso banco 
                Volte sempre.''')
                sleep (1.5)
                break
            #print("Processando...")
           # sleep(1.5)
    if cont>2:
            print("### NUMERO DE SAQUES DIARIOS EXCEDIDO ###")
    
    
    
