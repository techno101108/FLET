import flet as ft


def fruits(page: ft.Page):
    page.title = "Fruits"
    page.add(
        # Below example is row control
        ft.Row(controls=[
            ft.Text("My Favourite Fruits")
        ]),
        ft.Row(controls=[
            ft.Text("Apple"),
            ft.Text("Banana"),
            ft.Text("cherry"),
            ft.Text("Berry"),
        ]),
        # Below example is row control
        ft.Column(
            controls=[ft.Text("My Favourite Fruits")
                      ]),
        ft.Column(controls=[
            ft.Text("Apple"),
            ft.Text("Banana"),
            ft.Text("cherry"),
            ft.Text("Berry"),
        ])

    )


ft.app(target=fruits)
