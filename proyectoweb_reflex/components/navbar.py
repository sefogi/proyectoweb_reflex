import reflex as rx 

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/favicon.ico",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("About", "/#"),
                    navbar_link("Portfolio", "/#"),
                    navbar_link("Contact", "/#"),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/favicon.ico",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        padding= "5px"
                        rx.icon("menu", size=40)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home",),
                        rx.menu.item("About"),
                        rx.menu.item("Portfolio"),
                        rx.menu.item("Contact"),
                        
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="end",
            ),
        ),
        bg=rx.color("red", 9),
        padding="2em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )

# def navbar()->rx.Component:
#     return rx.hstack(
#         rx.text("Sebastian Forero",color="white", justify_content="end",font_size="2.0em",height="40px"),
#         position="sticky",
#         bg="blue",
#         padding_x="16px",
#         padding_y="8px",
#         z_index="999"
#     )