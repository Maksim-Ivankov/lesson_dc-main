


import flet as ft
from assets.variable import *
from assets.imports import *

from assets.src.pages.menu.UI.modernNavBar import ModernNavBar

class Menu(ft.UserControl):

    def __init__(self,page,callback,punkt_menu_one):
        super().__init__()
        self.callback = callback
        self.page = page
        self.punkt_menu_one = punkt_menu_one
        self.size_bar = 'max'
        self.time_event_hover = 0
        self.time_event_click = 0

    def build(self):

        # логика сворачивания окна
        def AnimateSidebar(e):
            self.time_event_click = time.time()
            if self.controls[0].width !=62:
                self.controls[0].content.controls[0].content.controls[0].content.src = 'src/img/logo_2_min.png'
                self.controls[0].content.controls[0].content.controls[0].update()
                for items in self.controls[0].content.controls[0].content.controls[2].controls:
                    if isinstance(items,ft.Container):
                        items.content.controls[1].opacity = 0
                        items.content.update()
                self.controls[0].content.controls[0].content.controls[3].content.controls[0].content.controls[0].controls[1].opacity = 0
                self.controls[0].width = 62
                self.controls[0].update()
            
        
        def open_menu(e):
            self.time_event_hover = time.time()
            if (self.time_event_hover - self.time_event_click)>0.5:
                self.controls[0].width = 200
                self.controls[0].update()
                self.controls[0].content.controls[0].content.controls[3].content.controls[0].content.controls[0].controls[1].opacity = 1
                self.controls[0].content.controls[0].content.controls[0].content.src = 'src/img/logo_2.png'
                self.controls[0].content.controls[0].content.controls[0].update()
                for items in self.controls[0].content.controls[0].content.controls[2].controls:
                    if isinstance(items,ft.Container):
                        items.content.controls[1].opacity = 1
                        items.content.update()
        
        # Контейнер меню
        self.menu = ft.Container(
                content=ModernNavBar(AnimateSidebar,self.callback,self.punkt_menu_one),
                width=200,
                bgcolor=c_blue,
                border_radius=0,
                border = ft.border.all(1, c_white),
                alignment=ft.alignment.center,
                animate=ft.animation.Animation(500,'decelerate'),
                margin = ft.margin.only(left=-10,top=-10),
                on_hover=open_menu
                

            
        )
        
        return self.menu