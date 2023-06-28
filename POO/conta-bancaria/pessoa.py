class Pessoa:
    def __init__(self,nome,cpf,cidade,endereco,uf):
        self.__nome = nome
        self.__cpf = cpf
        self.__cidade = cidade
        self.__endereco = endereco
        self.__uf = uf

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, new):
        self.__nome = new

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, new):
        self.__cpf = new

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



