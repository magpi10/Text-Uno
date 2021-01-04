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
currentStack = 0
game = True

while game == True:
    if len(deck.draw) == 0:
        for i in deck.discard:
            if i != deck.getCurrentDiscard():
                deck.draw.append(i)
                deck.discard.pop(i)
    currentHand = players[currentPlayer - 1]
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("It's player " + currentHand.name + "'s turn.")
    currentDiscard = deck.getCurrentDiscard()
    print("The top discard card is a " + currentDiscard.getDesc(True))
    if currentDiscard.name == "+2":
        currentStack = currentStack + 2
        if currentHand.hasCardWithName("+2") or currentHand.hasCardWithName("+4"):
            isValidMove = False
            while not isValidMove:
                r = currentHand.getCardsWithName("+2")
                r.append(currentHand.getCardsWithName("+4"))
                print("The cards you can play are:")
                print(currentHand.getCardsList(r))
                print()
                print("'d' = draw " + str(currentStack) + " cards, 'card number' = play card with number")
                move = input("What do you want to do? ")
                if move == "d":
                    for i in range(0,currentStack):
                        currentHand.cards.append(deck.getTopCard())
                        currentStack = 0
                        isValidMove = True
                elif move.isdigit():
                    cardNo = move
                    idx = int(cardNo) - 1
                    cardToPlay = r[idx]
                    idx = currentHand.getCardIndex(cardToPlay.group, cardToPlay.name)
                    currentHand.removeCard(idx)
                    deck.discard.append(cardToPlay)
                    isValidMove = True
                else:
                    print("Invalid Move")
        else:
            for i in range(0,currentStack):
                currentHand.cards.append(deck.getTopCard())
                currentStack = 0

    if currentDiscard.name == "+4":
        currentStack = currentStack + 4
        if currentHand.hasCardWithName("+2") or currentHand.hasCardWithName("+4"):
            isValidMove = False
            while not isValidMove:
                r = currentHand.getCardsWithName("+2")
                r.append(currentHand.getCardsWithName("+4"))
                print("The cards you can play are:")
                print(currentHand.getCardsList(r))
                print()
                print("'d' = draw " + str(currentStack) + " cards, 'card number' = play card with number")
                move = input("What do you want to do? ")
                if move == "d":
                    for i in range(0,currentStack):
                        currentHand.cards.append(deck.getTopCard())
                        currentStack = 0
                        isValidMove = True
                elif move.isdigit():
                    cardNo = move
                    idx = int(cardNo) - 1
                    cardToPlay = r[idx]
                    idx = currentHand.getCardIndex(cardToPlay.group, cardToPlay.name)
                    currentHand.removeCard(idx)
                    deck.discard.append(cardToPlay)
                    if currentDiscard.isValidMove(cardToPlay):
                        isValidMove = True
                else:
                    print("Invalid Move")
        else:
            for i in range(0,currentStack):
                currentHand.cards.append(deck.getTopCard())
                currentStack = 0

    currentHand.sort()
    print("Your cards are")
    print(currentHand.getHandList())
    isValidMove = False
    while not isValidMove:
        print()
        print("'d' = draw a card, 'card number' = play card with number")
        move = input("What do you want to do? ")
        if move == "d":
            currentHand.cards.append(deck.getTopCard())
            isValidMove = True
        elif move.isdigit():
            cardNo = move
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
                        newColor = newColor.lower()
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
                if cardToPlay.name == "switch":
                    n = 0
                    s = ""
                    otherPlayers = []
                    for i in range(0, len(players)):
                        if i != currentPlayer -1:
                            otherPlayers.append(players[i])
                    for i in otherPlayers:
                        n = n + 1
                        s = s + "%s: %s (%s cards), " %(n, p[i], (len(p[i].cards) + 1))
                    print(s)
                    playerNumber = input("Number of who you want to switch hands with: ")
                    playerNumber = int(playerNumber) - 1
                    ph = currentHand.cards
                    currentHand.cards = otherPlayers[playerNumber].cards
                    otherPlayers[playerNumber].cards = ph
        else:
            print("Invalid entry")
    currentPlayer = currentPlayer + direction
    if currentPlayer > n:
        currentPlayer = 1
    elif currentPlayer == 0:
        currentPlayer = n
    elif len(currentHand.cards) == 0:
        if currentDiscard.group == "black" or currentDiscard.name == "reverse" or currentDiscard.name == "+2" or currentDiscard == "block":
            print("You can't end on a special card take 1 card")
            currentHand.cards.append(deck.getTopCard())
        else:
            game = False

print(currentHand.name + " has won!")
