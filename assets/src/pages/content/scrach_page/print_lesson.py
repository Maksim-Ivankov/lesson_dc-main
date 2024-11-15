
import flet as ft
from assets.variable import *
from assets.imports import *


class Print_lesson(ft.UserControl):
    def __init__(self,less,gif_path,text_less,help_img_pas):
        super().__init__()
        self.less = less
        self.gif_path = gif_path
        self.text_less = text_less
        self.help_img_pas = help_img_pas

    def build(self):

        if self.help_img_pas != '':
            self.img_help_component = ft.Container(#11
                                            ft.Column(controls=[
                                                ft.Container(ft.Text('Алгоритм работы программы',size=12,color=c_white),margin=ft.margin.only(left=210,top=20)),
                                                ft.Image(src=self.help_img_pas)
                                            ]),
                                            # width=800,
                                            margin=ft.margin.only(left=190,top=-74,bottom=40),
                                        )
        else: self.img_help_component = ft.Container()
        if self.less == 'Урок 7' or self.less == 'Урок 8' or self.less == 'Урок 9':
            self.img_help_component = ft.Container(#11
                                            ft.Column(controls=[
                                                ft.Container(ft.Text('Алгоритм работы программы',size=12,color=c_white),margin=ft.margin.only(left=210,top=20)),
                                                ft.Image(src=self.help_img_pas,width=600)
                                            ]),
                                            # width=800,
                                            margin=ft.margin.only(left=190,top=-74,bottom=40),
                                        )


        self.oglav = ft.Container(
                        ft.Container(
                            ft.Container(
                                # ft.Container(
                                    
                                #     ft.Column(controls=[
                                #         ft.Image(src=self.gif_path,),
                                #         ft.Container(ft.Text(self.text_less,size=12,color=c_white),margin=ft.margin.only(left=100,right=100)),
                                #     ]),

                                # ),
                                
                                        # width=800,
                                        # margin=ft.margin.only(left=90,top=-74),
                                        # bgcolor='red',
                                ft.Column(controls=[
                                    ft.Container(ft.Text(self.text_less,size=12,color=c_white),margin=ft.margin.only(left=100,right=100)),
                                    ft.Container(ft.Text('Вот как должа работать твоя программа',size=12,color=c_white),margin=ft.margin.only(left=360,top=20)),
                                    ft.Container(#
                                        ft.Image(
                                            src=self.gif_path,
                                        ),
                                        width=800,
                                        margin=ft.margin.only(left=90,top=-74),
                                        # bgcolor='red',

                                    ),
                                    self.img_help_component,

                                ]),
                            alignment=ft.alignment.center),margin=ft.margin.only(top=2,left=-10,right=-10),padding=ft.padding.only(top=10)      
                        ),expand=2
                    )
        
        return self.oglav
        
        # self.print_lesson = ft.Container(
        #     ft.Column(
        #         controls=[
                    
        #             #    ft.Text(self.less),
        #             #    ft.Text(self.gif_path),
        #                ft.Container(ft.Text(self.text_less),width=800),
        #             #    ft.Text(self.help_img_pas),
        #                ft.Image(
        #                     src=self.gif_path,
        #                     # width=200,
        #                     # height=200,
        #                     # fit=ft.ImageFit.NONE,
        #                     # repeat=ft.ImageRepeat.NO_REPEAT,
        #                     # border_radius=ft.border_radius.all(10),
        #                 )
                    
        #         ]
        #     ),expand=2
        # )
        
        # return self.print_lesson