from django.shortcuts import render
from datetime import datetime
from estampador_service.application.estampagens.estampagens_manager import EstampagensManager
from estampador_service.application.estampagens.estampagens_dto import EstampagensDto
from estampador_service.application.estoque.estoque_dto import EstoqueDto

def home(request):
    estoque_dto = EstoqueDto()
    estoque_dto.name = "Leonardo"
    dto = EstampagensDto(datetime.today(), datetime.today(), estoque_dto)
    res = EstampagensManager().iniciar_registro_estampagem(dto)
    return render(request, "index.html", {"res": res})