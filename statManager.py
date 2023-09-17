from logic import *
from main import *
import main
statNamebase = ['power', 'health', 'sheilds' ]

#input the stat that needs to be changed and the mount it's changing by
def statManager(stat, num): 
    index = returnIdexOf(stat,statNamebase)

    if(main.playerTurn):

        if(index == -1):
            print('error finding stat')

        elif(index == 0):
            power = power + num

        elif(index == 1):
            health = health + num
    
        elif(index == 1):
            sheilds = sheilds + num
            
    elif(True):
        if(index == -1):
            print('error finding stat')

        elif(index == 0):
            power = power + num

        elif(index == 1):
            health = health + num
    
        elif(index == 1):
            sheilds = sheilds + num


    