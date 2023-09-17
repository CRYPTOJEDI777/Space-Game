# detects the card the user wants to play
# returns index of where the card is in the list
import random
def returnIdexOf(card, list):

    for x in range(len(list)):
        result = card.find(list[x])
        if(result != -1):
            return(x)


# moves one card from a list to another
#moveCard(card,discard,deck)

def moveCard(card,oldList,newlist ):
    cardIndex = returnIdexOf(card, oldList)

    newlist.append(oldList[cardIndex])
    oldList.remove(oldList[cardIndex])


# moves all items of one list to another
#moveAllCards(discard, deck)

def moveAllCards(oldList,newlist):
    for x in range(len(oldList)):
        moveCard(oldList[0],oldList,newlist)

def removeRandomCard(list):
    list.remove(random.choice(list))
