import flet as ft

from libs.counter.counterController import CounterController
from libs.counter.counterModel import Counter
from libs.view import View


# インスタンスなど...
__cm: Counter
__cc: CounterController

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    __cm= Counter()
    
    page.add(View(__cm))
    
    __cc = CounterController(__cm)


ft.app(main)