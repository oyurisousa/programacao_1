from random import randint
from historico import Historico
from agencia import Agencia
from pessoa import Pessoa
class Conta(Pessoa):
    def __init__(self,nome,cpf,cidade,endereco,uf,num_agencia,saldo=0):
        super().__init__(nome,cpf,cidade,endereco,uf)
        self.__numero = self.gerar_numero()
        self.__saldo = saldo
        self.__historico = []
    
    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self,new):
        self.__numero = new
     
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self,new):
        if isinstance(new,(int,float)):
            self.__saldo = new
    
    @property
    def historico(self):
        return self.__historico

    @historico.setter
    def historico(self,new):
        self.__historico.append(new)

    @staticmethod
    def gerar_numero():
        a = randint(1000,10000)
        for x in Agencia.contas:
            if x.numero == a:
                return Conta.gerar_numero()
        return a
    
    def depositar(self,valor,ti = 'de'):
        if valor > 0: 
            self.saldo += valor
            if ti == 'de':
                self.historico = Historico(self.numero,ti,valor)
            else:
                self.historico = Historico(self.numero,ti,valor)
        else:
            print("Digite valores maiores que 0!")

    def sacar(self,valor,ti = 'sa'):
        if valor <= self.saldo and valor > 0:
            self.saldo -= valor
            if ti == 'sa':
                self.historico = Historico(self.numero,ti,valor*-1)
            else:
                self.historico = Historico(self.numero,ti,valor*-1)
            print(f"saque de {valor} realizado com sucesso!")
            return True
        else:
            print("saldo insuficiente ou dados inválidos! ")
            return False
    
    def transferir(self,conta_destino, valor):
        if self.existe_conta(conta_destino) != False:
            if self.sacar(valor,'tr') == True:
                self.existe_conta(conta_destino).depositar(valor,'tr')
                
        else:
            print("A conta informada não existe! ")
    def extrato(self):
        for x in self.historico:
            print(f"""

            numero : {x.numero}
            transacao: {Historico.tipos_transacao[x.transacao]}      
            valor: {x.valor}
            data: {x.data}

            """)
    
    @classmethod
    def existe_conta(self,num):
        for conta in Agencia.contas:
            if conta.numero == num:
                return conta
        return False
    
