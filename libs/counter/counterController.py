# -*- coding: utf-8 -*-
from pynput import keyboard

from libs.counter.keyModel import Counter


class CounterController:
    """CounterController
    ユーザからのキーボード入力を受け取ってモデルの状態を変更するクラス

    Attributes:
        __counter (Counter): Counterインスタンス
    """

    self.__counter: Counter = None

    def __init__(self, counter: Counter) -> None:
        """__init__
        コンストラクタ

        Args:
            counter (Counter): counterModelのCounterクラスのインスタンス
        """
        self.__counter = counter

        with keyboard.Listener(on_press=_incrementCount) as listener:
            listener.join()

    def _incrementCount(self) -> None:
        """_incrementCount
        Counterインスタンスのタイプ数を1増やす
        """
        __counter.increment()
