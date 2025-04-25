

from time import sleep
from datetime import datetime
import pytz
saldo=0
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

    
def menu():
 print('''
********** BANCO PYTHON **********

****** ESCOLHA A OPERAÇÃO DESEJADA ******
[0] SAIR
[1] DEPOSITOS
[2] SAQUES
[3] EXTRATO DETALHADO

**************************************
''')
 valor=int(input("Entre com a opção \n"))
 if valor not in [0,1,2,3]:
    print("## OPÇÃO INVALIDA: DIGITE UM VALIDO##")
    sleep(2)
 return (valor)

def confirmar():
  while True:
    opção=str(input('''Deseja realizar outra operação? [s]\[n]\n''')).upper() #estrutura de decisão - usuario decide se deseja realizar outra operação.    
    if opção not in ["S","N"]:           
      print("### OPÇÃO INVALIDA ###")          
    elif opção == "S" or "N":
      return (opção)
      break 

def f_deposito():
  while True:
    global saldo
    global data_hora
    global data_hora_deposito
    global extrato_deposito
    global cont_operação_max
    global deposito
    print("deposito")
    deposito=float(input("Digite o valor do deposito \n"))
    print("Processando.....")
    sleep(1.0)
    if deposito>0:
      print(f"O valor do deposito é de R$ {deposito :.2f}")
      saldo+=deposito  
      data_hora=datetime.now()
      data_hora_deposito.append(data_hora.strftime('%d/%m/%y %H:%M:%S'))
      extrato_deposito.append(deposito)
      sleep(1.0)
      print(f"Seu saldo atual é de R$ {saldo :.2f}")
      sleep(1.0)
      cont_operação_max+=1
    if deposito<0:
      print("### OPERAÇÃO INVALIDA ###")
      sleep(1.0)  
    continuar=confirmar()
    if continuar =="N":
      sleep(1)
      print("### RETORNANDO AO MENU PRINCIPAL ###")
      break

def f_saque ():
  while True:
    global saque
    global cont_saque_diario
    global saldo
    global data_hora
    global data_hora_saque
    global extrato_saque
    global cont_operação_max
    print("Opção Saque\n")#3º bloco - opção saque - usuario informa o valor de saque,que é salvo em uma variavel e exibido no extrato
    print(f'*** Seu saldo é de R$ {saldo :.2f}****')
    print("Limite de saque por operação ***R$ 500,00***")
    print("Limite de saque diario ***R$ 1500,00***\n")
    saque=float(input("Digite o valor de saque desejado\n"))
    print("Processando.....")
    sleep(1.0)
    print(cont_saque_diario)
    if cont_saque_diario ==3:
      print("### NUMERO DE SAQUES DIARIOS EXCEDIDO ###")
      print("## OPERAÇÃO FINALIZADA ##")
      print("### RETORNANDO AO MENU PRINCIPAL ###")
      sleep(1)
      break                
    if saque<= 500 and saldo>=0 and saldo>=saque and saque>0:
      saldo-=saque
      data_hora=datetime.now()
      data_hora_saque.append(data_hora.strftime('%d/%m/%y %H:%M:%S'))
      extrato_saque.append(saque)
      cont_saque_diario+=1
      cont_operação_max+=1
      print(f"### VALOR SOLICITADO R$ {saque :.2f} ###\n")
      sleep(1)
      print(f"### RETIRE O VALOR SOLICITADO ### \n")
      sleep(1)
      print(f"Seu saldo atual é de R$ {saldo :.2f}\n")
      continuar=confirmar()
      if continuar =="N":
        print("### RETORNANDO AO MENU PRINCIPAL ###")
        sleep(1)
        break
    if saque>500:
      print("### LIMITE DE SAQUE DIARIO EXCEDIDO ### ")
      print("### RETORNANDO AO MENU PRINCIPAL ###")
      sleep(1.0)
      break
    if saldo<0 or saldo<saque:
      print("### SALDO INSUFICIENTE ### ")        
      print(f"Seu saldo atual é de R$ {saldo :.2f}")
      print("### RETORNANDO AO MENU PRINCIPAL ###")
      sleep(1.0)
      break
    if saque<0:
      print("### OPERAÇÃO INVALIDA ###")
      print("### RETORNANDO AO MENU PRINCIPAL ###")
      sleep(1.0)
      break
    
def f_extrato():
  while True:
    global saldo
    global deposito
    global saque
    global cont_deposito
    global cont_saque
    global data_hora_deposito
    global extrato_deposito
    global data_hora_saque
    global extrato_saque
    global cont_saque_diario
    global cont_operação_max
    print("extrato")
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
    print(f"Seu saldo atual é de ........R$ {saldo :.2f}")
    print("")
    for numero in extrato_saque:
      print(f'Data\Hora              {data_hora_saque[cont_saque]}')
      cont_saque+=1
      print(f'saque........................R$ {numero:.2f}') 
      print("*"*40)
      print("")      
      cont_operação_max+=1
    print(f"Seu saldo atual é de ........R$ {saldo :.2f}")
    print("")
    continuar=confirmar()
    if continuar =="N"or"S":
      print("### RETORNANDO AO MENU PRINCIPAL ###")
      sleep(1)
      break




while True:
 operação= menu()
 if operação==0:
   sleep(1)
   print("Opção Sair")       
   sleep(2) 
   print('''Obrigado por utilizar nosso banco Volte sempre.''')
   break
 elif operação==1:
   f_deposito()
 elif operação==2:
   f_saque()
 elif operação==3:
   f_extrato()
 
    