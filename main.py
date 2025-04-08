from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from FileSharer import FileSharer
import time

Builder.load_file('Frontend.kv')

class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%M%D-%H%M%"S')
        filepath = f"files/{current_time}.png"
        self.ids.camera.export_to_png(filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = filepath

class ImageScreen(Screen):
    def create_link(self)

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

MainApp().run()