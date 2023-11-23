# Casos de uso: Para criar uma estampagem, deletar estampagem, alterar estampagem.
from estampador_service.application.estampagens.estampagens_dto import EstampagensDto
from estampador_service.domain.estampagens.enums import ErrorCodes
from estampador_service.domain.estampagens.exceptions import RegisterDateCannotAfterConclusaoDate, PlacasCannotBeForgotten

class EstampagensManager(object):
    def iniciar_registro_estampagem(self, estampagensDto: EstampagensDto):
        domain_object = estampagensDto.to_domain()

        try:
            if domain_object.is_valid():
                return "save"
        except RegisterDateCannotAfterConclusaoDate as e:
            return {"message": e.message, 'code': ErrorCodes.REGISTERAFTERCONCLUSAO}
        except PlacasCannotBeForgotten as e:
            return {"message": e.message, 'code': ErrorCodes.PLACASREQUIRED}
        # except Exception as e:
        #     return {"message": e.message, "code": ErrorCodes.UNDEFINED}