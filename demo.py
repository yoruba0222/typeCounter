#python
import flet as ft

def main(page: ft.Page):

    set_page(page)
    page.add(
        ft.ElevatedButton(
            text='押すと終了',
            on_click=lambda e: app_close(e.page)
        )
    )


def set_page(page: ft.Page):
    '''
    画面全体の初期設定
    '''
    def window_event_handler(e):
        if e.data == 'close':
            app_close(e.page)

    def on_disconnect_handler(e):
        app_close(e.page)

    page.title = "test"

    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.window_width = 300
    page.window_height = 200
    page.window_left = 100
    page.window_top = 400

    page.window_prevent_close = True
    page.on_window_event = window_event_handler

    page.update()

def app_close(page: ft.Page):
    print('終了前に必要な処理はここでしてね！')
    page.window_destroy()


if __name__ == '__main__':
    '''
    エントリーポイント
    '''
    ft.app(target = main)
    # ft.app(target=main, view=ft.WEB_BROWSER)