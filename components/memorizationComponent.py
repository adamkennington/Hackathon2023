import random
import threading
import tkinter
import tkinter.messagebox
import customtkinter
import keyboard
import queue
import time

class MemorizationComponent(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.typed = ""
        self.sentence = ""
        self.shown = ""
        self.typo = False
        self.shownLetters = 0
        self.prevScore = ""
        self.currentScore = 0

        self.grid(row=0, column=1, padx=(5, 0), pady=(5, 0), rowspan=4, sticky="nsew")

        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        sequence = []
        for _ in range(25):
            sequence.append(random.choice(letters))
        self.sentence = "".join(sequence)
        print(self.sentence)

        self.instructions = customtkinter.CTkLabel(self, text="Copy the letters.\nPress enter to submit your answer.")
        self.instructions.grid(row=0, column=0)
        self.instructions.place(relx = 0.5, rely = 0.1,anchor=tkinter.CENTER)

        self.reset()

    def reset(self):

        self.score_label = customtkinter.CTkLabel(self, text=self.prevScore)
        self.score_label.grid(row=0, column=2)
        self.score_label.place(relx=0.8, rely=0.1)

        self.typed = ""
        self.shownLetters += 1
        self.shown = self.sentence[:self.shownLetters]
        self.sentence_label = customtkinter.CTkLabel(master=self, text=self.shown, anchor="w",
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
                self.sentence_label.destroy()
                self.start_typing()
                break

    def start_typing(self):         

        while True:
            self.typed_label = customtkinter.CTkLabel(master=self, text=self.typed, anchor="w",
                                                     font=customtkinter.CTkFont(size=30, weight="bold"), text_color=("gray"))
            self.typed_label.grid(row=2, column=0)
            self.typed_label.place(relx=0.1, rely=0.5)

            if self.typed == 'enter':
                self.typed_label.configure(text = 'FAILURE')
                
                self.prevScore = 'Your score: ' + str(self.currentScore)
                self.score_label.configure(text = self.prevScore)
                self.currentScore = 0
                self.configure(fg_color = "red") 
                while True:
                    event = keyboard.read_event()
                    if event.event_type == 'down':        
                        self.typed_label.destroy()
                        self.__init__(self.master)
                        break
                break
            
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
                    elif event.name == 'enter':
                        break
                    self.typed += event.name
                    print(self.typed)
                self.typed_label.destroy()
            
        if self.typed != self.shown:
            self.typed_label.configure(text = 'FAILURE')
            self.prevScore = 'Your score: ' + str(self.currentScore)
            self.score_label.configure(text = self.prevScore)
            self.currentScore = 0
            self.configure(fg_color = "red")
           
            while True:
                event = keyboard.read_event()
                if event.event_type == 'down':
                    self.typed_label.destroy()
                    self.__init__(self.master)
                    break            

        else:
            self.currentScore = len(self.typed)
            self.typed_label.destroy()
            self.reset()
