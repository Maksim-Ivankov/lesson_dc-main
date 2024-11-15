
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
                                ft.Container(ft.Text('Старший уровень программирования - Делаем вообще все, получаем профессию. Для ребят 8-11 клссов',size=12,color=c_white,text_align='center'),margin=ft.margin.only(left=120)),
                                ft.Container(#11
                                    ft.Row(controls=[
                                        ft.Column(controls=[
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nHTML 1. Введение/текст',size=12,text_align='center',height=50),width=224,data='HTML 1',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nHTML 2. Списки',size=12,text_align='center',height=50),width=224,data='HTML 2',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nHTML 3. Картинки',size=12,text_align='center',height=50),width=224,data='HTML 3',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nHTML 4. Много страниц',size=12,text_align='center',height=50),width=224,data='HTML 4',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nHTML 5. Таблицы',size=12,text_align='center',height=50),width=224,data='HTML 5',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nHTML 6. Выпускной - VK',size=12,text_align='center',height=50),width=224,data='HTML 6',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                        ]),
                                        ft.Column(controls=[
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nCSS 1. Введение, div, span',size=12,text_align='center',height=50),width=224,data='CSS 1',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nCSS 2. Обращение к тегам',size=12,text_align='center',height=50),width=224,data='CSS 2',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nCSS 3. Позиционирование',size=12,text_align='center',height=50),width=224,data='CSS 3',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nCSS 4. Первый сайт Буды',size=12,text_align='center',height=50),width=224,data='CSS 4',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nCSS 5. Counter  Strice',size=12,text_align='center',height=50),width=224,data='CSS 5',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nCSS 6. Выпускной 1',size=12,text_align='center',height=50),width=224,data='CSS 6',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nCSS 7. Выпускной 2',size=12,text_align='center',height=50),width=224,data='CSS 7',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                        ]),
                                        ft.Column(controls=[
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nJS 1. Управялем html',size=12,text_align='center',height=50),width=224,data='JS 1',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nJS 2. JS - запросы',size=12,text_align='center',height=50),width=224,data='JS 2',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nJS 3. Список дел',size=12,text_align='center',height=50),width=224,data='JS 3',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nJS 4. Аякс',size=12,text_align='center',height=50),width=224,data='JS 4',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nJS 5. Выпускной',size=12,text_align='center',height=50),width=224,data='JS 5',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
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