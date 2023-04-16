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
        # self.game.grid_rowconfigure(2, weight=4)
        self.game.grid_rowconfigure(0, weight=1)
        self.game.grid_rowconfigure(1, weight=1)
        self.game.grid_rowconfigure(2, weight=3, minsize=40)

        self.game.grid_columnconfigure(0, weight=1)
        self.game.grid_columnconfigure(1, weight=3)
        self.game.grid_columnconfigure(2, weight=1)
        
        

        self.playing: bool = False
        self.categories = []
        self.selectedCat = 0
        self.selectedDiff = 0

        


        # for when you start playing
        self.questions = []
        self.questionNum = 0
        self.qestionText = None

        self.questionBtnsContainer = customtkinter.CTkFrame(self.game, corner_radius=0, fg_color=("gray81", "gray20"))
        self.questionBtnsContainer.grid(row=2, column=1, sticky="nsew")

        for i in range(0, 2):
          self.questionBtnsContainer.grid_rowconfigure(i, weight=1)
          self.questionBtnsContainer.grid_columnconfigure(i, weight=1)
        self.questionBtns = []
        self.correctNum = 0
        self.nextQBtn = None

        self.cats = None
        self.diff = None
        self.playButton = None
        self.drawHeader()



    def pick_cat_event(self, el):
        print(f"{el} click")
        self.selectedCat = trivia.CATEGORIES.index(el)

    def pick_diff_event(self, el):
        print(f"{el} click")
        self.selectedDiff = trivia.DIFFICULTY.index(el)

    def drawHeader(self):
        textbox = customtkinter.CTkLabel(self.header, text="Category:")
        textbox.grid(row=0, pady=15, column=0)
        self.cats = customtkinter.CTkOptionMenu(master=self.header, width=300,
                                       values=trivia.CATEGORIES,
                                       command=self.pick_cat_event)
        self.cats.grid(row=1, column=0, padx=20, pady=10)


        textbox = customtkinter.CTkLabel(self.header, text="Difficulty:")
        textbox.grid(row=0, pady=15, column=1)
        self.diffs = customtkinter.CTkOptionMenu(master=self.header,
                                       values=trivia.DIFFICULTY,
                                       command=self.pick_diff_event)
        self.diffs.grid(row=1, column=1, padx=20, pady=10)
        self.playButton = customtkinter.CTkButton(self.header, text="Play!", command=self.play)
        self.playButton.grid(row=1, column=3, pady=15)

    def play(self):
        self.cats.configure(state="disabled")
        self.diffs.configure(state="disabled")
        self.playButton.configure(state="disabled")
        triviaInstance = trivia.Trivia(self.selectedCat, self.selectedDiff)

        self.questions = triviaInstance.getTrivia()
        
        self.questionNum = 0
        self.playing = True


        self.questionText = customtkinter.CTkLabel(self.game, text=f"Question {self.questionNum + 1}: {self.questions[self.questionNum]['question']}")

        self.questionText.grid(row=0, column=0, columnspan=3, sticky="nsew")
        
        for i in range(4):
            button = customtkinter.CTkButton(self.questionBtnsContainer, 
            text=self.questions[self.questionNum]["answers"][i], command=lambda i=i: self.answer(i))

            button.grid(row=i//2, column=i%2, padx=20, pady=10, sticky="nsew")
            
            self.questionBtns.append(button)

        self.nextQBtn = customtkinter.CTkButton(self.game, text="Next", command=self.nextQuestion, state="disabled")
        self.nextQBtn.grid(row=1, column=1)



    def answer(self, ans):
        if self.questions[self.questionNum]["correct"] == ans:
            self.correctNum += 1
            print("Correct!")
        else:
            print("Wrong...")
        self.nextQBtn.configure(state="normal")
        for i in range(4):
            if i == self.questions[self.questionNum]["correct"]:
                self.questionBtns[i].configure(state="disabled", fg_color="green")
            else:
                self.questionBtns[i].configure(state="disabled", fg_color="red")

        # self.nextQuestion()

    def nextQuestion(self):
        if self.questionNum == 9:
            self.nextQBtn.configure(state="disabled")
            self.questionText.configure(text=f"You answered {self.correctNum} questions correctly!")
            return

        self.questionNum += 1
        self.questionText.configure(text=f"Question {self.questionNum + 1}: {self.questions[self.questionNum]['question']}")
        self.nextQBtn.configure(state="disabled")
        for i in range(4):
            self.questionBtns[i].configure(text=self.questions[self.questionNum]["answers"][i], state="normal", fg_color=("#3B8ED0", "#1F6AA5"))




