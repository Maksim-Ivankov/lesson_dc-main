
import flet as ft
from assets.variable import *
from assets.imports import *

from assets.src.pages.content.roblox_page.data_roblox import less_print

class Print_lesson(ft.UserControl):
    def __init__(self,less):
        super().__init__()
        self.less = less

    def build(self):
        self.oglav = ft.Container(
                        ft.Container(
                            ft.Container(
                                ft.Container(less_print[self.less]),
                                alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                        ),expand=2
                    )
        
        return self.oglav
        