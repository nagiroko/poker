from CardCreator import card
from DeckMaker import Deck
import random
import sys

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
def game():
    playerbust = False
    dealerbust = False
    drawedcard = draw()
    drawedcard.read("player")
    playercount = drawedcard.value
    drawedcard = draw()
    drawedcard.read("player")
    playercount += drawedcard.value
    print(playercount)
def start():
    decide = input("enter y to play blackjack. caps dont matter")
    decide = decide.capitalize()
    decide = decide.replace(" ",'')
    if decide == "Y":
        game()
    else:
        print("Okay have a nice day")
        sys.exit()
    print("Thanks for playing")
    sys.exit()
start()


