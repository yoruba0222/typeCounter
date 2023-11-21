# -*- coding: utf-8 -*-
import flet as ft

from libs.observer.observer import Observer
from libs.counter.counterModel import Counter


class ReactiveText(ft.UserControl, Observer):
    """ReactiveText
    subjectのからの通知に合わせて自動的に更新するテキスト

    Attributes:
        control (ft.Text): fletのテキストの実態
        counter (Counter): subjectであるcounterの実態
    """
    def __init__(self, counter: Counter) -> None:
        """__init__
        コンストラクタ

        Args:
            counter (Counter): 通知対象のCounterインスタンスから値を取るためにオブジェクトを取得しておく
        """
        super().__init__()
        self.control: ft.Text = ft.Text('')
        self.counter: Counter = counter
        
    def update(self):
        """update
        自身のテキストを更新する
        """
        self.control.value = self.counter.getCount()
        self.control.update()
    
    def build(self) -> None:
        """build
        fletで自作コンポーネントを作るのに必要
        """
        return self.control