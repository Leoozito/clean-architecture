from datetime import datetime
from estampador_service.domain.estampagens.entities import Estampagens
from estampador_service.domain.estoque.entities import Placas

class EstampagensDto(object):
    iniciado: datetime 
    concluido: datetime
    tipo: Placas

    def __init__(self, iniciado: datetime, concluido: datetime, tipo: Placas):
        self.iniciado = iniciado
        self.concluido = concluido
        self.tipo = tipo

    def to_domain(self):
        return Estampagens(self.iniciado, self.concluido, self.tipo)