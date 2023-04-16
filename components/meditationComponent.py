import tkinter
import tkinter.messagebox
import customtkinter

class MeditationComponent(customtkinter.CTkFrame):
    def __init__(self, master, parentAfter, **kwargs):
        super().__init__(master, **kwargs)
        self.parentAfter = parentAfter
        
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure((0, 2), weight=3)
        self.grid_columnconfigure(1, weight=1)

        self.description = customtkinter.CTkLabel(self, text="What better way to end a long day of self improvement than a long meditation session?\nPress the button below to begin.")

        self.description.grid(row=0, column=0, columnspan=3)
        

        self.btn = customtkinter.CTkButton(self, text="Relax", command=self.begin)
        self.btn.grid(row=1, column=1)



    def begin(self):
        self.btn.configure(state="disabled")
        self.description.configure(text="Breathe in...")
