from estampador_service.application.estoque.estoque_dto import EstoqueDto
from estampador_service.application.estampagens.estampagens_dto import EstampagensDto
from .models import Estoque, Estampagens
from django.db import transaction
from estampador_service.application.estampagens.estampagens_storage import EstampagensStorage
from estampador_service.domain.estampagens.enums import EstampagensStatuses

class EstampagensRepository(EstampagensStorage):
    def _estoque_dto_to_model(self, estoqueDto: EstoqueDto):
        estoque = Estoque()
        estoque.tipo = estoqueDto.tipoPlaca
        estoque.quantidade = estoqueDto.quantidade

        return estoque
    
    def _estampagens_dto_to_model(self, estampagemDto: EstampagensDto):
        estampagem = Estampagens()
        estampagem.iniciado = estampagemDto.iniciado
        estampagem.concluido = estampagemDto.concluido

        return estampagem
    
    # transação atomica, ou salva tudo ou não salva nada
    @transaction.atomic
    def salvar_estampagens(self, estampagemDto: EstampagensDto):
        estoque = self._estoque_dto_to_model(estampagemDto.tipo)
        estoque.save()
        estampagem = self._estampagens_dto_to_model(estampagemDto)
        estampagem.tipo = estoque
        estampagem.save()

    def get_todas_estampagens(self):
        todas_estampagens = Estampagens.objects.all()
        estampagens_dto = []
        for estampagens in todas_estampagens:
            estampagens_dto.append(self._model_to_dto(estampagens))
        return estampagens_dto

    def get_estampagens_do_usuário(self):
        estampagens_not_cancel = Estampagens.objects.exclude(status=EstampagensStatuses.CANCELADO.name)
        estampagens_dto = []
        for cada_estampagem in estampagens_not_cancel:
            estampagens_dto.append(self._model_to_dto(cada_estampagem))
        return estampagens_dto