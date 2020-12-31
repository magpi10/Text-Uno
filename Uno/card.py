class Card:
    def __init__(self, g, n):
        self.group = g
        self.name = n
        self.newColor = ""
    
    def getDesc(self, isDiscard):
        if self.group == "black" and isDiscard:
            return("%s %s. New Color: %s" %(self.group, self.name, self.newColor))
        return("%s %s" %(self.group, self.name))

    def isValidMove(self, card):
        if card.group == "black":
            return(True)
        elif self.group == "black" and self.newColor == card.group:
            return(True)

        elif self.group != "black" and (card.group == self.group or card.name == self.name):
            return(True)
        else:
            return(False)
