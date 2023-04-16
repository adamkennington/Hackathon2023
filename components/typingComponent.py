import random
import threading
import tkinter
import tkinter.messagebox
import customtkinter
import typing
import keyboard
import queue
import time


class TypingComponent(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.typed = ""
        self.sentence = ""
        self.typo = False

        self.grid(row=0, column=1, padx=(5, 0), pady=(5, 0), rowspan=4, sticky="nsew")

        self.reset()


    def reset(self):
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
        self.sentence_label.place(relx=0.1, rely=0.5)

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
                self.start_typing()
                break

    def start_typing(self):
        while self.typed != self.sentence:
            self.sentence_label = customtkinter.CTkLabel(master=self, text=self.sentence, anchor="w",
                                                     font=customtkinter.CTkFont(size=30, weight="bold"), text_color=("gray"))

            if self.typed != self.sentence[:len(self.typed)]:
                self.typo = True
                self.typed_label = customtkinter.CTkLabel(master=self, text=self.sentence[:len(self.typed)], anchor="w",
                                                         font=customtkinter.CTkFont(size=30, weight="bold"), text_color=("red"))
                self.typed_label.grid(row=2, column=0)
                self.typed_label.place(relx=0.1, rely=0.5)

            correct_typed = min(len(self.sentence), len(self.typed))
            for i, (c1, c2) in enumerate(zip(self.sentence, self.typed)):
                if c1 != c2:
                    correct_typed = i
                    break
            self.correct_typed_label = customtkinter.CTkLabel(master=self, text=self.sentence[:correct_typed], anchor="w",
                                                     font=customtkinter.CTkFont(size=30, weight="bold"), text_color=("white"))
            self.correct_typed_label.grid(row=2, column=0)
            self.correct_typed_label.place(relx=0.1, rely=0.5)

            self.sentence_label.grid(row=2, column=0)
            self.sentence_label.place(relx=0.1, rely=0.5)
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
            if self.typo and self.typed == self.sentence:
                self.typed_label.destroy()
                self.typo = False

        self.sentence_label.destroy()
        self.correct_typed_label.destroy()
        self.reset()

