# import the flet library
import flet as ft


# creating a main function
def main(page: ft.Page):
    # setting a page title
    page.title = "Hello World"

    # Flet text control -> adds the contents of the control in the page
    text = ft.Text(value='My First Flet App', color='red', weight='bold')
    # appending and updating the controls into the page
    '''
    # we cand append through 
    page.add(text)
    '''
    # we can append through like this
    page.controls.append(text)
    page.update()


# start the app
# to view in Web Browser use view=ft.WEB BROWSER
ft.app(target=main, view=ft.WEB_BROWSER)
