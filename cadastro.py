#Crie um programa em Python que permita ao gestor cadastrar clientes. O programa deve seguir os seguintes passos:
#Cadastro de clientes: Para cada cliente, solicite: Nome, Idade, Cidade

#Repetição do cadastro: Após cadastrar um cliente, pergunte ao gestor: "Deseja cadastrar outro cliente?"
#Se a resposta for "Sim", continue o cadastro. Se a resposta for "Não", finalize o processo de cadastro.

#Ao final do cadastro, o programa deve exibir:
#A lista completa de clientes cadastrados, mostrando os dados de cada um separadamente.
#O total de clientes cadastrados.
#A média da idade dos clientes.

#Consulta por cliente:
#Após mostrar os dados, pergunte: "Deseja acessar os dados de um cliente específico pelo nome?"
#Se sim, solicite o nome do cliente e mostre suas informações.
#Se o nome não existir, mostre uma mensagem de "Cliente não encontrado".

gestor = "Sim"
clientes = []
media_idade = 0

while gestor == "Sim":
  cadastro = []

  nome = str(input("Qual o nome do cliente? ")).strip().capitalize()
  cadastro.append(nome)

  idade = int(input("Qual a idade do cliente? "))
  cadastro.append(idade)
  media_idade += idade

  cidade = str(input("Qual a cidade do cliente? ")).strip().capitalize()
  cadastro.append(cidade)

  clientes.append(cadastro)

  gestor = str(input("Deseja cadastrar outro cliente? ")).strip().capitalize()

print("Lista completa de clientes cadastrados\n")
for i, cliente in enumerate(clientes, start=1):
  print(f"Cliente {i}")
  print(f"  Nome: {cliente[0]}")
  print(f"  Idade: {cliente[1]}")
  print(f"  cidade: {cliente[2]}")
  print("")

print(f"Temos um total de {len(clientes)} clientes cadastrados")
print("")

print(f"A média de idade dos clientes cadastrados é: {media_idade / len(clientes):.0f}")

busca = str(input("Deseja acessar os dados de um cliente específico pelo nome? ")).strip().capitalize()

if busca == "Sim":
  nome_cliente = str(input("Qual o nome do cliente? ")).strip().capitalize()

  for busca_cliente in clientes:
    if nome_cliente in busca_cliente:
      print(f"Nome: {busca_cliente[0]}")
      print(f"Idade: {busca_cliente[1]}")
      print(f"Cidade: {busca_cliente[2]}")
  


