from produto import Produto
from random import randint

class Nota:

    def __init__(self):
        self.codigo = self.gerarCodigoNota()
        self.produtos = self.listar_produtos()

    @staticmethod
    def gerarCodigoNota():
        return randint(10000,99999)

    @staticmethod
    def listar_produtos():
        produtos = []
        with open("produtos.txt",'r') as file:
            for x in file:
                produtos.append(x.strip().split())
            
        return produtos            


    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self,new):
        self._codigo = new


n1 = Nota()
print(n1.__dict__)