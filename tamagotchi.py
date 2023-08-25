from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 10
        self.tiredness = 10
        self.happiness = 10

    def get_status(self):
        if self.happiness > 7:
            return "^_^"
        elif self.hunger > 7:
            return "o_o"
        else:
            return "-_-"

class TamagotchiApp(App):
    def build(self):
        self.tamagotchi = Tamagotchi("Tommy")
        self.box = BoxLayout(orientation='vertical')
        
        self.status_label = Label(text=self.tamagotchi.get_status(), font_size=50)
        self.box.add_widget(self.status_label)
        
        self.button_box = BoxLayout()
        
        eat_button = Button(text="Comer")
        eat_button.bind(on_press=self.feed)
        self.button_box.add_widget(eat_button)
        
        sleep_button = Button(text="Dormir")
        sleep_button.bind(on_press=self.rest)
        self.button_box.add_widget(sleep_button)
        
        play_button = Button(text="Jugar")
        play_button.bind(on_press=self.play)
        self.button_box.add_widget(play_button)
        
        self.box.add_widget(self.button_box)
        
        return self.box

    def feed(self, instance):
        self.tamagotchi.hunger = min(10, self.tamagotchi.hunger + 1)
        self.update_status()

    def rest(self, instance):
        self.tamagotchi.tiredness = min(10, self.tamagotchi.tiredness + 1)
        self.update_status()

    def play(self, instance):
        self.tamagotchi.happiness = min(10, self.tamagotchi.happiness + 1)
        self.update_status()

    def update_status(self):
        self.status_label.text = self.tamagotchi.get_status()

if __name__ == "__main__":
    TamagotchiApp().run()
