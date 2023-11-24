from estampador_service.application.estoque.estoque_dto import EstoqueDto
from estampador_service.application.estampagens.estampagens_dto import EstampagensDto
from .models import Estoque, Estampagens
from django.db import transaction
from estampador_service.application.estampagens.estampagens_storage import EstampagensStorage

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
        estampagem.status = estampagemDto.status

        return estampagem
    
    # transação atomica, ou salva tudo ou não salva nada
    @transaction.atomic
    def salvar_estampagem(self, estampagemDto: EstampagensDto):
        estoque = self._estoque_dto_to_model(estampagemDto.tipo)
        estoque.save()
        estampagem = self._estampagens_dto_to_model(estampagemDto)
        estampagem.tipo = estoque
        estampagem.save()