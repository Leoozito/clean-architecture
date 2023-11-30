import unittest
from datetime import datetime, timedelta
import sys
sys.path.append("..")
sys.path.append("../..")
from estampador_service.domain.estoque.entities import Placas
from estampador_service.domain.estampagens.entities import Estampagens
from domain.estampagens.exceptions import RegisterDateCannotAfterConclusaoDate
from application.estampagens.estampagens_manager import EstampagensManager
from application.estampagens.estampagens_dto import EstampagensDto
from application.estoque.estoque_dto import EstoqueDto
from estampador_service.domain.estoque.entities import Placas
from tests.test_estampagens_manager import DummyStorage

class EstampagensTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        self.dummy_storage = DummyStorage()
        super().__init__(methodName)

    def register_date_cannot_be_after_conclusion(self):
        iniciado = datetime.today()
        concluido = datetime.today() - timedelta(days=1)
        tipo = Placas()
        estampagens = Estampagens(iniciado=iniciado, concluido=concluido, tipo=tipo)

        with self.assertRaises(RegisterDateCannotAfterConclusaoDate) as ex:
            estampagens.is_valid()

        exception = ex.exception
        self.assertEqual(exception.message, "É necessário informar a placa")

    def register_date_cannot_be_after_conclusion2(self):
        iniciado = datetime.today()
        concluido = datetime.today() - timedelta(days=1)
        tipo = Placas()
        estampagens = Estampagens(iniciado=iniciado, concluido=concluido, tipo=tipo)

        self.assertRaises(RegisterDateCannotAfterConclusaoDate, estampagens.is_valid)

    def test_create(self): 
        iniciado = datetime.today()
        concluido = datetime.utcnow()
        tipo = Placas("CARRO", 23)
        estampagens_dto = EstampagensDto(iniciado=iniciado, concluido=concluido, tipo=tipo)
        manager = EstampagensManager(self.dummy_storage)
        res = manager.iniciar_registro_estampagem(estampagens_dto)
        self.assertEqual(res['code'], "SUCESS")

    def test_register_should_be_number_AE(self): 
        iniciado = datetime.today()
        concluido = datetime.utcnow()
        tipo = Placas("MOTO", 0)
        estampagens_dto = EstampagensDto(iniciado=iniciado, concluido=concluido, tipo=tipo)
        manager = EstampagensManager(self.dummy_storage)
        res = manager.iniciar_registro_estampagem(estampagens_dto)
        self.assertEqual(res['code'], "REGISTERSSHOULDBENUMBERAE")

    def test_invalid_register(self): 
        iniciado = datetime.today()
        concluido = datetime.utcnow()
        tipo = Placas("BLA BLA", 0)
        estampagens_dto = EstampagensDto(iniciado=iniciado, concluido=concluido, tipo=tipo)
        manager = EstampagensManager(self.dummy_storage)
        res = manager.iniciar_registro_estampagem(estampagens_dto)
        self.assertEqual(res['code'], "INVALIDREGISTER")
    
    def test_user_not_allowed_to_access_data(self): 
        iniciado = datetime.today()
        concluido = datetime.utcnow()
        tipo = Placas("CARRO", 0)
        estampagens_dto = EstampagensDto(iniciado=iniciado, concluido=concluido, tipo=tipo)
        manager = EstampagensManager(self.dummy_storage)
        res = manager.iniciar_registro_estampagem(estampagens_dto)
        self.assertEqual(res['code'], "USERNOTALLOWEDTOACCESSDATA")

if __name__ == "__main__":
    unittest.main()
