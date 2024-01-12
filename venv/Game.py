from CardCreator import card
from DeckMaker import Deck
import random

def setup():
    global dek
    global playercount
    global dealercount
    playercount = 0
    dealercount = 0
    dek = Deck()
setup()
def draw():
    count = len(dek) - 1
    pos = random.randint(0,count)
    single = dek[pos]
    dek.pop(pos)

    return single
test = draw()
test.read()
print(len(dek))
setup()
test = draw()
test.read()
print(len(dek))