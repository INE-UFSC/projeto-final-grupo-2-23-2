from data.base.view import View
from data.menu.menu_view import MenuView
from data.utils.exceptions.view_not_found import ViewNotFound
from data.menu.gameover_view import GameoverView
from data.menu.intro_config_view import IntroconfigView
from data.menu.intro_view import IntroView
from data.menu.pause_config_view import PauseconfigView
from data.menu.pause_view import PauseView
from data.menu.load_view import LoadView
from data.menu.win_view import WinView

class MenuViews:
    def __init__(self):
        self.__view = None
        self.__views = [
            GameoverView(),
            IntroconfigView(),
            IntroView(),
            PauseconfigView(),
            PauseView(),
            LoadView(),
            WinView()
        ]

    @property
    def view(self):
        return self.__view

    def select_view(self, name):
        for view in self.__views:
            view_name = view.__class__.__name__.lower().replace("view", "")

            if (view_name == name) and isinstance(view, View):
                self.__view = view
                break
        else:
            raise ViewNotFound(name)

    def add_view(self, view):
        if isinstance(view, MenuView):
            self.__views.append(view)
