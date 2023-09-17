# detects the card the user wants to play
# returns index of where the card is in the hand array
def findCard(hand, card):

    for x in range(len(hand)):
        result = card.find(hand[x])
        if(result != -1):
            return(x)

print("Card not in hand!")