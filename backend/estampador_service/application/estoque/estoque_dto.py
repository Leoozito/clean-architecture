from estampador_service.domain.estoque.entities import Placas

class EstoqueDto(object):
    tipoPlaca: str
    quantidade: int

    def __init__(self, tipoPlaca: str, quantidade: int):
        self.tipoPlaca = tipoPlaca
        self.quantidade = quantidade

    def to_domain(self):
        estoque = Placas(self.tipoPlaca, self.quantidade)
        return estoque

    def to_dto(self, customer: Placas):
        return EstoqueDto(
            tipoPlaca=customer.tipoPlaca, 
            quantidade=customer.quantidade,
        )