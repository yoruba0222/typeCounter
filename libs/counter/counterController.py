# -*- coding: utf-8 -*-
from pynput import keyboard

from libs.counter.counterModel import Counter


class CounterController:
    """CounterController
    ユーザからのキーボード入力を受け取ってモデルの状態を変更するクラス

    Attributes:
        __counter (Counter): Counterインスタンス
    """
    def __init__(self, counter: Counter) -> None:
        """__init__
        コンストラクタ

        Args:
            counter (Counter): counterModelのCounterクラスのインスタンス
        """
        self.__counter: Counter = counter

        with keyboard.Listener(on_press=self._incrementCount) as listener:
            listener.join()

    def _incrementCount(self, e) -> None:
        """_incrementCount
        Counterインスタンスのタイプ数を1増やす
        """
        self.__counter.increment()
        print("うんこ")
        