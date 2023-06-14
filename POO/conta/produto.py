class Produto:
    def __init__(self,descricao, codigo, preco):
        self.descricao = descricao
        self.codigo = codigo
        self.preco = preco 

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, new):
        self._descricao = new

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, new):
        self._codigo = new

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, new):
        self._preco = new