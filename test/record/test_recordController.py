# -*- coding: utf-8 -*-
import signal
from libs.record.recordModel import Record
from libs.record.recordController import RecordController
from libs.counter.counterModel import Counter


def test_l():
    c = Counter
    r = Record()
    rc = RecordController(c, r)
    
    print(type(rc.set_save))
    
    assert 10 == 10