from datetime import date,datetime,timedelta

class Data:
    def __init__(self):
        self.dia =  date.today().day
        self.mes =  date.today().month
        self.ano =  date.today().year

    def get_dia(self):
        return self.dia
    
    def set_dia(self,dia):
        self.dia = dia
    
    def get_mes(self):
        return self.mes
    
    def set_mes(self,mes):
        self.mes = mes
    
    def get_ano(self):
        return self.ano
    
    def set_ano(self,ano):
        self.ano = ano
    
    def toString(self):
        return datetime(self.ano,self.mes,self.dia).date() 

    def nextday(self,days):
        newDate =  datetime(self.ano,self.mes,self.dia).date() + timedelta(days = days)
        self.set_dia(newDate.day)
        self.set_mes(newDate.month)
        self.set_ano(newDate.year)

p1 = Data()
print(p1.toString())
p1.nextday(4)
print(p1.toString())
