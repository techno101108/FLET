import flet as ft
from flet import TextField,Checkbox,ElevatedButton,Text,Row,Column,OutlinedButton
from flet_core.control_event import ControlEvent


def main(page:ft.Page):
    page.title = "SignUp"
    page.theme_mode=ft.ThemeMode.DARK,ft.ThemeMode.LIGHT
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.window_width=400
    page.window_height=400
    page.window_resizable= True

    text_username=TextField(label="Username",text_align=ft.TextAlign.LEFT,width=200)
    text_password = TextField(label="Password", text_align=ft.TextAlign.LEFT, width=200)
    checkbox_signup= Checkbox(label="I agree to stuff",value=False)
    button_submit=ElevatedButton(text="Sign-Up", width=200,disabled=True)

    def validate(e:ControlEvent):
        if all([text_username.value,text_password.value,checkbox_signup.value]):
            button_submit.disabled=False
        else:
            button_submit.disabled=True
        page.update()
    def submit(e:ControlEvent):
        print('username',text_username.value)
        print('password', text_password.value)

    page.clean()
    page.add(
        Row(
            controls=[Text(value=f'welcome:{text_username.value}',size=20)],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)