from .exceptions import *

class Placas(object): 
    tipoPlaca: str
    quantidade: int
    
    def __init__(self, tipoPlaca: str, quantidade: int) -> None:
        self.tipoPlaca = tipoPlaca
        self.quantidade = quantidade

    def is_valid(self):
        todosTiposPlacas = ["CARRO", "MOTO", "MINI13", "MINI11"]
        verificacao = (self.tipoPlaca in todosTiposPlacas)
        print("VERIFICAÇÃO :", verificacao)
        if (verificacao == False):
            raise InvalidoTipoPlaca("O tipo da placa informado não consiste no sistema!")
        elif (self.quantidade <= 0):
            raise QuantityShouldBeMoreThan0("Você não possui estoque deste tipo placa!")
        
        return True