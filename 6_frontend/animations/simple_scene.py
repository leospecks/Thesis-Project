# run with: manim -pqh 6_frontend/animations/simple_scene.py HelloScene --media_dir 6_frontend/animations/media
# p(preview), q_ (quality, alternatives: ql, qm, qh, qk)

from manim import *

class HelloScene(Scene):
    def construct(self):
        title = Text("Thesis: Replication and Baseline Results")
        circle = Circle(color=BLUE)
        circle.shift(DOWN)
    

        self.play(Write(title))
        self.play(Create(circle))
        self.play(circle.animate.scale(1.5).set_color(GREEN))
        self.play(title.animate.scale(0.5).set_color(BLUE))
        self.wait(1)