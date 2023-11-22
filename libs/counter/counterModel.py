# -*- coding: utf-8 -*-
from libs.observerInterface.observer import Observer
from libs.observerInterface.subject import Subject




class Counter(Subject):
    """Counter
    現在のタイプ数関連の情報を保持するクラス

    Attributes:
        __count (int): 現在のタイプ数
        __observerList (list[Observer]): オブザーバリスト
    """
    def __init__(self) -> None:
        """__init__
        コンストラクタ
        """
        self.__observerList: list[Observer] = []
        self.__count: int = 0
    
    def increment(self) -> None:
        """increment
        現在のタイプ数を1増やす
        """
        self.__count += 1
        self.notifyObservers()

    def getCount(self) -> int:
        """getCount
        現在のタイプ数を返す

        Returns:
            int: 現在のタイプ数
        """
        return self.__count
    
    #
    # over load methods
    #
    def addObserver(self, ob: Observer) -> None:
        """addObserver
        オブザーバを登録する

        Args:
            ob (Observer): 登録したいオブザーバ
        """
        self.__observerList.append(ob)
        
    def notifyObservers(self) -> None:
        """notifyObservers
        登録している全てのオブザーバに値の変更を通知する
        """
        [ob.update() for ob in self.__observerList]
    
    def removeObserver(self) -> None:
        """removeObserver
        登録している全てのオブザーバを削除する
        """
        self.__observerList.clear()