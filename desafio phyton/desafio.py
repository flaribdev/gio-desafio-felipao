def depositar(valor, saldo, extrato, /):
    if valor > 0:
        
        saldo += valor
        extrato += f"Depósito: R$ {valor}\n"
        return saldo, extrato

    else:
        print("Operação falhou! O valor informado é inválido")
def sacar(*,valor, saldo, extrato, numero_saques):
    
    global LIMITE_SAQUES
    if numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número de saques diários excedido")

    elif valor > limite:
        print("Operação falhou! Seu limite de saque é R$ 500,00")

    elif valor > saldo:
        print("Operação falhou! Não há saldo suficiente para saque deste valor")

    elif valor <= saldo:

        saldo -= valor
        extrato += f"Saque: R$ {valor}\n"
        numero_saques += 1
        
        
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def visualizar_extrato(saldo,/,*, extrato):

    print("\n========== Extrato ==========\n")
    if extrato == "":
        print("Não foram realizadas movimentações")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo}")
    print("==============================")

global lista_usuarios 
lista_usuarios = []
def criar_usuario():
    nome = input("Digite o nome: ")
    dn = input("Digite a data de nascimento: ")
    cpf = input("Digite o CPF(somente números): ")
    logradouro = input("Digite o logradouro: ")
    numero = input("Digite o número: ")
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    uf = input("Digite a UF: ")

    encontrado = [u for u in lista_usuarios if u['cpf'] == cpf]

    if not encontrado:
        usuario = {
            "nome": nome,
            "dn": dn,
            "cpf": cpf,
            "endereco": {
                "logradouro": logradouro,
                "numero": numero,
                "bairro": bairro,
                "cidade": cidade,
                "uf": uf
                }
        }
        lista_usuarios.append(usuario)
    else:
        print("==============================")
        print("")
        print("Usuário já cadastrado")
        print("")
        print("==============================")
        input("Digite uma tecla para continuar")
global lista_contas
lista_contas = []

def criar_conta(usuario, numero_conta):
    agencia = "0001"
    conta = {
        "agencia": agencia,
        "conta": numero_conta,
        "usuario": usuario
    }
    lista_contas.append(conta)
    numero_conta += 1

    print(f"conta criada: agencia: {agencia}, conta: {numero_conta}, usuario: " + usuario["nome"])

    return numero_conta

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
[5] Criar novo usuário
[6] Listar usuarios
[7] Criar conta

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
numero_conta = 0


while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: "))

        saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        
        saldo, extrato, numero_saques = sacar(valor=valor, saldo=saldo, extrato=extrato, numero_saques=numero_saques)

    elif opcao == "3":
        
        visualizar_extrato(saldo, extrato = extrato)
    
    elif opcao == "4":
        break

    elif opcao == "5":
        criar_usuario()

    elif opcao == "6":
        print(lista_usuarios) 

    elif opcao == "7":
        usuario = input("Digite o cpf do usuário: ")
        usuario_encontrado = [u for u in lista_usuarios if u['cpf'] == usuario]
        if usuario_encontrado:
            numero_conta = criar_conta(usuario_encontrado[0], numero_conta)
        else:
            print("Usuário não encontrado")

    else:
        print("Opção inválida, favor selecionar uma opção disponível")

