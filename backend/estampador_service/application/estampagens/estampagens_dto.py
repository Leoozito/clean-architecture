from datetime import datetime
from estampador_service.domain.estampagens.entities import Estampagens
from estampador_service.domain.estoque.entities import Placas
from estampador_service.application.estoque.estoque_dto import EstoqueDto
from estampador_service.domain.estampagens.enums import EstampagensStatuses

class EstampagensDto(object):
    iniciado: datetime 
    concluido: datetime
    tipo: Placas
    status: str

    def __init__(self, iniciado: datetime, concluido: datetime, tipo: EstoqueDto):
        self.iniciado = iniciado
        self.concluido = concluido
        self.tipo = tipo
        self.status = EstampagensStatuses.CRIADO.name

    def to_domain(self):
        dados_estampagens = Estampagens(self.iniciado, self.concluido, self.tipo)
        dados_estampagens.status = EstampagensStatuses[self.status]
        return dados_estampagens
    
    def to_dto(self, estampagens: Estampagens):
        estoque_dto = self.tipo.to_dto(estampagens.customer)
        estampagens_dto = EstampagensDto(
            iniciado=estampagens.iniciado, 
            concluido=estampagens.concluido, 
            tipo=estoque_dto,
        )
        estampagens_dto.status = estampagens.status.name
        estampagens_dto.id = estampagens.id
        return estampagens_dto