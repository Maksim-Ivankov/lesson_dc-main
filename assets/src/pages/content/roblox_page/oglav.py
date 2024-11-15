
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
                                ft.Container(ft.Text('Средний уровень - программирование Роблокс. Создаем 3д игры в среде Роблокс на языке Луа. Для ребят 11-13 лет',size=12,color=c_white,text_align='center'),margin=ft.margin.only(left=120)),
                                ft.Container(#11
                                    ft.Row(controls=[
                                        ft.Column(controls=[
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 1. Знакомство с движком',size=12,text_align='center',height=50),width=224,data='Урок 1',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 2. Враги на острове',size=12,text_align='center',height=50),width=224,data='Урок 2',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 3. Строим дом',size=12,text_align='center',height=50),width=224,data='Урок 3',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 4. Строим город',size=12,text_align='center',height=50),width=224,data='Урок 4',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 5. Создание предметов',size=12,text_align='center',height=50),width=224,data='Урок 5',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                        ]),
                                        ft.Column(controls=[
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 6. Эффекты для блоков',size=12,text_align='center',height=50),width=224,data='Урок 6',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 7. Делаем меню',size=12,text_align='center',height=50),width=224,data='Урок 7',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 8. Телепорт',size=12,text_align='center',height=50),width=224,data='Урок 8',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 9. Килл блок',size=12,text_align='center',height=50),width=224,data='Урок 9',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 10. Смена дня и ночи',size=12,text_align='center',height=50),width=224,data='Урок 10',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                        ]),
                                        ft.Column(controls=[
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 11. Шахматы',size=12,text_align='center',height=50),width=224,data='Урок 11',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 12. Сбор яблок',size=12,text_align='center',height=50),width=224,data='Урок 12',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 13. Паркур',size=12,text_align='center',height=50),width=224,data='Урок 13',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 14. Контер страйк',size=12,text_align='center',height=50),width=224,data='Урок 14',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 15. Инвентарь',size=12,text_align='center',height=50),width=224,data='Урок 15',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                        ]),
                              
                        
                                        
                                    ]),
                                    width=800,
                                    # height=80,
                                    margin=ft.margin.only(left=90),
                                ),
                            ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                    ),expand=2
        )
        
        return self.oglav