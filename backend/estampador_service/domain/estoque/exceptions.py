class InvalidoTipoPlaca(Exception):
    def __init__(self, message):
        self.message = message

class QuantityShouldBeMoreThan0(Exception):
    def __init__(self, message):
        self.message = message