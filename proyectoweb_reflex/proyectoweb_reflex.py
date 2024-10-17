
import reflex as rx 
from .components.navbar import navbar

class State(rx.State):
    pass


def index() -> rx.Component:
    return navbar()
        
    






app= rx.App()
app.add_page(index)
app._compile()


