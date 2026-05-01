from manim import *
import json
from pathlib import Path

class DynamicScene(Scene):
    def construct(self):
        config_path = Path("frontend/animations/config.json")
        config = json.loads(config_path.read_text(encoding="utf-8"))

        commodity = config["commodity"]
        model = config["model"]
        period = config["period"]

        title = Text(f"{commodity}: {model}", font_size=42)
        subtitle = Text(f"Sample: {period}", font_size=30).next_to(title, DOWN)
        circle = Circle(color=BLUE).shift(DOWN * 1.5)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.play(Create(circle))
        self.play(circle.animate.scale(1.3).set_color(GREEN))
        self.wait(1)