# -*- coding: utf-8 -*-
import abc

from observer import Observer


class Subject(metaclass=abc.ABCMeta):
    """Subject
    サブジェクト
    オブザーバーに値の変更があれば通知する
    登録したオブザーバを管理するのはリストが望ましい

    Args:
        metaclass (_type_, optional): インタフェース
        
    Raises:
        NotImplementedError: メソッドが定義されていない
    """
    @abc.abstractmethod
    def addObserver(self, observer: Observer) -> None:
        """addObserver
        値の変更を通知するobserverを登録

        Args:
            observer (Observer):  登録したいobserverのインスタンス

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError()
    
    @abc.abstractmethod
    def notifyObservers(self) -> None:
        """notifyObservers
        登録したオブザーバに値の変更を通知する

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError()
    
    @abc.abstractmethod
    def removeObserver(self) -> None:
        """removeObservers
        登録したオブザーバを削除する

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError()