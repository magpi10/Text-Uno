import card

class Hand:
    def __init__(self):
        self.cards = []
        self.name = ""

    def sort(self):
        self.cards.sort(key = getKey)

    def getHandList(self):
        n = 0
        s = ""
        for i in self.cards:
            n = n + 1
            s = s + "%s: %s %s, " %(n, i.group, i.name)
        return(s)

    def removeCard(self, idx):
        self.cards.pop(idx)

    def hasCardWithName(self, name):
        for c in self.cards:
            if c.name == name:
                return(True)
        return(False)
    
    def getCardsWithName(self, name):
        r = []
        for c in self.cards:
            if c.name == name:
                r.append(c)
        return(r)

    def getCardsList(self, arr):
        n = 0
        s = ""
        for i in arr:
            n = n + 1
            s = s + "%s: %s %s, " %(n, i.group, i.name)
        return(s)
    
    def getCardIndex(self, group, name):
        for i in range(0, len(self.cards)):
            c = self.cards[i]
            if c.group == group and c.name == name:
                return(i)
        return(-1)

def getKey(elem):
    return(elem.getDesc(False))
