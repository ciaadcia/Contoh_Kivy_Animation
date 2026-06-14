from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.core.window import Window
import random

Window.size = (420, 800)


class Drop:

    def __init__(self, parent):

        self.x = random.randint(0, 420)

        self.y = random.randint(-900, 0)

        self.speed = random.randint(
            10,
            18
        )

        self.slant = random.uniform(
            -.4,
            .4
        )

        with parent.canvas.after:

            Color(
                .88,
                .95,
                1,
                .8
            )

            self.obj = Ellipse(

                pos=(
                    self.x,
                    self.y
                ),

                size=(
                    4,
                    10
                )
            )

    def move(self):

        self.y -= self.speed

        self.x += self.slant

        if self.y < -20:

            self.y = random.randint(
                820,
                1000
            )

            self.x = random.randint(
                0,
                420
            )

        self.obj.pos = (
            self.x,
            self.y
        )


class Star:

    def __init__(
        self,
        parent
    ):

        x = random.randint(
            0,
            420
        )

        y = random.randint(
            350,
            760
        )

        size = random.randint(
            2,
            5
        )

        with parent.canvas.after:

            Color(
                1,
                1,
                1
            )

            self.obj = Ellipse(

                pos=(
                    x,
                    y
                ),

                size=(
                    size,
                    size
                )
            )


class WeatherUI(
    FloatLayout
):

    def __init__(
        self,
        **kwargs
    ):

        super().__init__(
            **kwargs
        )

        self.mode = ""

        self.parts = []

        self.draw_bg(
            .45,
            .8,
            1
        )

        self.build()

        Clock.schedule_interval(
            self.animate,
            1 / 60
        )

    def draw_bg(
        self,
        r,
        g,
        b
    ):

        self.canvas.before.clear()

        with self.canvas.before:

            Color(
                r,
                g,
                b
            )

            Rectangle(
                size=Window.size
            )

    def clear_weather(
        self
    ):

        self.canvas.after.clear()

        self.parts = []

    def build(
        self
    ):

        self.title = Label(

            text="SkyMotion",

            font_size=30,

            bold=True,

            pos_hint={

                "center_x": .5,

                "top": .95
            }
        )

        self.add_widget(
            self.title
        )

        self.temp = Label(

            text="31°C",

            font_size=72,

            pos_hint={

                "center_x": .5,

                "center_y": .68
            }
        )

        self.add_widget(
            self.temp
        )

        self.status = Label(

            text="SUNNY",

            font_size=24,

            pos_hint={

                "center_x": .5,

                "center_y": .58
            }
        )

        self.add_widget(
            self.status
        )

        buttons = [

            (
                "SUN",
                .2
            ),

            (
                "RAIN",
                .5
            ),

            (
                "NIGHT",
                .8
            )

        ]

        for text, x in buttons:

            btn = Button(

                text=text,

                size_hint=(

                    .22,

                    .08

                ),

                pos_hint={

                    "center_x": x,

                    "y": .08
                }
            )

            btn.bind(
                on_press=self.change
            )

            self.add_widget(
                btn
            )

        self.sun()

    def sun(
        self
    ):

        self.clear_weather()

        self.mode = "sun"

        self.draw_bg(
            .45,
            .8,
            1
        )

        self.temp.text = "31°C"

        self.status.text = "SUNNY"

        with self.canvas.after:

            Color(
                1,
                .9,
                .2
            )

            self.sun_obj = Ellipse(

                pos=(

                    160,

                    480

                ),

                size=(

                    90,

                    90
                )
            )

    def rain(
        self
    ):

        self.clear_weather()

        self.mode = "rain"

        self.draw_bg(
            .30,
            .35,
            .55
        )

        self.temp.text = "24°C"

        self.status.text = "RAINY"

        for _ in range(
            100
        ):

            self.parts.append(
                Drop(
                    self
                )
            )

    def night(
        self
    ):

        self.clear_weather()

        self.mode = "night"

        self.draw_bg(
            .07,
            .09,
            .16
        )

        self.temp.text = "19°C"

        self.status.text = "NIGHT"

        with self.canvas.after:

            Color(
                1,
                1,
                .8
            )

            Ellipse(

                pos=(

                    160,

                    500

                ),

                size=(

                    80,

                    80
                )
            )

        for _ in range(
            50
        ):

            self.parts.append(
                Star(
                    self
                )
            )

    def change(
        self,
        btn
    ):

        if btn.text == "SUN":

            self.sun()

        elif btn.text == "RAIN":

            self.rain()

        else:

            self.night()

    def animate(
        self,
        dt
    ):

        if self.mode == "rain":

            for i in self.parts:

                i.move()

        elif self.mode == "sun":

            if hasattr(
                self,
                "sun_obj"
            ):

                x, y = (
                    self.sun_obj.pos
                )

                y += random.uniform(
                    -.1,
                    .1
                )

                self.sun_obj.pos = (
                    x,
                    y
                )


class SkyMotion(
    App
):

    def build(
        self
    ):

        return (
            WeatherUI()
        )


SkyMotion().run()