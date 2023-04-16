import tkinter
import tkinter.messagebox
import customtkinter
from random import randrange, random

class ShowerComponent(customtkinter.CTkFrame):
    def __init__(self, master, parentAfter, **kwargs):
        super().__init__(master, **kwargs)
        self.parentAfter = parentAfter
        self.bestTime = 0
        self.yourTime = 0
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        # self.grid_rowconfigure(1, weight=1)
        # self.grid_rowconfigure(2, weight=1)
        # self.grid_rowconfigure(3, weight=1)

        self.grid_columnconfigure((0, 1, 2), weight=1)
        
        self.bestTimeDisplay = customtkinter.CTkLabel(self, text=f"Best Shower Delay = {self.bestTime} Days")

        self.yourTimeDisplay = customtkinter.CTkLabel(self, text=f"It has been {self.yourTime} days since you have taken a shower.")

        self.prompt =  customtkinter.CTkLabel(self, text=f"Press the button to have your shower delay calculated!")
        
        self.calculatebtn = customtkinter.CTkButton(self, text="Press Me!", command=self.calculate)

        self.bestTimeDisplay.grid(row=0, column=1, sticky="nsew")

        self.yourTimeDisplay.grid(row=1, column=1, sticky="nsew")

        self.prompt.grid(row=2, column=1, sticky="nsew")
        self.calculatebtn.grid(row=3, column=1, sticky="nsew")

    def entry_event(self, shower_variable):
        self.yourTime = shower_variable
        if self.yourTime > self.bestTime:
            self.yourTimeDisplay.configure(text=f"WOW! It has been more than {self.bestTime} days since you have taken a shower?!?")
            self.bestTime = self.yourTime
            self.bestTimeDisplay.configure(text=f"Best Shower Delay = {self.bestTime} Days.")
        else:
            self.yourTimeDisplay.configure(text=f"It has been {self.yourTime} days since you have taken a shower.")


    def calculate(self):
        self.calculatebtn.configure(text="Sniffing...", state="disabled")
        self.parentAfter(500 + int(random()*3000), self.afterDelay)

    def afterDelay(self):
        self.calculatebtn.configure(text="Press Me!", state="normal")
        self.entry_event(randrange(0, 25))
