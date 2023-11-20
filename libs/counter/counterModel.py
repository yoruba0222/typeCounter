# -*- coding: utf-8 -*-


class Counter:
    """Counter
    現在のタイプ数関連の情報を保持するクラス

    Attributes:
        __count (int): 現在のタイプ数
    """

    __count: int = 0

    def increment(self) -> None:
        """現在のタイプ数を1増やす"""
        self.__count += 1

    def getCount(self) -> int:
        """現在のタイプ数を返す

        Returns:
            int: 現在のタイプ数
        """
        return self.__count
