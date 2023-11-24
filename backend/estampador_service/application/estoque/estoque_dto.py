class EstoqueDto(object):
    tipoPlaca: str
    quantidade: int

    def __init__(self, tipoPlaca: str, quantidade: int) -> None:
        self.tipoPlaca = tipoPlaca
        self.quantidade = quantidade