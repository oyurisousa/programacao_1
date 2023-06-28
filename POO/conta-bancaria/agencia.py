class Agencia:
    contas = []
    def __init__(self,numero, cidade, endereco, uf):
        self.__numero = numero
        self.__cidade = cidade
        self.__endereco = endereco 
        self.__uf = uf

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, new):
        self.__numero = new

    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, new):
        self.__cidade = new

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, new):
        self.__endereco = new

    @property
    def uf(self):
        return self.__uf
    
    @uf.setter
    def uf(self, new):
        self.__uf = new
