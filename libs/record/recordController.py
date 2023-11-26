# -*- coding: utf-8 -*-
import atexit
from libs.record.recordModel import Record


class RecordController:
    def __init__(self, r: Record):
        self.__record: Record = r
        atexit.register(self.__record.saveRecord({""}))
