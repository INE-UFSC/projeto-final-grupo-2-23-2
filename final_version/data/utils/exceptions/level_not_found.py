class LevelNotFound(Exception):
    def __init__(self, level):
        message = f"{level} is not a level that belong to levels, fix the code"
        super().__init__(message)