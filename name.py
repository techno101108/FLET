# import libraries

import flet as ft


# creating a main function
def name(page: ft.Page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please Enter Your Name!!"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hello {name}"))


    txt_name = ft.TextField(label='Enter Your Name')
    page.add(txt_name, ft.ElevatedButton(text="say hello!", on_click=btn_click,on_focus=ft.colors.BLUE))


ft.app(target=name)
