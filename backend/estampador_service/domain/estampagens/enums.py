# Para definir o estado de uma estampagem
# Também para mensagem de erros
from enum import Enum

class ErrorCodes(Enum):
    REGISTERAFTERCONCLUSAO = "Não pode ser iniciado registro que ja está concluido"
    PLACASREQUIRED = "Informe o tipo da placa"
    REGISTERSSHOULDBENUMBERAE = 'Informe o número de autorização para realizar a estampagem'
    TIPOPLACAINVALIDO = 'Este tipo de placa é invalido'
    USERNOTALLOWEDTOACCESSDATA = 'O usuário não tem permissão para acessar esses dados'
    REGISTERSREQUIREDTIPOPLACA = 'Informe o tipo da placa para atualizar o registro'
    REGISTERSTATUSDOESNOTALLOWDELETE = 'Não é possivel deletar o registro, pois já está concluido'
    UNDEFINED = "undefined"

class SuccessCodes(Enum):
    SUCCESS = 'Success'

class BookingStatuses(Enum):
    EM_ESTAMPAGEM = 0
    INICIADO = 1 
    CONCLUIDO = 2
    CANCELADO = 3