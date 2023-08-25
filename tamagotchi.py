import tkinter as tk
from tkinter import messagebox

# Tamagotchi class definition
class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 10
        self.tiredness = 10
        self.happiness = 10

    def get_pet(self):
        if self.happiness > 7:
            return "^_^"
        elif self.hunger > 7:
            return "o_o"
        else:
            return "-_-"

    def show_status(self):
        pet = self.get_pet()
        return f"{pet}\n{self.name} - Hambre: {self.hunger}, Sueño: {self.tiredness}, Felicidad: {self.happiness}"

# GUI Application class definition
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.tamagotchi = Tamagotchi("Tommy")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.status = tk.Label(self, text=self.tamagotchi.show_status(), font=("Courier", 14))
        self.status.pack(side="top")

        self.eat = tk.Button(self, text="Comer", command=self.feed)
        self.eat.pack(side="left")

        self.sleep = tk.Button(self, text="Dormir", command=self.rest)
        self.sleep.pack(side="left")

        self.play = tk.Button(self, text="Jugar", command=self.game)
        self.play.pack(side="left")

    def feed(self):
        self.tamagotchi.hunger = min(10, self.tamagotchi.hunger + 1)
        self.update_status()

    def rest(self):
        self.tamagotchi.tiredness = min(10, self.tamagotchi.tiredness + 1)
        self.update_status()

    def game(self):
        self.tamagotchi.happiness = min(10, self.tamagotchi.happiness + 1)
        self.update_status()

    def update_status(self):
        self.status.config(text=self.tamagotchi.show_status())

# Main function to run the application
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()