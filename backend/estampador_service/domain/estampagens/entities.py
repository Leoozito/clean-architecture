# Onde vou definir minhas entidades
# Entidade placas, clientes, preços
from datetime import datetime
from .exceptions import RegisterDateCannotAfterConclusaoDate, PlacasCannotBeForgotten
from estampador_service.domain.estoque.entities import Placas
from estampador_service.domain.fiscal.entities import Fiscal
from .enums import EstampagensStatuses

class Estampagens(object): 
    iniciado: datetime 
    concluido: datetime
    tipo: Placas
    fiscal: Fiscal
    status: EstampagensStatuses

    def __init__(self, iniciado: datetime, concluido: datetime, tipo: Placas):
        self.iniciado = iniciado
        self.concluido = concluido
        self.tipo = tipo
        self.status = EstampagensStatuses.EM_ESTAMPAGEM

    def create_estampagens(self):
        self.is_valid()
        self.status = EstampagensStatuses.INICIADO

    def is_valid(self):
        print('INICIO: ', self.iniciado ,"|", "FINAL: ", self.concluido)
        if self.iniciado > self.concluido:
            raise RegisterDateCannotAfterConclusaoDate("Registro para iniciar não pode ser efetuado depois de concluido!")
        elif not self.tipo:
            raise PlacasCannotBeForgotten("É necessário informar a placa")

        return True