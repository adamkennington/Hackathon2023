import tkinter
import tkinter.messagebox
import customtkinter
import pandas as pd
import random as rand

class MathComponent(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.df = None
        self.df = pd.read_csv('components/high_scores.csv')
        self.math_best_streak = self.df['math'][0]
        self.current_streak = 0
        self.output = None
        self.answer = 0
        self.initial_state = True

        self.math_best_streak_label = customtkinter.CTkLabel(master=self, text="High Score: "+str(self.math_best_streak), anchor="w",
                                                            font=customtkinter.CTkFont(size=30, weight="bold"),
                                                            text_color="lightblue")
        self.math_best_streak_label.grid(row=2, column=0)
        self.math_best_streak_label.place(relx=0.1, rely=0.1)

        self.current_streak_label = customtkinter.CTkLabel(master=self, text=(not self.initial_state)*("Last Score: "+str(self.current_streak)), anchor="w",
                                                       font=customtkinter.CTkFont(size=30, weight="bold"),
                                                       text_color="lightblue")
        self.current_streak_label.grid(row=2, column=0)
        self.current_streak_label.place(relx=0.1, rely=0.8)

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter Text")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.enter_button = customtkinter.CTkButton(master=self, text="Enter", fg_color="transparent", command=self.entry_button_event,
                                                     border_width=2, text_color=("gray10", "#DCE4EE"))
        self.enter_button.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.math_problem_label = customtkinter.CTkLabel(master=self,
                                                         text="", anchor="w",
                                                         font=customtkinter.CTkFont(size=30, weight="bold"),
                                                         text_color="lightblue")
        self.math_problem_label.grid(row=2, column=0)
        self.math_problem_label.place(relx=0.4, rely=0.4)

        self.answer_label = customtkinter.CTkLabel(master=self,
                                                         text="", anchor="w",
                                                         font=customtkinter.CTkFont(size=20, weight="bold"),
                                                         text_color="gray")
        self.answer_label.grid(row=2, column=0)
        self.answer_label.place(relx=0.4, rely=0.65)

        self.reset()

    def entry_button_event(self):
        self.initial_state = False
        user_entry = self.entry.get()
        if user_entry == int(self.entry.get()):
            user_entry = int(self.entry.get())
        if user_entry == str(self.output):
            self.current_streak += 1
            if self.current_streak > self.math_best_streak:
                self.df.loc[0, 'math'] = self.current_streak
                self.df.to_csv('components/high_scores.csv', index=False)
                self.math_best_streak = self.current_streak
        else:
            self.current_streak = 0

        self.answer_label.configure(text=f"{self.entry.get() == str(self.output)}  {self.answer}")
        self.current_streak_label.configure(text=(not self.initial_state)*("Current Streak: "+str(self.current_streak)))
        self.math_best_streak_label.configure(text="High Score: "+str(self.math_best_streak))

        self.entry.delete(0, "end")
        self.reset()
        
    def reset(self):
        self.df = pd.read_csv('components/high_scores.csv')
        self.math_best_streak = self.df['math'][0]
        
        self.output = None
        num1 = None
        num2 = None
        opertations = ["+", "-", "*", "/"]
        operator = rand.choice(opertations)

        if operator in "+-":
            num1 = rand.randint(-100, 100)
            num2 = rand.randint(-100, 100)
            self.output = eval(str(num1) + operator + str(num2))
        elif operator == "*":
            num1 = rand.randint(-25, 25)
            num2 = rand.randint(-25, 25)
            self.output = eval(str(num1) + operator + str(num2))
            while abs(abs(num1)-abs(num2)) < 20 and self.output > 100:
                num1 = rand.randint(-25, 25)
                num2 = rand.randint(-25, 25)
                self.output = eval(str(num1) + operator + str(num2))
        elif operator == "/":
            num1 = rand.randint(-100, 100)
            num2 = rand.randint(-25, 25)
            self.output = eval(str(num1) + operator + str(num2))
            while self.output != int(self.output) or num2 == 0 or abs(num2) <3:
                num1 = rand.randint(-100, 100)
                num2 = rand.randint(-25, 25)
                if num2 != 0:
                    self.output = eval(str(num1) + operator + str(num2))
        self.output = int(self.output)
        self.answer = f"{num1} {operator} {num2} = {self.output}"

        self.math_problem_label.configure(text=f"{num1} {operator} {num2} = ?")

        


