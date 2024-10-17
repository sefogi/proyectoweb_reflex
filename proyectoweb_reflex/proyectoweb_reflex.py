
import reflex as rx 

class State(rx.State):
    pass


def index() -> rx.Component:
    
    return rx.center(
        rx.text("hola reflex", color="blue", text_align="center",font_size="2em")
        
    )






app= rx.App()
app.add_page(index)
app._compile()


