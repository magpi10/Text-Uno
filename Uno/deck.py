import card
from random import randint

class Deck:
    draw = []
    discard = []
    
    def __init__(self):
        self.draw = []
        self.discard = []
        for g in ["red", "green", "yellow", "blue"]:
            for n in range(1, 9):
                self.draw.append(card.Card(g,n))
                self.draw.append(card.Card(g,n))
            self.draw.append(card.Card(g,0))
            self.draw.append(card.Card(g,"+2"))
            self.draw.append(card.Card(g,"+2"))
            self.draw.append(card.Card(g,"block"))
            self.draw.append(card.Card(g,"block"))
            self.draw.append(card.Card(g,"reverse"))
            self.draw.append(card.Card(g,"reverse"))
    
    def shuffle(self):
        for i in range(len(self.draw)-1, 0, -1):
            j = randint(0, i + 1)
            self.draw[i], self.draw[j] = self.draw[j], self.draw[i]