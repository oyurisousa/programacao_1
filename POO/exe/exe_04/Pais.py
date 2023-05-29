

class Pais:
    paises = {}
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
    
    def compararCodigoIso():
        print("Paises cadastrados:")
        print('--------------------')
        for x in Pais.paises:
            print(x)
        p1 = input("nome país 1: ").capitalize()
        p2 = input("nome país 2: ").capitalize()
        if p1 in Pais.paises and p2 in Pais.paises:
            if Pais.paises[p1].codigoISO == Pais.paises[p2].codigoISO:
                print('são iguais')
            else:
                print('são diferentes')
        else:
            print('Pais não cadastrado')

    def paisLimitrofe(p1,p2):
        if p1 in Pais.paises and p2 in Pais.paises:
            if p1.lower() in Pais.paises[p2].paisesFronteira:
                print(Pais.paises[p2].paisesFronteira)
            else:
                print(Pais.paises[p1].__dict__)
                print(Pais.paises[p2].__dict__)
                print('não fazem fronteira')
        else:
            print('paises não cadastrados!')



def cadastrar():
    dados = {
        'codigoISO': input('código ISO: ').upper(),
        'nome': input('nome: ').capitalize(),
        'populacao': int(input('populacao: ')),
        'dimensao': float(input('Dimensão: ')),
        'front': input("paises que fazem fronteiras (utilize ',' para separar): ").split(",")
    }
    front = ''
    for x in dados['front']:
        if front == '':
            front = x
        else:
            front += f",{x}"

    inst = Pais(dados['codigoISO'], dados['nome'], int(dados['populacao']), float(dados['dimensao']), list(dados['front']))
    Pais.paises[dados['nome']] = inst  # Adiciona o país ao dicionário paises
    with open('paises.txt', 'a') as file:
        file.write(f"{dados['codigoISO']},{dados['nome']},{dados['populacao']},{dados['dimensao']}, {front}\n")
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
        Pais.compararCodigoIso()
    elif acao == '3':
        print("Paises cadastrados:")
        print('--------------------')
        for x in Pais.paises:
            print(x)
        p1 = input("nome país 1: ").capitalize()
        p2 = input("nome país 2: ").capitalize()
        return Pais.paisLimitrofe(p1, p2)
    # Restante do código...

if __name__ == "__main__":
    with open("paises.txt", 'r') as file:
        for obj in file:
            x = obj.split(',',maxsplit=4)
            Pais.paises[x[1]] = Pais(x[0], x[1], int(x[2]), float(x[3]), x[4].replace('[', '').replace(']', '').strip().split(','))
        print(Pais.paises)
    menu()
