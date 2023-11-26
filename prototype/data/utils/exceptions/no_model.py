class NoModel(Exception):
    def __init__(self):
        message = "model is equal None, fix the code"
        super().__init__(message)