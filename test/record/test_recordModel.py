from pprint import pprint
from libs.record.recordModel import Record


def test_save():
    r2 = Record()
    
    r2.saveRecord({"today_count": 0})

    assert r2.getCurrentRecord().get("today_count") == 10
