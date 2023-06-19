from random import randint
from nota import Nota
from produto import Produto

clientes = []

class Cliente:
    def __init__(self,nome):
        self.id = self.calc_id()
        self.nome = nome

    @staticmethod
    def calc_id():
        return randint(1, 1000)


def menu_compra():
    print("""
    ================ MENU COMPRA ================
    
    1.inserir produtos
    2.ver produtos
    3.fechar compra
    0.Sair
    
    """)
    acao = input("")
    if acao == '0':
        print('Você saiu!')
        return
    elif acao == '1':
        nome = input('nome:')
        c = Cliente(nome)
        clientes.append({c.id : c})
        

def menu():
    print("""
    ==================== MENU ====================
    
    1.Começar uma compra 
    0.Sair
    
    """)
    acao = input("")
    if acao == '0':
        print('Você saiu!')
        return
    elif acao == '1':
        menu_compra()



if __name__== '__main__':
    menu()