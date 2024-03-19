import flet as ft
from flet import TextField
from flet_core.control_event import ControlEvent


def main(page: ft.Page):
    page.title = "Increment counter"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    text_number = TextField(value=0, text_align=ft.TextAlign.CENTER, width=100)

    def decrement(e:ControlEvent):
        text_number.value = str(int(text_number.value) - 1)
        page.update()

    def increment(e:ControlEvent):
        text_number.value = str(int(text_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [ft.IconButton(ft.icons.REMOVE, on_click=decrement, bgcolor=ft.colors.GREY, icon_size=20,
                           icon_color=ft.colors.BLACK, selected_icon_color=ft.colors.CYAN),
             text_number,
             ft.IconButton(ft.icons.ADD, on_click=increment, bgcolor=ft.colors.GREY, icon_size=20,
                           icon_color=ft.colors.BLACK, selected_icon_color=ft.colors.CYAN)],
            alignment=ft.MainAxisAlignment.CENTER,

        )

    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
