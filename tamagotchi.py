import tkinter as tk
from tkinter import messagebox

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 10
        self.tiredness = 10
        self.happiness = 10
        self.pet = """
        ^_^
       /   \\
      (     )
       \\___/
        """

    def eat(self):
        if self.hunger > 0:
            self.hunger -= 1
        else:
            messagebox.showinfo("Información", f"{self.name} no tiene hambre.")

    def sleep(self):
        if self.tiredness > 0:
            self.tiredness -= 1
        else:
            messagebox.showinfo("Información", f"{self.name} no tiene sueño.")

    def play(self):
        if self.happiness < 10:
            self.happiness += 1
        else:
            messagebox.showinfo("Información", f"{self.name} ya está muy feliz.")

    def show_status(self):
        return f"{self.pet}\n{self.name} - Hambre: {self.hunger}, Sueño: {self.tiredness}, Felicidad: {self.happiness}"

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.tamagotchi = Tamagotchi("Tommy")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.status = tk.Label(self, text=self.tamagotchi.show_status(), font=("Courier", 10))
        self.status.pack(side="top")

        self.eat = tk.Button(self)
        self.eat["text"] = "Comer"
        self.eat["command"] = self.feed
        self.eat.pack(side="left")

        self.sleep = tk.Button(self)
        self.sleep["text"] = "Dormir"
        self.sleep["command"] = self.rest
        self.sleep.pack(side="left")

        self.play = tk.Button(self)
        self.play["text"] = "Jugar"
        self.play["command"] = self.game
        self.play.pack(side="left")

    def feed(self):
        self.tamagotchi.eat()
        self.status["text"] = self.tamagotchi.show_status()

    def rest(self):
        self.tamagotchi.sleep()
        self.status["text"] = self.tamagotchi.show_status()

    def game(self):
        self.tamagotchi.play()
        self.status["text"] = self.tamagotchi.show_status()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
