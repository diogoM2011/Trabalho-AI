from manim import *
from manim_slides import Slide

class Work_Scene(Slide):
    def construct(self):
        titulo = Text("Marshall Mathers", color=BLACK)
        self.play(Write(titulo)) 
