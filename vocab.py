import random
from nltk.corpus import wordnet as wn

class Vocab: 
    def __init__(self):
        self.words = [w for w in wn.all_lemma_names()]
       
        '''self.words = []
        numWords = 20000
        for i in wn.all_lemma_names():
            self.words.append(i)
            if(len(self.words) >= numWords):
                break
                '''
        self.definitions = [wn.synsets(w)[0].definition() for w in self.words]

    def wordToDef(self):
        allAnswers = []
        index = random.randint(0,len(self.definitions)-1)
        answerWord = self.words[index]
        answerDef = self.definitions[index]

        allAnswers.append(answerDef)
        for i in range(3):
            while True:
                index = random.randint(0,len(self.definitions)-1)
                if (self.definitions[index] in allAnswers): 
                    continue
                allAnswers.append(self.definitions[index])
                break
                
        print(answerWord)
        print(answerDef)


    def defToWord(self):
        allAnswers = []
        index = random.randint(0,len(self.definitions)-1)
        answerWord = self.words[index]
        answerDef = self.definitions[index]

        allAnswers.append(answerWord)
        for i in range(3):
            while True:
                index = random.randint(0,len(self.words)-1)
                if (self.words[index] in allAnswers): 
                    continue
                allAnswers.append(self.words[index])
                break


if __name__ == "__main__":
    voc = Vocab()
   # print(voc.words)
    print(len(voc.words))
    print(len(voc.definitions))
    #print(voc.definitions)
#    voc.wordToDef()
