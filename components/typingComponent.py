import random
import threading
import tkinter
import tkinter.messagebox
import customtkinter
import typing
import keyboard
import queue
import time
import pandas as pd


class TypingComponent(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.df = None
        self.df = pd.read_csv('components/high_scores.csv')
        self.typing_high_score = self.df['typing'][0]

        self.typed = ""
        self.sentence = ""
        self.typo = False
        self.last_score = 0

        self.grid(row=0, column=1, padx=(5, 0), pady=(5, 0), rowspan=4, sticky="nsew")

        self.typing_high_score_label = customtkinter.CTkLabel(master=self, text="High Score: "+str(self.typing_high_score), anchor="w",
                                                     font=customtkinter.CTkFont(size=30, weight="bold"),
                                                     text_color=("lightblue"))
        self.typing_high_score_label.grid(row=2, column=0)
        self.typing_high_score_label.place(relx=0.1, rely=0.1)

        self.last_score_label = customtkinter.CTkLabel(master=self, text=(self.last_score != 0)*("Last Score: "+str(self.last_score)), anchor="w",
                                                     font=customtkinter.CTkFont(size=30, weight="bold"),
                                                     text_color=("lightblue"))
        self.last_score_label.grid(row=2, column=0)
        self.last_score_label.place(relx=0.1, rely=0.9)

        self.reset()


    def reset(self):
        self.df = pd.read_csv('components/high_scores.csv')
        self.typing_high_score = self.df['typing'][0]
        print(self.typing_high_score)
        self.typed = ""

        f = open('components/10000-english-usa.txt').read()
        sentences = f.split('\n')
        words = []
        for _ in range(5):
            words.append(random.choice(sentences))
        self.sentence = " ".join(words)
        print(self.sentence)
        self.sentence_label = customtkinter.CTkLabel(master=self, text=self.sentence, anchor="w",
                                                     font=customtkinter.CTkFont(size=30, weight="bold"),
                                                     text_color=("gray"))
        self.sentence_label.grid(row=2, column=0)
        self.sentence_label.place(relx=0.1, rely=0.4)

        input_queue = queue.Queue()
        kb_input_thread = threading.Thread(target=self.check_letter_pressed, args=(input_queue,))
        kb_input_thread.daemon = True
        kb_input_thread.start()

    def check_letter_pressed(self, input_queue):
        while True:
            event = keyboard.read_event()
            if event.event_type == 'down' and event.name.isalpha():
                print("Typing Begins")
                self.typed += event.name
                self.sentence_label.destroy()
                self.start_typing()
                break

    def start_typing(self):
        start_time = time.time()
        while self.typed != self.sentence:
            self.sentence_label = customtkinter.CTkLabel(master=self, text=self.sentence, anchor="w",
                                                     font=customtkinter.CTkFont(size=30, weight="bold"), text_color=("gray"))

            if self.typed != self.sentence[:len(self.typed)]:
                self.typo = True
                self.typed_label = customtkinter.CTkLabel(master=self, text=self.sentence[:len(self.typed)], anchor="w",
                                                         font=customtkinter.CTkFont(size=30, weight="bold"), text_color=("red"))
                self.typed_label.grid(row=2, column=0)
                self.typed_label.place(relx=0.1, rely=0.4)

            correct_typed = min(len(self.sentence), len(self.typed))
            for i, (c1, c2) in enumerate(zip(self.sentence, self.typed)):
                if c1 != c2:
                    correct_typed = i
                    break
            self.correct_typed_label = customtkinter.CTkLabel(master=self, text=self.sentence[:correct_typed], anchor="w",
                                                     font=customtkinter.CTkFont(size=30, weight="bold"), text_color=("white"))
            self.correct_typed_label.grid(row=2, column=0)
            self.correct_typed_label.place(relx=0.1, rely=0.4)

            self.sentence_label.grid(row=2, column=0)
            self.sentence_label.place(relx=0.1, rely=0.4)

            event = keyboard.read_event()
            while event.event_type != 'down':
                event = keyboard.read_event()
            if event.event_type == 'down':
                if event.name == 'backspace':
                    self.typed = self.typed[:-1]
                else:
                    if event.name == 'space':
                        event.name = ' '
                    elif event.name == 'period':
                        event.name = '.'
                    self.typed += event.name
                    print(self.typed)
            try:
                self.typed_label.destroy()
            except:
                pass

            self.sentence_label.destroy()
            self.correct_typed_label.destroy()

        end_time = time.time()
        duration_in_minutes = (end_time - start_time) / 60
        wpm = round(len(self.sentence.split())/duration_in_minutes, 2)
        print(wpm)
        self.last_score = wpm
        if wpm > self.typing_high_score:
            self.df.loc[0, 'typing'] = wpm
            self.df.to_csv('components/high_scores.csv', index=False)
            self.typing_high_score = wpm
        self.typing_high_score_label.configure(text="High Score: "+str(self.typing_high_score))
        self.last_score_label.configure(text=(self.last_score != 0)*("Last Score: "+str(self.last_score)))
        self.reset()

