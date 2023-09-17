import random
from logic import *
from CardActions import *

playerTurn = True

text = 'failed to update text'
text1 = ''

deck = ['reactor', 'laser', 'thruster']
hand = []
discard = []

power = 3
shields = 3


def updateGraphics():
    print('POWER: ' + str(power))
    print('shields : ' + str(shields))
    print('DECK:')
    print(deck)
    print('HAND:')
    print(hand)
    print('DISCARD:')
    print(discard)
    print(" \n")

def draw():

    card = random.choice(deck)
    moveCard(card,deck,hand)
    print("You drew a "+card + "!")

def play(card):

    moveCard(card,hand,discard)
    print("You Played a "+card + "!")
    playcard(card)


playing = True

while(playing):
    userInput = input("input: ")

    #GAME SETTINGS
    if(userInput == 'q'):
        playing = False

    #DRAWING A CARD
    if('draw' in userInput):
        try:
            draw()
        except:
            moveAllCards(discard,deck)
        updateGraphics()

    #PLAYING A CARD
    if('play' in userInput):

        index = returnIdexOf(userInput,hand)

        play(hand[index])
        updateGraphics()
        
        
