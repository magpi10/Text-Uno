import deck

d = deck.Deck()
d.shuffle()
for c in d.draw:
    print(c.group, c.name),