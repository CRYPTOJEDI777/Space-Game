import random
from main import *
from logic import *
from statManager import *

# 
def playcard(card):
    cardNamebase =['laser', 'reactor', 'thruster'] 
    index = returnIdexOf(card,cardNamebase)

    if(index == -1):
        print('card not found')

    elif(index == 0):
        print('ZAP!!')

    elif(index == 1):
        print('VROOM')
        reactor()
    
    elif(index == 2):
        print('BRRRRHHH')



def laser(list):
    statManager('power', -1)
    removeRandomCard(list)


def reactor(list):
    power = power + 3
