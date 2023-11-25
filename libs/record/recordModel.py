# -*- coding: utf-8 -*-
from typing import Final
import typeCounter_pb2
import datetime


FILENAME: Final[str] = "./data.pb"

class Record():
    """Record
    過去の記録の読み書きを担当する

    Attribute:
        __tc (typeCounter_pb2.typeCount): pbのクラス
        __todayCount (int): 今日タイプした回数
    """
    def __init__(self) -> None:
        """コンストラクタ
        現在の統計情報を読み込む
        なければ作る
        """
        self.__tc: typeCounter_pb2.typeCount = typeCounter_pb2.typeCount()
        self.__todayCount: int = 0

        try:
            # ファイルが存在しているなら読み込んじゃう
            __f = open(FILENAME, "rb")
            self.__tc.ParseFromString(__f.read())
            self.__todayCount = self.__tc.count
            
        except FileNotFoundError as e:
            # ファイルが存在しない(データを削除したか，初利用)
            __f = open(FILENAME, "wb")
            self.__tc.count = 0
            __feed_data: str = self.__tc.SerializeToString()
            __f.write(__feed_data)

        finally:
            __f.close()

    # get past record by date (yyyy-mm-dd)
    def getPastRecord(self, date: str) -> dict:
        pass

    def saveRecord(self, data: dict) -> None:
        pass