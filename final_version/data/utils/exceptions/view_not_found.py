class ViewNotFound(Exception):
    def __init__(self, view):
        message = f"{view} is not a view that belong to views, fix the code"
        super().__init__(message)