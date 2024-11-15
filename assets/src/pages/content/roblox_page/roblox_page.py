
import flet as ft
from assets.variable import *
from assets.imports import *

from assets.src.pages.content.roblox_page.oglav import Oglav
from assets.src.pages.content.roblox_page.print_lesson import Print_lesson

class Roblox_page(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def change_page(self,e):
        self.controls = []
        self.controls.append(self.print_page(e.control.data))
        self.update()

    def print_page(self,page):

        pages_list={
            'Оглавление':Oglav(self.change_page),
            'Урок 1': Print_lesson(page),
            'Урок 2': Print_lesson(page),
            'Урок 3': Print_lesson(page),
            'Урок 4': Print_lesson(page),
            'Урок 5': Print_lesson(page),
            'Урок 6': Print_lesson(page),
            'Урок 7': Print_lesson(page),
            'Урок 8': Print_lesson(page),
            'Урок 9': Print_lesson(page),
            'Урок 10': Print_lesson(page),
            'Урок 11': Print_lesson(page),
            'Урок 12': Print_lesson(page),
            'Урок 13': Print_lesson(page),
            'Урок 14': Print_lesson(page),
            'Урок 15': Print_lesson(page),
        }
  
        if page == 'Оглавление': title_print = 'Учебник Роблокс'
        else: title_print = 'Учебник Роблокс | ' + page


        self.scrach_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(
                                    ft.Text(title_print,color=c_blue),
                                    alignment=ft.alignment.center
                                    
                        ),
                        bgcolor=c_yelow,
                        height=28,
                        margin=ft.margin.only(top=-10,left=-10,right=-10),
                        border = ft.border.all(1,c_white),
                        
                    ),
                    ft.Container(
                        ft.Column(controls=[
                            pages_list[page]
                        ],scroll=ft.ScrollMode.ALWAYS),
                        expand=2,
                    )
                ]
            ),expand=2
        )
        
        return self.scrach_page


    def build(self):
        
        # return self.print_page('Урок 1')
        # return self.print_page('Урок 15')
        return self.print_page('Оглавление')
        