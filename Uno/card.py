class Card:
    def __init__(self, g, n):
        self.group = g
        self.name = n
    
    def getDesc(self):
        return("%s %s" %(self.group, self.name))