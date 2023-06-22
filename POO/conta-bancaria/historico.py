from datetime import date
class Historico:
    tipos_transacao = {
        'sa':'saque',
        'de':'deposito',
        'tr':'transferencia'
        } 
    def __init__(self,numero,transacao, valor):
        self.numero = numero
        self.transacao = transacao
        self.valor = valor
        self.data = date.today()
    

   