import flet as ft 

def todo(page:ft.Page):
    page.title ='Todo App'
    page.appbar =ft.AppBar(
        # leading=ft.Icon(ft.icons.IMAGE()),
        leading_width=40,
        bgcolor=ft.colors.GREY_200,
        title=ft.Text("TODO APP",font_family="TimesNewRoman"),
        center_title=False,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.MenuItemButton(content=ft.Text("Menu"),disabled=False)
        ]
    )

    txt_name = ft.TextField(label='Enter Your Name')
    page.add(txt_name)


ft.app(target=todo)