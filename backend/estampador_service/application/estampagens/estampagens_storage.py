from abc import ABC, abstractclassmethod
from .estampagens_dto import EstampagensDto

class EstampagensStorage(ABC):

    @abstractclassmethod
    def salvar_estampagens(self, estampagens:EstampagensDto):
        pass