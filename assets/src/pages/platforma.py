import flet as ft
from assets.variable import *
from assets.imports import *

from assets.src.pages.menu.menu import Menu
from assets.src.pages.content.main_page.main_page import Main_page
from assets.src.pages.content.maincraft_page.maincraft_page import Maincraft_page
from assets.src.pages.content.roblox_page.roblox_page import Roblox_page
from assets.src.pages.content.scrach_page.scrach_page import Scrach_page
from assets.src.pages.content.web_page.web_page import Web_page


class Platforma(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
        self.page_one = 'Главная'

    # запуск в потоке пересчета времени
    def did_mount(self):
        self.running = True
        self.myThread = threading.Thread(target=self.update_data, args=(), daemon=True)
        self.myThread.start()

    #то что крутится в потоке - пересчет времени 
    def update_data(self):
        while self.running:
            self.controls[0].content.controls[0].content.controls[0].content.controls[0].content.controls[3].content.controls[0].content.controls[0].controls[1].value = time.strftime("%d.%m.%Y г. %H:%M:%S", time.localtime())
            time.sleep(1)
            self.controls[0].content.controls[0].content.controls[0].content.controls[0].content.controls[3].content.controls[0].content.controls[0].controls[1].update()

    def build(self):
        # отрисовка страницы согласно выбранному пункту меню
        def print_window(page,punkt_menu):
            platforma = ft.Container(
                ft.Row(
                    controls=[
                        ft.Container(
                            content=Menu(self.page,callback,punkt_menu),
                        ),
                        ft.Container(
                            expand=2, content=page
                        ),
                    ]),
            )
            return platforma
        
        # выбор пункта меню
        def callback(punkt_menu=self.page_one):
            self.page_select = punkts[punkt_menu]
            self.controls = []
            self.update()
            self.controls.append(print_window(self.page_select,punkt_menu))
            self.update()

        
        punkts = {
                'Главная':Main_page(),
                'Майнкрафт':Maincraft_page(),
                'Роблокс':Roblox_page(),
                'Скрейч':Scrach_page(),
                'WEB':Web_page(),

            }

        self.page_select = punkts[self.page_one]
        
        return print_window(self.page_select,self.page_one)