import reflex as rx 



def navbar()->rx.Component:
    return rx.hstack(
        rx.text("Sebastian Forero",color="white", justify_content="end",font_size="2.0em",height="40px"),
        position="sticky",
        bg="blue",
        padding_x="16px",
        padding_y="8px",
        z_index="999"
    )