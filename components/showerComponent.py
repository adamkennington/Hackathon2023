import tkinter
import tkinter.messagebox
import customtkinter

class ShowerComponent(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bestTime = 0
        self.yourTime = 0
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=3)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.grid_columnconfigure((0, 1, 2), weight=1)
        
        self.bestTimeDisplay = customtkinter.CTkLabel(self, text=f"Best Shower Delay = {self.bestTime} Days")

        self.yourTimeDisplay = customtkinter.CTkLabel(self, text=f"It has been {self.yourTime} days since you have taken a shower.")

        self.prompt =  customtkinter.CTkLabel(self, text=f"Type how long it has been since you have showered below!")
        
        self.bestTimeDisplay.grid(row=1, column=1, sticky="nsew")

        self.yourTimeDisplay.grid(row=2, column=1, sticky="nsew")

        self.prompt.grid(row=3, column=1, sticky="nsew")

    def entry_event(self, text):
        self.yourTime = int(text)
        if self.yourTime > self.bestTime:
            self.yourTimeDisplay.configure(text=f"WOW! It has been more than {self.bestTime} days since you have taken a shower?!?")
            self.bestTime = self.yourTime
            self.bestTimeDisplay.configure(text=f"Best Shower Delay = {self.bestTime} Days.")
        else:
            self.yourTimeDisplay.configure(text=f"It has been {self.yourTime} days since you have taken a shower.")




