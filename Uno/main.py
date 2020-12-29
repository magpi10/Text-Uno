import deck
import hand
import card

n = 0

while n <= 0 or n > 4: 
    n = input("Number of players: ")
    n = int(n)

players = []

for i in range(0, n):
    q = "What is player {pn}'s name: "
    name  = input(q.format(pn = i + 1))
    h = hand.Hand()
    h.name = name
    players.append(h)

deck = deck.Deck()
deck.shuffle()

for i in range(0,7):
    for p in players:
        p.cards.append(deck.getTopCard())

deck.discard.append(deck.getTopCard())


'''       
for p in players:
    print(p.name)
    print(p.getHandList())
'''

currentPlayer = 1

while True:
    currentHand = players[currentPlayer - 1]
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("It's player " + currentHand.name + "'s turn.")
    currentDiscard = deck.getCurrentDiscard()
    print("The top discard card is a " + currentDiscard.getDesc())
    currentHand.sort()
    print("Your cards are")
    print(currentHand.getHandList())
    print()
    print("'d' = draw a card, 'p n' = play card with number n")
    move = input("What do you want to do? ")
    if move == "d":
        currentHand.cards.append(deck.getTopCard())
        currentPlayer = currentPlayer + 1
        if currentPlayer > n:
            currentPlayer = 1
