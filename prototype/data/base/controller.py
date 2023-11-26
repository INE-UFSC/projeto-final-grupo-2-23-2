from data.utils.exceptions.no_model import NoModel
from data.utils.exceptions.no_view import NoView
from data.base.model import Model
from data.base.view import View


from abc import ABC, abstractmethod

class Controller(ABC):
    def __init__(self):
        self.__model = None
        self.__view = None

    @property
    def model(self) -> Model:
        if self.__model != None:
            return self.__model
        else:
            raise NoModel
    
    @model.setter
    def model(self, model: Model) -> None:
        if isinstance(model, Model):
            self.__model = model
        else:
            raise NoModel
    
    @property
    def view(self) -> Model:
        if self.__view != None:
            return self.__view
        else:
            raise NoView
    
    @view.setter
    def view(self, view: View) -> None:
        if isinstance(view, View):
            self.__view = view
        else:
            raise NoView
    
    @abstractmethod
    def run(self):
        pass