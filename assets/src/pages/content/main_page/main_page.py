
import flet as ft
from assets.variable import *
from assets.imports import *


class Main_page(ft.UserControl):
    # def __init__(self,change_menu):
    #     super().__init__()
    #     self.change_menu = change_menu

    def build(self):
        
        self.scrach_page = ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Container(
                                    ft.Text('Учебник Майнкрафт',color=c_blue),
                                    alignment=ft.alignment.center
                                    
                        ),
                        bgcolor=c_yelow,
                        height=28,
                        margin=ft.margin.only(top=-10,left=-10,right=-10),
                        border = ft.border.all(1,c_white),
                        
                    ),
                    ft.Container(
                        ft.Column(controls=[
                            ft.Container(
                                ft.Container(
                                    ft.Container(
                                        ft.Column(controls=[
                                            ft.Container(ft.Text('В РАЗРАБОТКЕ',text_align='center'),width=700),
                                            ft.Container(ft.Text('У нас лапки, но мы работаем. Скоро здесь что-то появится.',text_align='center'),width=700),
                                        ]),
                                    alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=260)      
                                ),expand=2
                            )


                        ]),
                        expand=2,
                    )
                ]
            ),expand=2
        )
        
        return self.scrach_page