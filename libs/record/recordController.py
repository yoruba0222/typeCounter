# -*- coding: utf-8 -*-
import signal
from libs.record.recordModel import Record
from libs.counter.counterModel import Counter


class RecordController:
    def __init__(self, c: Counter, r: Record) -> None:
        self.__record: Record = r
        self.__counter: Counter = c
    
    def save_when_quit(self) -> None:
        self.__record.saveRecord({"today_count": self.__counter.getCount()})
