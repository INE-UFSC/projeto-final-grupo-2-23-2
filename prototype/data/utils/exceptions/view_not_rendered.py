class ViewNotRendered(Exception):
    def __init__(self, view):
        message = f"view {view} was not able to render, fix the code"
        super().__init__(message)
