# -*- coding: utf-8 -*-
import abc

from observer import Observer


class Subject(metaclass=abc.ABCMeta):
    """Subject
    サブジェクト

    Args:
        metaclass (_type_, optional): インタフェース
    """
    @abc.abstractmethod
    def addObserver(self, observer: Observer) -> None:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def notifyObservers(self) -> None:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def removeObserver(self) -> None:
        raise NotImplementedError()