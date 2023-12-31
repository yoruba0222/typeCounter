# -*- coding: utf-8 -*-
import flet as ft

from libs.components.reactiveText import ReactiveText
from libs.counter.counterModel import Counter
from libs.record.recordModel import Record


class View(ft.UserControl):
    """View
    全ての見た目を決定する
    注入はmainから行う

    Attributes:
        __counter (Counter):
    """

    def __init__(self, cm: Counter, r: Record) -> None:
        """__init__
        コンストラクタ

        Args:
            cm (Counter): オブザーバ
        """
        super().__init__(self)
        # 表示機構
        self.__counter: Counter = cm
        self.__text: ReactiveText = ReactiveText(self.__counter)
        self.__counter.addObserver(self.__text)

        # セーブする
        self.__record: Record = r
        self.__counter.setCount(self.__record.getCurrentRecord())

    def build(self) -> ft:
        return ft.Row(
            [self.__text],
            alignment=ft.MainAxisAlignment.CENTER,
        )
