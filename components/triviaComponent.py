import tkinter
import tkinter.messagebox
import customtkinter
import trivia

class TriviaComponent(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid(row=0, column=1, padx=(5, 0), pady=(5, 0), rowspan=4, sticky="nsew")
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.header = customtkinter.CTkFrame(self, corner_radius=0)
        self.header.grid(row=0, column=0, sticky="nsew")

        self.game = customtkinter.CTkFrame(self, corner_radius=0)
        self.game.grid(row=1, column=0, sticky="nsew", rowspan=2)
        self.game.grid_rowconfigure(2, weight=4)
        
        self.playing: bool = False
        self.categories = []
        self.selectedCat = 0
        self.selectedDiff = 0

        self.drawHeader()

        

    def pick_cat_event(self, el):
        print(f"{trivia.CATEGORIES.index(el)} click")
        self.selectedCat = el

    def pick_diff_event(self, el):
        print(f"{trivia.DIFFICULTY.index(el)} click")
        self.selectedDiff = el

    def drawHeader(self):
        textbox = customtkinter.CTkLabel(self.header, text="Category:")
        textbox.grid(row=0, pady=15, column=0)
        cats = customtkinter.CTkOptionMenu(master=self.header, width=300,
                                       values=trivia.CATEGORIES,
                                       command=self.pick_cat_event)
        cats.grid(row=1, column=0, padx=20, pady=10)


        textbox = customtkinter.CTkLabel(self.header, text="Difficulty:")
        textbox.grid(row=0, pady=15, column=1)
        diffs = customtkinter.CTkOptionMenu(master=self.header,
                                       values=trivia.DIFFICULTY,
                                       command=self.pick_diff_event)
        diffs.grid(row=1, column=1, padx=20, pady=10)

