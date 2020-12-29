import card

class Hand:
    cards = []

    def sort(self):
        self.cards.sort(key = getKey)

    def getHandList(self):
        s = ""
        for i in self.cards:
            s = s + "%s %s, " %(i.group, i.name)
        return(s)

def getKey(elem):
    return(elem.getDesc())