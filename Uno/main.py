import deck
import hand

d = deck.Deck()
d.shuffle()
print(d.getDeckList())
print()

h = hand.Hand()

for i in range(0,7):
    h.cards.append(d.getTopCard())

print(h.getHandList())
h.sort()
print(h.getHandList())