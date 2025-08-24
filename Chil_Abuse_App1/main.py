from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class ChildAbuseApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Child Abuse Management System", font_size=20))
        layout.add_widget(Button(text="Report Case"))
        layout.add_widget(Button(text="View Records"))
        layout.add_widget(Button(text="Exit", on_press=lambda x: exit()))
        return layout

if __name__ == "__main__":
    ChildAbuseApp().run()
