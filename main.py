from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.uix.settings import Settings, SettingsWithTabbedPanel
from kivy.core.window import Window
from kivy.uix.image import AsyncImage
from kivy.properties import ObjectProperty
import math

class CalculateApp(App):
    formula = ObjectProperty()
    fahrenheit = ObjectProperty()
    celsius = ObjectProperty()
    font_size = ObjectProperty()
    bg_color = StringProperty()
    text_color = ObjectProperty()
    img1 = StringProperty()
    img2 = StringProperty()

    def build_config(self, config):
            config.setdefaults("Settings", {"font_num": 20,
                                            "font_color": "black",
                                            "bg_color": "white",
                                            "cover_photo": "C:/Users/Acer/PycharmProjects/APPDEV_FCHW2/default.jpg"})

    def build_settings(self, settings):
            settings.add_json_panel("Settings", self.config, data="""
            [ 
                 { "type": "numeric",
                    "title": "Change Font Size" 
                    "section":"Settings",
                    "desc": "Change font size of your application",
                    "key": "font_num"
           },        
                { "type": "options",
                    "title": "Change Font Color",
                    "section":"Settings",
                    "desc": "Change the font color of your application"
                    "options":["black", "red", "green", "blue", "yellow"],
                    "key":"font_color"
           },         
                    { "type": "options",
                    "title": "Change Background Color",
                    "section":"Settings",
                    "desc": "Change the background color of your application"
                    "options":["white","black", "red", "green", "blue", "yellow"],
                    "key":"bg_color"
           }, 
            { "type": "path",
                    "title": "Change Cover Photo",
                    "section":"Settings",
                    "desc": "Change the cover photo of your application",
                    "key":"cover_photo"    
                    }             
            ]""")

    def build(self):
        # settings panel
        self.settings_cls = SettingsWithTabbedPanel
        self.font_size = self.config.getint('Settings', 'font_num')
        self.text_color = self.config.get('Settings', 'font_color')
        self.bg_color = self.config.get('Settings', 'bg_color')
        self.img1 = self.config.get('Settings', 'cover_photo')

        # entire app layout
        MyLayout = BoxLayout(orientation="vertical")

        # changes window color
        Window.clearcolor = (self.bg_color)
        # layout for the image
        ImageLayout = RelativeLayout()
        MyLayout.add_widget(ImageLayout)

        cover_photo = AsyncImage(source=self.img1, size_hint=(0.75, 1),
                                 pos_hint={"center_x": 0.5, "center_y": 0.40})
        ImageLayout.add_widget(cover_photo)

        # layout for adding specific widgets
        WidgetLayout = RelativeLayout()
        MyLayout.add_widget(WidgetLayout)

        f_label = Label(text='Fahrenheit', pos_hint={"center_x": 0.15, "center_y": 0.45}, font_size=self.font_size,
                        color=self.text_color)
        WidgetLayout.add_widget(f_label)

        self.f_text = TextInput(size_hint_x=0.15, size_hint_y=0.20, pos_hint={"center_x": 0.30, "center_y": 0.45})
        WidgetLayout.add_widget(self.f_text)

        label = Label(text='=', pos_hint={"center_x": 0.47, "center_y": 0.45}, font_size=self.font_size, color=self.text_color )
        WidgetLayout.add_widget(label)

        c_label = Label(text='Celsius', pos_hint={"center_x": 0.60, "center_y": 0.45}, font_size=self.font_size, color=self.text_color)
        WidgetLayout.add_widget(c_label)

        self.c_text = TextInput(size_hint_x=0.15, size_hint_y=0.20, pos_hint={"center_x": 0.75, "center_y": 0.45})
        WidgetLayout.add_widget(self.c_text)

        convert_button = Button(text="Convert", size_hint=(None, None), size_hint_x=0.15, size_hint_y=0.20,
                                pos_hint={"center_x": 0.30, "center_y": 0.15}, font_size = self.font_size, on_press=self.convert_to_fahrenheit)
        WidgetLayout.add_widget(convert_button)

        settings_button = Button(text="Settings", size_hint=(None, None), size_hint_x=0.15, size_hint_y=0.20,
                                 pos_hint={"center_x": 0.75, "center_y": 0.15}, on_press=self.open_settings, font_size=self.font_size)
        WidgetLayout.add_widget(settings_button)

        return MyLayout

    def on_config_change(self, config, section, key, value):
            if config is self.config:
                # changes font size
                if key == "font_num":
                    self.font_size = value
                # changes font color
                if key == "font_color":
                     if value == "black":
                         self.text_color == value
                     elif value == "red":
                         self.text_color == value
                     elif value == "green":
                         self.text_color == value
                     elif value == "blue":
                         self.text_color == value
                     elif value == "yellow":
                        self.text_color == value
                # changes background color
                if key == "bg_color":
                     if value == "white":
                         self.text_color == value
                     elif value == "black":
                         self.text_color == value
                     elif value == "red":
                         self.text_color == value
                     elif value == "green":
                         self.text_color == value
                     elif value == "blue":
                         self.text_color == value
                     elif value == "yellow":
                        self.text_color == value
                # changes cover photo
                if key == "cover_photo":
                        self.img1 == value

    def convert_to_fahrenheit(self, arg):
        self.fahrenheit = float(self.f_text.text)
        self.celsius = round(self.fahrenheit - 32) * 5 / 9
        math.trunc(self.celsius)
        self.celsius = str(self.celsius)
        self.c_text.text = self.celsius

    def convert_to_celsius(self, arg):
        self.celsius = float(self.c_text.text)
        self.fahrenheit = round(self.celsius * 9/5) + 32
        math.trunc(self.fahrenheit)
        self.fahrenheit = str(self.fahrenheit)
        self.f_text.text = self.fahrenheit

if __name__ == "__main__":
    CalculateApp().run()