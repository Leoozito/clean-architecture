from django.shortcuts import render
from datetime import datetime
from estampador_service.application.estampagens.estampagens_manager import EstampagensManager
from estampador_service.application.estampagens.estampagens_dto import EstampagensDto
from estampador_service.application.estoque.estoque_dto import EstoqueDto
from .repositories import EstampagensRepository

def home(request):
    estoque_dto = EstoqueDto()
    estoque_dto.name = "Leonardo"
    dto = EstampagensDto(datetime.today(), datetime.today(), estoque_dto)
    res = EstampagensManager().iniciar_registro_estampagem(dto)
    return render(request, "index.html", {"res": res})

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
    quantidade = int(request.POST.get('quantidade'))
    estoque_dto = EstampagensDto(tipoPlaca, quantidade)
    return estoque_dto