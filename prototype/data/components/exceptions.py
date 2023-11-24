class ScreenNotFound(Exception):
    def __init__(self, screen):
        message = f"screen {screen} not found, fix the code"
        super().__init__(message)

class ScreenNotRunned(Exception):
    def __init__(self, screen):
        message = f"screen {screen} was not able to run"
        super().__init__(message)