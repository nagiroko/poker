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
def draw(user):
    count = len(dek) - 1
    pos = random.randint(0,count)
    single = dek[pos]
    dek.pop(pos)
    single.read(user)
    return single.value
def game():
    playerbust = False
    dealerbust = False
    playercount = draw(name)
    playercount += draw(name)
    print(playercount)
def start():
    global name
    name = input("type name then enter ")
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


