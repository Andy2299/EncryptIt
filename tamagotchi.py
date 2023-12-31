import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'
import tkinter as tk

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.tiredness = 5
        self.happiness = 5

    def get_status(self):
        if self.happiness > 7:
            return "^_^"
        elif self.hunger > 7:
            return "o_o"
        else:
            return "-_--"

class TamagotchiApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tamagotchi")
        self.tamagotchi = Tamagotchi("Tommy")

        self.status_label = tk.Label(self.master, text=self.tamagotchi.get_status(), font=("Arial", 50))
        self.status_label.pack()

        self.eat_button = tk.Button(self.master, text="Comer", command=self.feed)
        self.eat_button.pack()

        self.sleep_button = tk.Button(self.master, text="Dormir", command=self.rest)
        self.sleep_button.pack()

        self.play_button = tk.Button(self.master, text="Jugar", command=self.play)
        self.play_button.pack()

    def feed(self):
        self.tamagotchi.hunger = min(10, self.tamagotchi.hunger + 1)
        self.update_status()

    def rest(self):
        self.tamagotchi.tiredness = min(10, self.tamagotchi.tiredness + 1)
        self.update_status()

    def play(self):
        self.tamagotchi.happiness = min(10, self.tamagotchi.happiness + 1)
        self.update_status()

    def update_status(self):
        new_status = self.tamagotchi.get_status()
        self.status_label.config(text=new_status)
        self.master.update_idletasks()

def main():
    root = tk.Tk()
    app = TamagotchiApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()