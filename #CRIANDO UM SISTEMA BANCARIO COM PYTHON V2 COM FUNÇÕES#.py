#CRIANDO UM SISTEMA BANCARIO COM FUNÇÕES EM PYTHON V2#

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
contas_banco=[]
conta_usuario=[]
cont_saque_diario=0
cont_operação_max=0
num_conta=0

    
def menu():
 print('''
********** BANCO PYTHON **********

****** ESCOLHA A OPERAÇÃO DESEJADA ******
[0] SAIR
[1] DEPOSITOS
[2] SAQUES
[3] EXTRATO DETALHADO
[4] CRIAR CONTA
[5] CADASTRAR USUARIO
[6] CONSULTAR CONTA DE USUARIO
       
**************************************
''')
 valor=int(input("Entre com a opção \n"))
 if valor not in [0,1,2,3,4,5,6]:
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

def f_deposito(): #Bloco 1 -Opção Deposito
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

def f_saque (): #Bloco 2 -opção saque - usuario informa o valor de saque,que é salvo em uma variavel e exibido no extrato
  while True:
    global saque
    global cont_saque_diario
    global saldo
    global data_hora
    global data_hora_saque
    global extrato_saque
    global cont_operação_max
    print("Opção Saque\n") 
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
    
def f_extrato(): #Bloco 3 -Opção Extrato Detalhado
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
    
def cad_conta(): #Bloco 4 -Opção Criar conta
  global num_conta
  cadastro={}
  agencia="0001" 
  num_conta+=1
  print("Processando.....")
  sleep(1.0)
  usuario=int(input("Digite o CPF DO USUARIO\n"))
  cadastro={"usuario":usuario,"agencia":agencia,"num_cont":num_conta}
  print("Processando.....")
  sleep(1.0)
  print("*"*40)
  texto="## CONTA BANCARIA ##"
  print(f'{texto:^40}')
  print(f" Usuario CPF:  {usuario} \n Agencia:  {agencia} \n Conta Numero {num_conta} ")
  texto="## CRIADA COM SUCESSO ##"
  print(f'{texto:^40}')
  sleep(2.0)
  return cadastro         

def cad_usuario():#Bloco 5 -Cadastrar Usuario
  cadastro={}
  end=[]
  print("Processando.....")
  sleep(1.0)
  nome=str(input("Digite o nome do Usuario\n"))
  cpf=int(input("Digite o CPF do usuario\n"))
  data_nasc=str(input("Digite a data de nasciento\n"))
  logradouro=str(input("Digite a Rua\n"))
  bairro=str(input("Digite o Bairro\n"))
  cidade=str(input("Digite a Cidade\n"))  
  estado=str(input("Digite o Estado\n"))
  sigla=str(input("Digite a Sigla\n"))
  cadastro= {"CPF":cpf,"Nome":nome,"Data de Nascimento":data_nasc,"Logradouro":logradouro,"Bairro":bairro,"Cidade":cidade,"Estado":estado,"Sigla":sigla}
  print("Processando.....")
  sleep(1.0)
  print("*"*40)
  texto="## CADASTRO DE USUARIO ##"
  print(f'{texto:^40}')
  print(f" Usuario Nome:                {nome} ")
  print(f" Usuario CPF:                 {cpf} ")
  print(f" Usuario data de nascimento:  {data_nasc} ")
  print(f" Usuario Logradouro:          {logradouro} ")
  print(f" Usuario Bairro:              {bairro} ")
  print(f" Usuario Cidade:              {cidade} \{sigla} ") 
  texto="## CRIADA COM SUCESSO ##"
  print(f'{texto:^40}') 
  sleep(2.0)
  return cadastro

def consulta_conta(): #Bloco 6 -Consultar Conta de Usuario
 global contas_banco
 global conta
 cont=0
 print("Processando.....")
 sleep(1.0)
 valor_procurado =int(input("Digite o CPF pra consultar\n"))
 for cliente in contas_banco:
  if cliente["usuario"]==valor_procurado:
   print(f"Informações do usuário: {cliente}")  
   cont+=1
  sleep(3)
  if cont<1: 
   sleep
   print("## CLIENTE NÃO ENCONTRADO ##")
   print("## REALIZE O CADASTRO DO CLIENTE ##") 
   sleep(2)

while True:
 operação= menu() 
 if operação==0: #Bloco 0 -Opção Sair
   sleep(1)
   print("Opção Sair")       
   sleep(2) 
   print('''Obrigado por utilizar nosso banco Volte sempre.''')
   break
 elif operação==1:#Bloco 1 -Opção Deposito
   f_deposito()
 elif operação==2:#Bloco 2 -opção saque - usuario informa o valor de saque,que é salvo em uma variavel e exibido no extrato
   f_saque()
 elif operação==3: #Bloco 3 -Opção Extrato Detalhado
   f_extrato()
 elif operação==4: #Bloco 4 -Opção Criar conta
   conta=cad_conta()
   contas_banco.append(conta.copy())
 elif operação==5: #Bloco 5 -Cadastrar Usuario  
   conta_user=cad_usuario()
   conta_usuario.append(conta_user.copy())
 elif operação==6: #Bloco 6 -Consultar Conta de Usuario
   contas_banco=contas_banco.copy()
   consulta_conta()

    
    
        
    
    
