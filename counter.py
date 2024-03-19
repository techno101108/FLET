# import libraries

from time import sleep

import flet as ft


# creating a main function
def counter(page: ft.Page):
    # setting the page title
    page.title = 'Counter App'

    # flet control
    text_numer = ft.Text(text_align=ft.TextAlign.CENTER,size=20)
    # num =ft.Text()
    # append controls to page
    page.add(text_numer)
    for i in range(1,11):
        # str is used to convert int to string
        text_numer.value = "count" + str(i)
        page.update()
        # it will take the parameter in seconds
        sleep(1)
        # it checks the value of variable i
        if (i == 10):
            # it automatically closes the window if condition satisfied
            page.window_close()



ft.app(target=counter)
