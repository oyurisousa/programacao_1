paises = {}

class Pais:
    def __init__(self,codigoISO, nome,populacao,dimensao,paisesFronteira=[]):
        if isinstance(codigoISO,str) and codigoISO != "":
            self.codigoISO = codigoISO.upper()
        else:
            print("no")
            return
        self.nome = nome.capitalize()
        self.populacao = populacao
        self.dimensao = dimensao
        self.paisesFronteira = paisesFronteira

    def get_codigoISO(self):
        return self.codigoISO
    
    def set_codigoIso(self,newIso):
        self.codigoISO = newIso
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self,newNome):
        self.nome = newNome    

    def get_populacao(self):
        return self.populacao
    
    def set_populacao(self,newPopulacao):
        self.populacao = newPopulacao  

    def get_dimensao(self):
        return self.dimensao
    
    def set_dimensao(self,newDimensao):
        self.dimensao = newDimensao 
    def get_paisesFronteira(self):
        return self.paisesFronteira
    
    def set_paisesFronteira(self,newPaisesFronteira):
        self.paisesFronteira = newPaisesFronteira 
    
    def compararCodigoIso(self,ISO=0):
        for x in paises:
            print(x)
            """if self.codigoISO == ISO.upper():
                return True
            return False"""




def cadastrar():
    dados = {
        'codigoISO': input('código ISO: ').upper(),
        'nome': input('nome: ').capitalize(),
        'populacao': int(input('populacao: ')),
        'dimensao': float(input('Dimensão: ')),
        'front': input("paises que fazem fronteiras (utilize ',' para separar): ").split(",")
    }
    inst = Pais(dados['codigoISO'], dados['nome'], int(dados['populacao']), float(dados['dimensao']), list(dados['front']))
    paises[dados['nome']] = inst  # Adiciona o país ao dicionário paises
    with open('paises.txt', 'a') as file:
        file.write(f"{dados['codigoISO']},{dados['nome']},{dados['populacao']},{dados['dimensao']}, {dados['front']}\n")
    print(f"{dados['nome']} cadastrado com sucesso!")


def menu():
    # Restante do código...
    print("""
        =============== MENU ===============
        1.cadastrar país 2. comparar código ISO
        3.verificar países limítrofes 4.verificar densidade populacional
        5.verificar paises vizinhos comuns
        0. sair 
        ------------------------------------
        """)
    acao = input("")
    if acao == "0":
        return
    elif acao == "1":
        cadastrar()
    elif acao == "2":
        p1 = input("nome país 1: ").capitalize()
        p2 = input("nome país 2: ").capitalize()
        if p1 in paises and p2 in paises:
            if paises[p1].codigoISO == paises[p2].codigoISO:
                print('são iguais')
            else:
                print('são diferentes')
        else:
            print('Pais não cadastrado')

    # Restante do código...

if __name__ == "__main__":
    with open("paises.txt", 'r') as file:
        for obj in file:
            x = obj.split(',')
            paises[x[1]] = Pais(x[0], x[1], int(x[2]), float(x[3]), list(x[4]))
        print(paises)
    menu()
