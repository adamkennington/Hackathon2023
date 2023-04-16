import tkinter
import tkinter.messagebox
import customtkinter

class Sidebar(customtkinter.CTkFrame):
    def __init__(self, master, buttonEv, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self, text="Categories", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_names = ['Typing', 'Math', 'Memorization', 'Vocab', 'Reaction', 'Trivia', 'Shower Tracker', 'Meditation']
        self.sidebar_buttons = []
        for i in range(8):
            button = customtkinter.CTkButton(self, text=self.sidebar_names[i], command=lambda i=i: buttonEv(i))
            button.grid(row=i+1, column=0, padx=20, pady=10, sticky="nsew")
            self.grid_rowconfigure(i+1, weight=1)
            self.sidebar_buttons.append(button)
