from abc import ABC, abstractmethod
from datetime import datetime

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    @abstractmethod
    def registrar(conta):
        pass

class Historico:
    def __init__(self):
        self.transacoes = []    
    #Propriedade para pegr as transações
    @property
    def transacoes(self):
        return self.__transacoes
    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%s")
        })

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = [] #lista de contas vazia
    def adicionar_conta(self, conta):
        self.contas.append(conta) #adiciona a conta ao array
    def realizar_transacao(self, conta, transacao: Transacao):
        transacao.registrar(Conta)

class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()
    def saldo(self):
        return self.saldo
    def nova_conta(self, cliente, numero):
        return Conta(numero, cliente)
    #criar propertie para os atribuos ´privados
    @property
    def saldo(self):
        return self.__saldo
    @property
    def numero(self):
        return self.__numero
    @property
    def agencia(self):
        return self.__agencia
    @property
    def cliente(self):
        return self.__cliente
    @property
    def historico(self):
        return self.__historico   
    
    def sacar(self,valor):

        if valor <= 0:
            print("O valor do saque deve ser maior do que 0")            
        elif valor <= self.saldo:
            self.saldo -= valor
            print("\n Saque realizado com sucesso")
            return True
        else:
            print("Saldo insuficiente.")
        return False
    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            print("\n Depósito realizado com sucesso")
            return True
        else:
            print("O valor o saque deve ser maior do que 0")
        return False

class ContaCorrente(Conta):
    def __init__(self,numero, cliente, limite = 500,limite_saque = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"])
        
        if valor > self.limite:
            print("O valor do saque ultrapassa o limite de saque.")
        elif numero_saques > self.limite_saque:
            print("Excedeu o núero de saquesperimtido")
        else:
            super.saque(valor)
            return True
        return False
    def __str__(self):
        return f"""\n
                Agência: \t {self.agencia}
                C/C: \t\t {self.numero}
                Titular: \t {self.cliente.nome}
                """
        

class Deposito(Transacao):
    def __init__(self,valor):
        self.valor = valor
    @property
    def valor(self):
        return self.__valor
    def registrar(self, conta: ContaCorrente):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self,valor):
        self.valor = valor
    @property
    def valor(self):
        return self.__valor
    def registrar(self, conta: ContaCorrente):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

class PessoaFisica(Cliente):
    def __init__(self, endereco, nome, cpf, data_nascimento):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento