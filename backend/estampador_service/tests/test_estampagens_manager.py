import unittest
from datetime import datetime, timedelta
import sys
sys.path.append("..")
sys.path.append("../..")
from estampador_service.application.estampagens.estampagens_storage import EstampagensStorage
from estampador_service.application.estampagens.estampagens_dto import EstampagensDto
from estampador_service.application.estampagens.estampagens_manager import EstampagensManager
from estampador_service.domain.estoque.entities import Placas
from authentication.application.authentication_dto import AuthDto

class DummyStorage(EstampagensStorage):
    def salvar_estampagens(self, estampagensDto: EstampagensDto):
        return True
    
    def get_todas_estampagens(self):
        iniciado = datetime.today()
        concluido = datetime.today() - timedelta(days=1)
        tipo = Placas("CARRO", 23)
        estampagens_dto = EstampagensDto(iniciado=iniciado, concluido=concluido, tipo=tipo)
        lista1 = estampagens_dto

        iniciado = datetime.today()
        concluido = datetime.today() - timedelta(days=1)
        tipo = Placas("CARRO", 23)
        estampagens_dto = EstampagensDto(iniciado=iniciado, concluido=concluido, tipo=tipo)
        lista2 = estampagens_dto

        duas_listas = [lista1, lista2]
        return duas_listas

    def get_estampagens_do_usuário(self):
        iniciado = datetime.today()
        concluido = datetime.today() - timedelta(days=1)
        tipo = Placas("CARRO", 23)
        estampagens_dto = EstampagensDto(iniciado=iniciado, concluido=concluido, tipo=tipo)
        
        lista1 = estampagens_dto
        return lista1
        
class EstampagensAggregateManagerTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        self.dummy_storage = DummyStorage()
        super().__init__(methodName)

    def register_date_cannot_be_after_conclusion2(self):
        iniciado = datetime.today()
        concluido = datetime.today() - timedelta(days=1)
        tipo = Placas("CARRO", 23)
        estampagens_dto = EstampagensDto(iniciado=iniciado, concluido=concluido, tipo=tipo)
        manager = EstampagensManager(self.dummy_storage)
        res = manager.iniciar_registro_estampagem(estampagens_dto)
        print("RESPOSTA: ", res)
        self.assertEqual(res['code'], "REGISTERAFTERCONCLUSAO")

    def test_get_estampagens_user_admin(self):
        manager = EstampagensManager(self.dummy_storage)     
        user_dto = AuthDto('admin', True)
        estampagens = manager.get_estampagens(user_dto)
        self.assertEqual(len(estampagens), 2)

    def test_get_estampagens_user_NOT_admin(self):
        manager = EstampagensManager(self.dummy_storage)     
        user_dto = AuthDto('no_admin', False)
        estampagens = manager.get_estampagens(user_dto)
        self.assertEqual(len(estampagens), 1)
