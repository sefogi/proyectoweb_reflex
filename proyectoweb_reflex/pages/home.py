import reflex as rx 


@rx.page(route="/", text='Inicio')
def home()-> rx.Component:
    return rx.box(
        rx.slider(
            rx.image(src="")
        )
    )