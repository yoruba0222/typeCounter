# -*- coding: utf-8 -*-
from typing import Any, List, Optional, Union
import flet as ft
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue

from libs.components.reactiveText import ReactiveText
from libs.counter import (
    counterController,
    counterModel
)


class View(ft.UserControl):
    def __init__(self,):
        super().__init__(self)
    
    def build():
        return ft.Container(ReactiveText())