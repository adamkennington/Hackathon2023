import tkinter
import tkinter.messagebox
import customtkinter
from random import random
import time
import pandas as pd

class ReactionComponent(customtkinter.CTkFrame):
    def __init__(self, master, parentAfter, **kwargs):
        super().__init__(master, **kwargs)
        self.parentAfter = parentAfter


        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=3)
        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)

        self.df = None
        self.df = pd.read_csv('components/high_scores.csv')
        self.bestTime = self.df['reaction'][0]
        

        self.btn = customtkinter.CTkButton(self, text="Ready?", command=self.clicked)
        self.btn.grid(row=1, column=1, sticky="nsew")

        self.bestTxt = customtkinter.CTkLabel(self, text=f"Best Time = {self.bestTime}")
        self.bestTxt.grid(row=0, column=1, sticky="nsew")

        self.stopped = True
        self.waiting = False
        self.counting = False
        
        self.startTime = 0
        self.finalTime = 0
        self.cheating = 0




    def clicked(self):
        if self.waiting:
            print("WAIT")
            self.cheating += 10000000
            self.btn.configure(text="WAIT")

        if self.stopped:
          self.stopped = False
          self.waiting = True
          self.parentAfter(500 + int(random()*3000), self.afterDelay)
          self.btn.configure(text="...", fg_color=("gray92", "gray14"))

        if self.counting:
          self.finalTime = self.cheating + (time.time_ns() - self.startTime ) / 1000000000
          self.cheating = 0
          print(self.finalTime)
          self.counting = False
          self.stopped = True
          self.btn.configure(text=f"Your Time: {self.finalTime}", fg_color=("#3B8ED0", "#1F6AA5"))
          if self.finalTime < self.bestTime:
              self.bestTime = self.finalTime
              self.df.loc[0, 'reaction'] = self.bestTime
              self.df.to_csv('components/high_scores.csv', index=False)

              self.bestTxt.configure(text=f"Best Time: {self.bestTime}")

        

    def afterDelay(self):
        self.waiting = False
        self.counting = True
        self.startTime = time.time_ns()
        self.btn.configure(text="CLICK ME", fg_color=("red", "red"))

