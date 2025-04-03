#CRIANDO UM SISTEMA BANCARIO COM PYTHON#

menu='''
********** BANCO PYTHON **********

****** ESCOLHA A OPERAÇÃO DESEJADA ******
[0] SAIR
[1] DEPOSITOS
[2] SAQUES
[3] EXTRATOS

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
        print("Processando.....")
        sleep(2.5)
        if deposito>0:
            print(f"O valor do deposito é de R$ {deposito}")
            saldo+=deposito
            sleep(3.5)
            print(f"Seu saldo atual é de R$ {saldo}")
            sleep(2.5)
            opção=str(input('''Deseja realizar outra operação? [s]\[n]\n''')).upper
            if opção=="N":
                sleep(3.5) 
        print('''Obrigado por utilizar nosso banco 
                 Volte sempre.''')
        sleep (2.5)
        break
    if operação==2:
        print("saque")
    if operação==3:
        print("extrato")
    
    
