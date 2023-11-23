# Onde vou definir minhas entidades
# Entidade placas, clientes, preços
from datetime import datetime
from .exceptions import RegisterDateCannotAfterConclusaoDate, PlacasCannotBeForgotten
from estampador_service.domain.estoque.entities import Placas
from estampador_service.domain.fiscal.entities import Fiscal

class Estampagens(object): 
    iniciado: datetime 
    concluido: datetime
    tipo: Placas
    fiscal: Fiscal

    def __init__(self, iniciado: datetime, concluido: datetime, tipo: Placas):
        self.iniciado = iniciado
        self.concluido = concluido
        self.tipo = tipo

    def is_valid(self):
        print('INICIO: ', self.iniciado ,"|", "FINAL: ", self.concluido)
        if self.iniciado > self.concluido:
            raise RegisterDateCannotAfterConclusaoDate("Registro para iniciar não pode ser efetuado depois de concluido!")
        elif not self.tipo:
            raise PlacasCannotBeForgotten("É necessário informar a placa")

        return True