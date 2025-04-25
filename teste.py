#teste
'''saldo=0
extrato=[2.5,4.2,6.6]
list=[5,7,9]

#list.append(input("entre com um numero\n"))
for numero in list:

    print(f'extrato deposito..................R$ {numero :>20}')
for numero in extrato:

    print(f'extrato saque.....................R$ {numero:.2f}')'''

'''while True:
    numero = int(input("Digite um número (1, 2 ou 3): "))
    if numero not in [1, 2, 3]:
        print("nok")    
    else:
        print("Número válido. ")
        break        

saque =int(input( "num"))
if saque>500 or saque>1500:
    print("### LIMITE DE SAQUE DIARIO EXCEDIDO ### ")'''

'''from datetime import time,datetime,date

data_hora=datetime.today()
print(data_hora)'''

#import pytz
from datetime import datetime

'''x=[]
data=datetime.now()
x.append(data.strftime('%d/%m/%y %H:%M:%S'))
print(x)'''



contagemx=0
contagemy=0
x=[2,3,4,5]
y=[6,7,8,9]
for num in x:
    print(x[contagemx])
    contagemx+=1
    print(y[contagemy])
    contagemy+=1   
    
    ''' if cont_saque_diario ==2:
                print("### NUMERO DE SAQUES DIARIOS EXCEDIDO ###")
                print("## OPERAÇÃO FINALIZADA ##")
                print(cont_saque_diario)
                sleep(1)
                break    '''
    


    #teste funções


'''def adicionar_elemento(lista, elemento):
  lista.append(elemento)
  print("Dentro da função:", lista)

lista_ex = [1, 2, 3]
adicionar_elemento(lista_ex, 4)
print("Fora da função:", lista_ex)

def listar_compras(*itens):
    for item in itens:
        print(item)

listar_compras('pão', 'leite', 'ovos')

def configuracoes(**opcoes):
    for chave, valor in opcoes.items():
        print(f'{chave}: {valor}')

configuracoes(cor='azul', tamanho='grande', forma='circular')'''

'''def menu():
   print(
********** BANCO PYTHON **********

****** ESCOLHA A OPERAÇÃO DESEJADA ******
[0] SAIR
[1] DEPOSITOS
[2] SAQUES
[3] EXTRATO DETALHADO

**************************************


   opção=int(input("Entre com a opção \n"))
   return(opção)

resultado = menu()
print(resultado)

def configurar_usuario(nome, idade, cidade):
    print(f'Nome: {nome}, Idade: {idade}, Cidade: {cidade}')

info_usuario = {'nome': 'Carlos', 'idade': 28, 'cidade': 'São Paulo'}
configurar_usuario(**info_usuario)'''



list=[]
listas=[22,4,5]
list.append(1)
list.append(2)
list.append(listas)
print(list)


minha_lista = ["foo", "bar", "baz", "bar"]
indices_de_bar = [indice for indice, item in enumerate(minha_lista) if item == "bar"]
print(indices_de_bar)  # Saída: [1, 3]