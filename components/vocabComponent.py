import tkinter
import tkinter.messagebox
import customtkinter
import threading
from vocab import Vocab

class VocabComponent(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid(row=0, column=1, padx=(5, 0), pady=(5, 0), rowspan=4,sticky="nsew")

        self.buttonWords = customtkinter.CTkButton(self, command=self.load0, text="Option 1: Choose the correct definition")
        self.buttonWords.grid(row=0, column=0, padx=20, pady=10)
        self.buttonWords.place(relx = 0.25, rely = 0.5,anchor=tkinter.CENTER)

        self.buttonDefs = customtkinter.CTkButton(self, command=self.load1, text="Option 2: Choose the correct word")
        self.buttonDefs.grid(row=0, column=1, padx=20, pady=10)
        self.buttonDefs.place(relx = 0.75, rely = 0.5,anchor=tkinter.CENTER)

        self.answerWord = ""
        self.answerDef = ""
        self.allAnswers = []
        self.voc : object

        t1 = threading.Thread(target = self.makeObj)
        t1.start()
        
        
    def makeObj(self):
        self.voc = Vocab()
        
    def button_click(self, butNum):
        if butNum == 0:
            if self.button0.cget("text") == self.answerDef or self.button0.cget("text") == self.answerWord:
                print("Correct")
                self.configure(fg_color = "green")
            else:
                print("Incorrect")
                self.configure(fg_color = "red")
    
        elif butNum == 1:
            if self.button1.cget("text") == self.answerDef or self.button1.cget("text") == self.answerWord:
                print("Correct")
                self.configure(fg_color = "green")
            else:
                print("Incorrect")
                self.configure(fg_color = "red")
               
        elif butNum == 2:
            if self.button2.cget("text") == self.answerDef or self.button2.cget("text") == self.answerWord:
                print("Correct")
                self.configure(fg_color = "green")
            else:
                print("Incorrect")
                self.configure(fg_color = "red")
                
        elif butNum == 3:
            if self.button3.cget("text") == self.answerDef or self.button3.cget("text") == self.answerWord:
                print("Correct")
                self.configure(fg_color = "green")
            else:
                print("Incorrect")
                self.configure(fg_color = "red")
                

    def button_next(self):
        if self.master._get_appearance_mode() == "dark":
            self.configure(fg_color = "#2a2a2b")
        elif self.master._get_appearance_mode() == "light":
            self.configure(fg_color = "#dadbda")

        self.prompt.destroy()
        self.button0.destroy()
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.load()

    def load(self):
        while threading.active_count() > 1:
            pass

        self.prompt = customtkinter.CTkLabel(self, text = "Placeholder Text", font=("Times", 24, "bold"), wraplength=1000)
        self.prompt.grid(row = 0, column = 0)
        self.prompt.place(relx = 0.5, rely = 0.1,anchor=tkinter.CENTER)

        self.button0 = customtkinter.CTkButton(self, command=lambda: self.button_click(0), text = "")
        self.button0.grid(row=0, column=1, padx=20, pady=10)
        self.button0.place(relx = 0.5, rely = 0.3,anchor=tkinter.CENTER)

        self.button1 = customtkinter.CTkButton(self, command=lambda: self.button_click(1), text = "")
        self.button1.grid(row=0, column=2, padx=20, pady=10)
        self.button1.place(relx = 0.5, rely = 0.45,anchor=tkinter.CENTER)

        self.button2 = customtkinter.CTkButton(self, command=lambda: self.button_click(2), text = "")
        self.button2.grid(row=1, column=0, padx=20, pady=10)
        self.button2.place(relx = 0.5, rely = 0.6,anchor=tkinter.CENTER)

        self.button3 = customtkinter.CTkButton(self, command=lambda: self.button_click(3), text = "")
        self.button3.grid(row=1, column=1, padx=20, pady=10)
        self.button3.place(relx = 0.5, rely = 0.75,anchor=tkinter.CENTER)

        self.buttonNext = customtkinter.CTkButton(self, command=self.button_next, text="Next")
        self.buttonNext.grid(row=2, column=1, padx=20, pady=10)
        self.buttonNext.place(relx=0.5, rely=0.9,anchor=tkinter.CENTER)

        if self.mode == 0:
            self.answerWord, self.answerDef, self.allAnswers = self.voc.wordToDef()
            self.prompt.configure(text = self.answerWord)
        elif self.mode == 1:
            self.answerWord, self.answerDef, self.allAnswers = self.voc.defToWord()
            self.prompt.configure(text = self.answerDef)

        self.button0.configure(text = self.allAnswers[0])
        self.button1.configure(text = self.allAnswers[1])
        self.button2.configure(text = self.allAnswers[2])
        self.button3.configure(text = self.allAnswers[3])
        


    def load0(self):
        self.mode = 0
        self.buttonWords.destroy()
        self.buttonDefs.destroy()
        self.load()

    def load1(self):
        self.mode = 1
        self.buttonWords.destroy()
        self.buttonDefs.destroy()
        self.load()