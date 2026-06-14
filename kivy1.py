from math import sin, cos, pi
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.core.window import Window

Window.size = (900, 700)
Window.clearcolor = (0.02, 0.02, 0.08, 1)


class Heart(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.labels = []
        self.t = 0

        jumlah = 90

        for i in range(jumlah):

            label = Label(
                text="I Love You",
                font_size=14,
                bold=True,
                size_hint=(None, None),
                color=(1, 0.75, 0.85, 1)
            )

            self.add_widget(label)

            sudut = i / jumlah * (2 * pi)

            self.labels.append(
                (label, sudut)
            )

        Clock.schedule_interval(
            self.update,
            1 / 60
        )

    def update(self, dt):

        self.t += 0.03

        cx = Window.width / 2
        cy = Window.height / 2

        scale = 22 + sin(self.t * 2) * 1.5

        for label, a in self.labels:

            tt = a

            x = 16 * sin(tt) ** 3

            y = (
                13 * cos(tt)
                - 5 * cos(2 * tt)
                - 2 * cos(3 * tt)
                - cos(4 * tt)
            )

            x *= scale
            y *= scale

            gerak = sin(self.t * 3 + a * 5) * 4

            px = cx + x
            py = cy + y + gerak

            label.center = (px, py)

            glow = 0.8 + 0.2 * sin(self.t * 5)

            label.color = (
                1,
                glow,
                0.9,
                1
            )


class LoveApp(App):

    def build(self):
        return Heart()


LoveApp().run()