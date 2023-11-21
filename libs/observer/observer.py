# -*- coding: utf-8 -*-
import abc


class Observer(metaclass=abc.ABCMeta):
    """Observer
    オブザーバ
    サブジェクトからの値変更通知を受け取り値を変更する

    Args:
        metaclass (_type_, optional): インタフェース

    Raises:
        NotImplementedError: メソッドが定義されていない
    """
    @abc.abstractmethod
    def update(self) -> None:
        """update
        現在の状態をアップデートする

        Raises:
            NotImplementedError: メソッドが定義されていない
        """
        raise NotImplementedError()