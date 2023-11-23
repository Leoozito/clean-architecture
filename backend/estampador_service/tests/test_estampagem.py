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

class EstampagensTest(unittest.TestCase):

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
        tipo = Placas()
        estampagens_dto = EstampagensDto(iniciado=iniciado, concluido=concluido, tipo=tipo)
        manager = EstampagensManager()
        res = manager.iniciar_registro_estampagem(estampagens_dto)
        self.assertEqual(res, "save")

if __name__ == "__main__":
    unittest.main()
