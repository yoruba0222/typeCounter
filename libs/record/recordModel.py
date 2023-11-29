# -*- coding: utf-8 -*-
from typing import Final
from libs.record import typeCounter_pb2
import datetime


FILENAME: Final[str] = "./data.pb"


class Record:
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
            # クローズ
            __f.close()

    # get currnet record
    def getCurrentRecord(self) -> dict:
        """getCurrentRecord
        現在の記録をリターンする

        Returns:
            dict: 現在の記録
        """
        __tmp_dict: dict = {"today_count": self.__todayCount}
        return __tmp_dict

    # get past record by date (yyyy-mm-dd)
    def getPastRecord(self, date: str) -> dict:
        pass

    def saveRecord(self, data: dict) -> None:
        """saveRecord
        引数で与えた状態を保存する

        Args:
            data (dict): 保存して欲しい記録
        """
        try:
            # 保存している
            __f = open(FILENAME, "wb")
            __tc_tmp: typeCounter_pb2.typeCount = typeCounter_pb2.typeCount()
            __tc_tmp.count = data.get("today_count")
            __feed_data: str = __tc_tmp.SerializeToString()
            __f.write(__feed_data)
            self.__todayCount = data.get("today_count")

        except Exception as e:
            # エラーが出る
            print("エラー出てるよ:", e)

        finally:
            # ファイルインスタンスを閉じる
            __f.close()
