deck = ['reactor', 'laser', 'thruster']
discard = ['reactor', 'laser']

# moves all items of one array to the next
def moveCards():
    for x in range(len(discard)):
        print(deck)
        deck.append(discard[x])



print("deck = ")
print(deck)
print("discard = ")
print(discard)
