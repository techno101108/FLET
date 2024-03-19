# import libraries

import flet as ft


# defining the main function
def main(page: ft.Page):
    page.title = "TO DO Application"
    input_text = ft.TextField(hint_text="Enter the Task.")
    def btn_click(e):
        if not input_text.value:
            input_text.error_text = "PLEASE ENTER TASK TO ADD"
            page.update()
        else:
            page.add(ft.Checkbox(label=input_text.value))
            input_text.value=""
            page.update()
    page.add(
             ft.Row(
                 controls=[input_text,ft.FloatingActionButton(text="ADD",on_click=btn_click
                    #   ft.ElevatedButton(text="ADD",on_click=btn_click
                                   )]
             )
             )


ft.app(target=main)
