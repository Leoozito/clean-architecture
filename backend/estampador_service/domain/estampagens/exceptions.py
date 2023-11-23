class RegisterDateCannotAfterConclusaoDate(Exception):
    def __init__(self, message):
        self.message = message

class PlacasCannotBeForgotten(Exception):
    def __init__(self, message):
        self.message = message    