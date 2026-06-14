from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.animation import Animation

class MyLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn = Button(
            text="Click here",
            size_hint=(None, None),
            size=(200, 80),
            pos=(100, 100),
            background_color=(1, 0.412, 0.706, 1)
        )
        self.add_widget(self.btn)
        self.btn.bind(on_press=self.start_animation)
    def start_animation(self, instance):
        anim = (
            Animation(
                x=500,          # Gerak ke kanan
                duration=3
            )
            + Animation(
                y=350,          # Gerak ke atas
                duration=3
            )
            + Animation(
                size=(300, 120),   # Membesarkan tombol (zoom in)
                duration=3
            )
            + Animation(
                size=(150, 60),    # Mengecilkan tombol (zoom out)
                duration=3
            )
            + Animation(
                opacity=0.3,       # Membuat tombol transparan
                duration=3
            )
            + Animation(
                opacity=1,         # Mengembalikan transparansi normal
                duration=3
            )
            + Animation(
                background_color=(1, 0, 0, 1),   # Mengubah warna jadi merah
                duration=3
            )
            + Animation(
                background_color=(0, 1, 0, 1),   # Mengubah warna jadi hijau
                duration=3
            )
            + Animation(
                pos=(100, 100),    # Balik ke posisi awal
                size=(200, 80),    # Balik ke ukuran awal
                duration=3
            )
        )
        anim.start(self.btn)
class AnimationApp(App):
    def build(self):
        return MyLayout()
if __name__ == "__main__":
    AnimationApp().run()