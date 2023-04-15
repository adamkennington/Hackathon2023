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

        self.grid(row=0, column=1, padx=(5, 0), pady=(5, 0), rowspan=4, sticky="nsew")

        """self.playing = False
        self.start_typing_button = customtkinter.CTkButton(master=self, text="Start", fg_color="transparent",
                                                           border_width=2, text_color=("gray10", "#DCE4EE"))
        self.start_typing_button.grid(row=2, column=0)
        self.start_typing_button.place(relx=0.4, rely=0.6)"""
        #self.start_typing()
        #root = tkinter.Tk()

        # bind the on_key_press function to the <Key> event
        #self.start_typing_button.bind('<Key>', self.on_key_press)
        input_queue = queue.Queue()
        kb_input_thread = threading.Thread(target=self.check_esc_pressed, args=(input_queue,))
        kb_input_thread.daemon = True
        kb_input_thread.start()

    def check_esc_pressed(self, input_queue):
        while True:
            event = keyboard.read_event()
            if event.event_type == 'down' and event.name.isalpha():
                print(event.name)
            #time.sleep(0.1)  # seconds

    """def on_press(self, event):
        if event.event_type == 'down' and event.name.isalpha():
            print(event.name)

    def start_typing(self):
        keyboard.on_press(self.on_press)
        keyboard.wait()
        #self.start_typing_button.destroy()"""
