# -*- coding: utf-8 -*-
import flet as ft

from libs.components import reactiveText
from libs.counter import (
    counterController,
    counterModel
)


class View(ft.UserControl):
    def build():
        return ft.Container()