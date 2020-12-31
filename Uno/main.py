import deck
import hand
import card

n = 0

while n <= 1 or n > 6: 
    n = input("Number of players: ")
    n = int(n)
    if n <= 1 or n > 6:
        print("Only 2 - 6 players can play")

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

d = deck.getTopCard()

while d.group == "black":
    deck.draw.append(d)
    d = deck.getTopCard()
    
deck.discard.append(d)


'''       
for p in players:
    print(p.name)
    print(p.getHandList())
'''

currentPlayer = 1
direction = 1

while True:
    currentHand = players[currentPlayer - 1]
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("It's player " + currentHand.name + "'s turn.")
    currentDiscard = deck.getCurrentDiscard()
    print("The top discard card is a " + currentDiscard.getDesc(True))
    if currentDiscard.name == "+2": 
        for i in range(0,2):
            currentHand.cards.append(deck.getTopCard())

    if currentDiscard.name == "+4":
        for i in range(0,4):
            currentHand.cards.append(deck.getTopCard())

    currentHand.sort()
    print("Your cards are")
    print(currentHand.getHandList())
    isValidMove = False
    while not isValidMove:
        print()
        print("'d' = draw a card, 'p n' = play card with number n")
        move = input("What do you want to do? ")
        if move == "d":
            currentHand.cards.append(deck.getTopCard())
            isValidMove = True
        elif move.startswith("p "):
            cardNo = move[2:]
            idx = int(cardNo) - 1
            cardToPlay = currentHand.cards[idx]
            if currentDiscard.isValidMove(cardToPlay):
                currentHand.removeCard(idx)
                deck.discard.append(cardToPlay)
                isValidMove = True
                if cardToPlay.name == "change" or cardToPlay.group == "black":
                    newColor = ""
                    while newColor == "":
                        newColor = input("Please enter the new color")
                        newColor.lower()
                        if newColor != "red" and newColor != "yellow" and newColor != "green" and newColor != "blue":
                            newColor = ""
                            print("Invalid color")
                    cardToPlay.newColor = newColor
                if cardToPlay.name == "reverse":
                    direction = direction * -1
                if cardToPlay.name == "block":
                    currentPlayer = currentPlayer + direction
                    if currentPlayer > n:
                        currentPlayer = 1
                    if currentPlayer == 0:
                        currentPlayer = n
        else:
            print("Invalid entry")
    currentPlayer = currentPlayer + direction
    if currentPlayer > n:
        currentPlayer = 1
    if currentPlayer == 0:
        currentPlayer = n
