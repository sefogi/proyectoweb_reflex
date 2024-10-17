
import reflex as rx 
from .components.navbar import navbar
from .pages.home import home

class State(rx.State):
    pass


def index() -> rx.Component:
    return navbar(), home()

        
    






app= rx.App()
app.add_page(index)
app._compile()


