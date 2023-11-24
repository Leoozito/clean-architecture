import unittest
from datetime import datetime, timedelta
import sys
sys.path.append("..")
sys.path.append("../..")
from estampador_service.application.estampagens.estampagens_storage import EstampagensStorage
from estampador_service.application.estampagens.estampagens_dto import EstampagensDto
from estampador_service.application.estampagens.estampagens_manager import EstampagensManager
from estampador_service.domain.estoque.entities import Placas

class DummyStorage(EstampagensStorage):
    def salvar_estampagem(self, estampagensDto: EstampagensDto):
        return True
    
class EstampagensAggregateManagerTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        self.dummy.storage = DummyStorage()
        super().__init__(methodName)

    def register_date_cannot_be_after_conclusion2(self):
        iniciado = datetime.today()
        concluido = datetime.today() - timedelta(days=1)
        tipo = Placas("CARRO", 23)
        estampagens_dto = EstampagensDto(iniciado=iniciado, concluido=concluido, tipo=tipo)
        manager = EstampagensManager(self.dummy.storage)
        res = manager.iniciar_registro_estampagem(estampagens_dto)
        self.assertEqual(res['code'], "REGISTERAFTERCONCLUSAO")