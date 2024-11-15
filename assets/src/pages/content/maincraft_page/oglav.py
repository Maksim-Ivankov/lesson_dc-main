
import flet as ft
from assets.variable import *
from assets.imports import *


class Oglav(ft.UserControl):
    def __init__(self,change_page):
        super().__init__()
        self.change_page = change_page

    def build(self):
        
        self.oglav = ft.Container(
            ft.Container(
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(ft.Text('Средний уровень - программирование Роблокс. Создаем 3д игры в среде Роблокс на языке Луа. Для ребят 11-13 лет',size=12,color=c_white,text_align='center'),margin=ft.margin.only(left=0)),
                                ft.Container(#11
                                    ft.Row(controls=[
                                        ft.Column(controls=[
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 1. Установка Minecraft',size=12,text_align='center',height=50),width=250,data='Урок 1',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 2. Перемещение персонажа',size=12,text_align='center',height=50),width=250,data='Урок 2',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 3. Телепортация по кругу',size=12,text_align='center',height=50),width=250,data='Урок 3',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 4. Постройка дома',size=12,text_align='center',height=50),width=250,data='Урок 4',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ]),
                                        ft.Column(controls=[
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 5. Случайные числа и чат',size=12,text_align='center',height=50),width=250,data='Урок 5',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 6. Умное перемещение',size=12,text_align='center',height=50),width=250,data='Урок 6',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 7. Умное строительство',size=12,text_align='center',height=50),width=250,data='Урок 7',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 8. Блок под ногами игрока',size=12,text_align='center',height=50),width=250,data='Урок 8',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ]),
                                       
                              
                        
                                        
                                    ]),
                                    width=400,
                                    # height=80,
                                    margin=ft.margin.only(left=90),
                                ),
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.oglav