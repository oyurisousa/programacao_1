from produto import Produto
from random import randint

class Nota:

    def __init__(self):
        self.codigo = self.gerarCodigoNota()
        self._produtos = self.listar_produtos()

        
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self,new):
        self._codigo = new

    @property
    def produtos(self):
        return self._codigo
    
    @produtos.setter
    def codigo(self,new):
        self._produtos = new




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

    def inserir_produto(self):
        data = {
            'desc' : input("descrição: "),
            'codigo' : int(input("codigo: ")),
            'preco' : float(input("preco: "))
        }
        
        #Produto(data['desc'], data['codigo'], data['preco'])

        with open('produtos.txt','a') as file:
            file.write(f"{data['desc']} {data['codigo']} {data['preco']}\n")


n1 = Nota()
