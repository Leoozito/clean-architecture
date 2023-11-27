from abc import ABC, abstractclassmethod
from .estampagens_dto import EstampagensDto

class EstampagensStorage(ABC):

    @abstractclassmethod
    def salvar_estampagens(self, estampagens:EstampagensDto):
        pass

    @abstractclassmethod
    def get_todas_estampagens(self):
        pass

    @abstractclassmethod
    def get_estampagens_do_usuário(self):
        pass