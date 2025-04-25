'''#cadastro de conta

def cad_conta():
  global num_conta
  cadastro={}
  agencia="0001" 
  num_conta+=1
  usuario=int(input("Digite o CPF DO USUARIO\n"))
  cadastro={"usuario":usuario,"agencia":agencia,"num_cont":num_conta}
  print("*"*40)
  texto="## CONTA BANCARIA ##"
  print(f'{texto:^40}')
  print(f" Usuario CPF:  {usuario} \n Agencia:  {agencia} \n Conta Numero {num_conta} ")
  texto="## CRIADA COM SUCESSO ##"
  print(f'{texto:^40}')
  return cadastro
  
           

conta_banco=[]
num_conta=0
conta=cad_conta()
conta_banco.append(conta)
print(conta_banco)

#cadastro de usuario


def cad_usuario():
  cadastro={}
  end=[]
  nome=str(input("Digite o nome do Usuario\n"))
  cpf=int(input("Digite o CPF do usuario\n"))
  data_nasc=str(input("Digite a data de nasciento\n"))
  logradouro=str(input("Digite a Rua\n"))
  bairro=str(input("Digite o Bairro\n"))
  cidade=str(input("Digite a Cidade\n"))  
  estado=str(input("Digite o Estado\n"))
  sigla=str(input("Digite a Sigla\n"))
  cadastro= {"CPF":cpf,"Nome":nome,"Data de Nascimento":data_nasc,"Logradouro":logradouro,"Bairro":bairro,"Cidade":cidade,"Estado":estado,"Sigla":sigla}
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
  
  return cadastro


def consulta_conta():
 global conta_banco
 print(conta_banco)





conta_usuario=[]
conta=cad_usuario()
conta_usuario.append(conta)
print(conta_usuario)
conta_banco=[]
num_conta=0
conta=cad_conta()
conta_banco.append(conta)
print(conta_banco)'''

def cad_conta():
  global num_conta
  cadastro={}
  agencia="0001" 
  num_conta+=1
  usuario=int(input("Digite o CPF DO USUARIO\n"))
  cadastro={"usuario":usuario,"agencia":agencia,"num_cont":num_conta}
  print("*"*40)
  texto="## CONTA BANCARIA ##"
  print(f'{texto:^40}')
  print(f" Usuario CPF:  {usuario} \n Agencia:  {agencia} \n Conta Numero {num_conta} ")
  texto="## CRIADA COM SUCESSO ##"
  print(f'{texto:^40}')
  return cadastro

def consulta_conta():
 global conta_banco
 valor_procurado =int(input("Digite o CPF pra consultar\n"))
 chave_para_verificar = "usuario"
 for chave in conta_banco:
  
  print(chave)
        

  
           

conta_banco=[]
num_conta=0
conta=cad_conta()
conta_banco.append(conta)
conta=cad_conta()
conta_banco.append(conta)
conta=cad_conta()
conta_banco.append(conta)
conta=cad_conta()
conta_banco.append(conta)
print(conta_banco)
consulta_conta()
