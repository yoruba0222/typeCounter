from pprint import pprint
from libs.record.recordModel import Record


def test_save():
    r = Record()

    r.saveRecord({"today_count": 0})

    r2 = Record()

    assert r2.getCurrentRecord().get("today_count") == 0
