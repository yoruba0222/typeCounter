import flet as ft

from libs.counter.counterController import CounterController
from libs.counter.counterModel import Counter
from libs.record.recordModel import Record
from libs.record.recordController import RecordController
from libs.view import View


# インスタンスなど...
__cm: Counter
__cc: CounterController
__r: Record
__rc: RecordController

def main(page: ft.Page):
    # アプリが終了する際の処理
    def _app_close(page: ft.Page):
        __rc.save_when_quit()
        page.window_destroy()
    
    def _window_event_handler(e):
        if e.data == 'close':
            _app_close(e.page)

    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    __cm = Counter()
    __r = Record()
    
    page.add(View(__cm, __r))
    
    __cc = CounterController(__cm)
    __rc = RecordController(__cm, __r)
    
    # セーブ
    page.window_prevent_close = True
    page.on_window_event = _window_event_handler
    
    page.update()


ft.app(main)