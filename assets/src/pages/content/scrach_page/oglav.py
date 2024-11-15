
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
                                ft.Container(ft.Text('Начальный уровень - программирование Скрейч. Создаем 2д игры без кода. Для ребят 7-11 лет',size=12,color=c_white,text_align='center'),margin=ft.margin.only(left=160)),
                                ft.Container(#11
                                    ft.Row(controls=[
                                        ft.Column(controls=[
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 1. Движение и анимация',size=12,text_align='center',height=50),width=224,data='Урок 1',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 2. Танцульки',size=12,text_align='center',height=50),width=224,data='Урок 2',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 3. Кот улетает',size=12,text_align='center',height=50),width=224,data='Урок 3',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 4. Управление с клавы',size=12,text_align='center',height=50),width=224,data='Урок 4',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 5. Уборка в комнате',size=12,text_align='center',height=50),width=224,data='Урок 5',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 6. Кошак плывун',size=12,text_align='center',height=50),width=224,data='Урок 6',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 7. Догони меня кружок',size=12,text_align='center',height=50),width=224,data='Урок 7',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 8. Убегаем от мужика',size=12,text_align='center',height=50),width=224,data='Урок 8',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 9. Кот метатель такос',size=12,text_align='center',height=50),width=224,data='Урок 9',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 10. Лабиринт',size=12,text_align='center',height=50),width=224,data='Урок 10',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                        ]),
                                        ft.Column(controls=[
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 11. Бейся в стену',size=12,text_align='center',height=50),width=224,data='Урок 11',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 12. Включить свет',size=12,text_align='center',height=50),width=224,data='Урок 12',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 13. Идём по маршруту',size=12,text_align='center',height=50),width=224,data='Урок 13',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 14. Обезьяна космонавт',size=12,text_align='center',height=50),width=224,data='Урок 14',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 15. Ограбление',size=12,text_align='center',height=50),width=224,data='Урок 15',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 16. Пенальти',size=12,text_align='center',height=50),width=224,data='Урок 16',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 17. Том и джери',size=12,text_align='center',height=50),width=224,data='Урок 17',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 18. Джедай',size=12,text_align='center',height=50),width=224,data='Урок 18',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 19. Сбор яблок',size=12,text_align='center',height=50),width=224,data='Урок 19',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 20. Танки',size=12,text_align='center',height=50),width=224,data='Урок 20',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                        ]),
                                        ft.Column(controls=[
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 21. Поймай рыбку',size=12,text_align='center',height=50),width=224,data='Урок 21',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 22. Снаряды кончились',size=12,text_align='center',height=50),width=224,data='Урок 22',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 23. Гонки',size=12,text_align='center',height=50),width=224,data='Урок 23',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 24. Догони, дракон',size=12,text_align='center',height=50),width=224,data='Урок 24',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 25. Кот и зомби',size=12,text_align='center',height=50),width=224,data='Урок 25',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 26. Арканоид',size=12,text_align='center',height=50),width=224,data='Урок 26',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 27. Кошки-мышки',size=12,text_align='center',height=50),width=224,data='Урок 27',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 28. ЦУЕФА',size=12,text_align='center',height=50),width=224,data='Урок 28',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 29. Кресты и ноли',size=12,text_align='center',height=50),width=224,data='Урок 29',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
                                            ft.Container(ft.ElevatedButton(content = ft.Text('\nУрок 30. Змейка',size=12,text_align='center',height=50),width=224,data='Урок 30',on_click=self.change_page,bgcolor=c_yelow,color=c_blue,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),alignment=ft.alignment.center,margin=2),
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