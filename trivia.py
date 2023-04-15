import requests
from random import randrange
import base64
DIFFICULTY = ["random", "easy", "medium", "hard"]
CAT_ID = 8 # General Knowledge has index of 1, but ID of 1 + 8 = 9 in the DB
CATEGORIES = ["Random", 
              "General Knowledge",
              "Entertainment: Books",
              "Entertainment: Film",
              "Entertainment: Music",
              "Entertainment: Musicals & Theatres",
              "Entertainment: Television",
              "Entertainment: Video Games",
              "Entertainment: Board Games",
              "Science & Nature",
              "Science: Computers",
              "Science: Mathematics",
              "Mythology",
              "Sports",
              "Geography",
              "History",
              "Politics",
              "Art",
              "Celebrities",
              "Animals",
              "Vehicles",
              "Entertainment: Comics",
              "Science: Gadgets",
              "Entertainment: Japanese Anime & Manga",
              "Entertainment: Cartoon & Animations"
            ]



def b64toS(b):
    return base64.b64decode(b).decode('utf-8')

class Trivia:

    def __init__(self, category: int, difficulty: int):
      self.category: int = category
      self.difficulty: int = difficulty

    def getURL(self) -> str:
        cat=""
        diff=""
        if self.category > 0:
            cat = f"&category={self.category + CAT_ID}"

        if self.difficulty > 0:
            diff = f"&difficulty={DIFFICULTY[self.difficulty]}"
        
        return f"https://opentdb.com/api.php?amount=10{cat}{diff}&type=multiple&encode=base64"
    
    def getTrivia(self) -> dict:
        URL = self.getURL()
        response: requests.Response = requests.get(URL)
        if response.status_code == 404:
            raise Exception("!!! 404 !!!")
        res = response.json()
        trivia = []

        for result in res["results"]:
            question = {}
            question["question"] = b64toS(result["question"])
            correctIndex = randrange(0, 4)
            question["correct"] = correctIndex
            question["answers"] = []
            
            incorrectInd = 0
            for i in range(4):
                if i == correctIndex:
                    question["answers"].append(b64toS(result["correct_answer"])) 
                else:
                    question["answers"].append(b64toS(result["incorrect_answers"][incorrectInd]))
                    incorrectInd += 1

            trivia.append(question)      

        return trivia

if __name__ == "__main__":
    triv = Trivia(1, 1)
    print(triv.getTrivia())