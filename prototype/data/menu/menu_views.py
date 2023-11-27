from data.base.view import View
from data.utils.exceptions.view_not_found import ViewNotFound
from data.menu.intro_view import IntroView


class MenuViews:
    def __init__(self):
        self.__view = None
        self.__views = []

    @property
    def view(self):
        return self.__view
    
    def select_view(self, name):
        for view in self.__views:
            view_name = view.__class__.__name__.lower().replace("view", "")
            
            if (view_name == name) and isinstance(view, View):
                self.__view = view
                return True
        return False
    
    def add_view(self, view):
        if isinstance(view, View):
            self.__views.append(view)

