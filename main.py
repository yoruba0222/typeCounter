import flet as ft

from libs.counter import (
    counterController,
    counterModel
)



def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


ft.app(main)
