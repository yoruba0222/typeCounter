from pprint import pprint
from ...libs.record.recordModel import Record


r = Record()

pprint(r.getCurrentRecord())

r.saveRecord({"today_count": 10})

r2 = Record()

pprint(r.getCurrentRecord())
