from django.shortcuts import render
from datetime import datetime
from estampador_service.application.estampagens.estampagens_manager import EstampagensManager
from estampador_service.application.estampagens.estampagens_dto import EstampagensDto
from estampador_service.application.estoque.estoque_dto import EstoqueDto
from .repositories import EstampagensRepository
from backend.authentication.application.authentication_dto import *

def home(request):
    user_dto = AuthDto(request.user, request.user.is_superuser)
    repository = EstampagensRepository()
    manager = EstampagensManager(repository)
    res = manager.iniciar_registro_estampagem(user_dto)
    return render(request, "index.html", {'estampagens': res})

def create_new(request):
    iniciado = datetime.strptime(request.POST.get('iniciado'),  "%Y-%m-%dT%H:%M")
    concluida = datetime.strptime(request.POST.get('concluida'),"%Y-%m-%dT%H:%M")
    tipo = get_customer_from_request(request)

    dto = EstampagensDto(iniciado, concluida, tipo)
    repository = EstampagensRepository()
    manager = EstampagensManager(repository)
    res = manager.iniciar_registro_estampagem(dto)

    if res['code'] != 'SUCCESS':
        return render(request, 'index.html', {'res': res})
    else:
        return render(request, 'confirmation.html')
    
def get_customer_from_request(request):
    tipoPlaca = request.POST.get('tipoPlaca')
    quantidade = request.POST.get('quantidade')
    estoque_dto = EstoqueDto(tipoPlaca, quantidade)
    return estoque_dto