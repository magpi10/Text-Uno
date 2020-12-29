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

def getKey(elem):
    return(elem.getDesc())