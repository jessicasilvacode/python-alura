class Data:
    
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print(" {}/{}/{} ".format(self.dia, self.mes, self.ano))


# no Python Console:
# from data import Data
# data = Data(dia, mes, ano)
# print(data.formatada())
