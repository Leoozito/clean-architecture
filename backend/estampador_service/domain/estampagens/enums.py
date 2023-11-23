# Para definir o estado de uma estampagem
# Também para mensagem de erros
from enum import Enum

class ErrorCodes(Enum):
    REGISTERAFTERCONCLUSAO = "Não pode ser iniciado registro que ja está concluido"
    PLACASREQUIRED = "Informe o tipo da placa"
    UNDEFINED = "undefined"