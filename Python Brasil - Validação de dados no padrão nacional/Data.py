from datetime import datetime

class Data:
    def __init__(self):
        self._momento_do_cadastro = datetime.now()

    def hora_do_cadastro(self):
        return f'{self._momento_do_cadastro.hour}:{self._momento_do_cadastro.minute}'
    
    def dia_da_semana(self):
        dias_da_semana = [
            "Domingo",
            "Segunda-Feira",
            "Terça-Feira",
            "Quarta-Feira",
            "Quinta-Feira",
            "Sexta-feira",
            "Sábado"            
        ]
        dia_do_cadastro = self._momento_do_cadastro.weekday()
        return dias_da_semana[dia_do_cadastro + 1]
    
    def mes_do_cadastro(self):
        meses_do_ano = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]
        mes_do_cadastro = self._momento_do_cadastro.month
        return meses_do_ano[mes_do_cadastro + 1]

    def dia_do_mes(self):
        return self._momento_do_cadastro.day
    
    def ano_do_cadastro(self):
        return self._momento_do_cadastro.year

    def __str__(self):
        return f'Conta criada dia {self.dia_do_mes()} de {self.mes_do_cadastro()} de {self.ano_do_cadastro()}, {self.dia_da_semana()} as {self.hora_do_cadastro()}'