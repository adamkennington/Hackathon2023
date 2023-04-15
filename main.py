import tkinter
import tkinter.messagebox
import customtkinter
from components.sidebar import Sidebar
from components.triviaComponent import TriviaComponent
from components.vocabComponent import VocabComponent

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Self Improvement")
        self.geometry(f"{1100}x{700}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = Sidebar(self, self.sidebar_button_event, width=140, corner_radius=0)
        # self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        # self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        # self.sidebar_frame.grid_rowconfigure(4, weight=1)
        # self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Categories", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # self.sidebar_names = ['Typing', 'Math', 'Nutrition', 'Vocab', 'Reaction', 'Trivia', '7', '8', '9']
        # self.sidebar_buttons = []
        # for i in range(9):
        #     button = customtkinter.CTkButton(self.sidebar_frame, text=self.sidebar_names[i], command=lambda i=i: self.sidebar_button_event(i))
        #     button.grid(row=i+1, column=0, padx=20, pady=10, sticky="nsew")
        #     self.sidebar_frame.grid_rowconfigure(i+1, weight=1)
        #     self.sidebar_buttons.append(button)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=10, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=11, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=12, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=13, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter Text")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, text="Enter", fg_color="transparent",
                                                     command=self.entry_button_event,
                                                     border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

        # create tab frame
        
        self.tab_frame = None
        
        self.tab_label = None
        

    def createTrivia(self):
        self.tab_frame = TriviaComponent(self, corner_radius=0)
        self.tab_frame.grid(row=0, column=1, rowspan=3, columnspan=3, sticky="nsew")
        self.tab_label = customtkinter.CTkLabel(self.tab_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"))

    def createVocab(self):
        self.tab_frame = VocabComponent(self, corner_radius=0)
        self.tab_frame.grid(row=0, column=1, rowspan=3, columnspan=3, sticky="nsew")
        self.tab_label = customtkinter.CTkLabel(self.tab_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"))

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self, index):
        if self.tab_frame: 
            self.tab_frame.destroy()

        if self.sidebar_frame.sidebar_names[index] == "Trivia":
            self.createTrivia()

        if self.sidebar_frame.sidebar_names[index] == "Vocab":
            self.createVocab()

        print(f"{self.sidebar_frame.sidebar_names[index]} click")
        # self.tab_label.configure(text=f"{self.sidebar_frame.sidebar_names[index]}")

    def entry_button_event(self):
        text = f"{self.entry.get()}"
        print(text)


if __name__ == "__main__":
    app = App()
    app.mainloop()