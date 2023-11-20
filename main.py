import flet as ft

from libs.counter import (
    counterController,
    counterModel
)



def main(page: ft.Page):
    page.title = "demo"


ft.app(main)
