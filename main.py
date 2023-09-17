import random
from logic import *

deck = ['reactor', 'laser', 'thruster']
hand = []
discard = []

def update():
    print("\n \n \n \n HAND:")
    print(hand)
    print(" \n \n")

def draw():

    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)
    print("You drew a "+card + "!")

def play(card):

    discard.append(card)
    hand.remove(card)
    print("You Played a "+card + "!")


playing = True

while(playing):
    userInput = input("input: ")

    #GAME SETTINGS
    if(userInput == 'q'):
        playing = False

    if('draw' in userInput):
        draw()

    if('play' in userInput):
        play(hand[findCard(hand,userInput)])
        update()
        
        
