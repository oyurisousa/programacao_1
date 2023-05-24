class Fatura:
    produtos = []

    def __init__(self, numero, descricao, quantidade=0, precoUnitario=0.0):
        self.__numero = numero
        self.__descricao = descricao
        self.__quantidade = max(0, quantidade)
        self.__precoUnitario = max(0.0, precoUnitario)

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        if isinstance(numero, int):
            self.__numero = numero
        else:
            raise ValueError("O número da fatura deve ser um valor inteiro.")

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise ValueError("A descrição da fatura deve ser uma string.")

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        if isinstance(quantidade, int):
            self.__quantidade = max(0, quantidade)
        else:
            raise ValueError("A quantidade deve ser um valor inteiro.")

    @property
    def precoUnitario(self):
        return self.__precoUnitario

    @precoUnitario.setter
    def precoUnitario(self, precoUnitario):
        if isinstance(precoUnitario, float) or isinstance(precoUnitario, int):
            self.__precoUnitario = max(0.0, float(precoUnitario))
        else:
            raise ValueError("O preço unitário deve ser um valor numérico.")

    @classmethod
    def getTotalDaFatura(self):
        total = []
        for obj in Fatura.produtos:
            print(f"Produto...Preco..quant")
            print("--------------------------")
            print(f"{obj.descricao}...{obj.precoUnitario}*{obj.quantidade}")
            total.append(obj.quantidade*
            obj.precoUnitario)

        print("--------------------------")
        print(f"Total....{sum(total)}") 

def cadastrar():
    while True:
        numero = input("Numero: ")
        if numero == "0": break
        descricao = input("descricao: ")
        quantidade = int(input("quantidade: "))
        precoUnitario = float(input("precoUnitario: "))

        temp = Fatura(numero, descricao,quantidade,precoUnitario)
        Fatura.produtos.append(temp)
    main()
    
    



def main():
    print("""
    =============== MENU ===============
    1.cadastrar produtos 2. ver fatura
    0. sair 
    ------------------------------------
    """)
    acao = input("")
    if acao == "0":
        return
    elif acao == "1":
        cadastrar()
    elif acao == "2":
        Fatura.getTotalDaFatura()
    else:
        print("a opção nao existe!")
        return




if __name__ == "__main__":
    main()