import card
from random import randint

class Deck:
    def __init__(self):
        self.draw = []
        self.discard = []
        for g in ["red", "green", "yellow", "blue"]:
            for n in range(1, 10):
                self.draw.append(card.Card(g,n))
                self.draw.append(card.Card(g,n))
            self.draw.append(card.Card(g,0))
            self.draw.append(card.Card(g,"+2"))
            self.draw.append(card.Card(g,"+2"))
            self.draw.append(card.Card(g,"block"))
            self.draw.append(card.Card(g,"block"))
            self.draw.append(card.Card(g,"reverse"))
            self.draw.append(card.Card(g,"reverse"))
        for g in range(0,4):
            self.draw.append(card.Card("black","change"))
        for g in range(0,4):
            self.draw.append(card.Card("black","+4"))
        self.draw.append(card.Card("black","switch"))
    
    def shuffle(self):
        for i in range(len(self.draw)-1, 0, -1):
            j = randint(0, i + 1)
            self.draw[i], self.draw[j] = self.draw[j], self.draw[i]
    
    def getDeckList(self):
        s = ""
        for i in self.draw:
            s = s + "%s %s, " %(i.group, i.name)
        return(s)
    
    def getTopCard(self):
        return(self.draw.pop(0))

    def getCurrentDiscard(self):
        return(self.discard[len(self.discard) - 1])
