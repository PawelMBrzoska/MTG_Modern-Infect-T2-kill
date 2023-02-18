# Main of MTG Modern Infect T2 kill chance calculator
import random
import pandas as pd
import os
import sys
import converter

#Setting directory
os.chdir(os.path.dirname(sys.argv[0]))

class Game:
    def __init__(self, elf=bool, t2_damage=int, G_mana=int, U_mana=int, Total_mana=int):
        self.elf = False
        self.t2_damage = 0 
        self.G_mana = 0
        self.U_mana = 0
        self.Total_mana = 0

    def __str__(self):
        return f"Game: Elf = {self.elf}, Total poison in T2 = {self.t2_damage}, Total mana = {self.Total_mana} including {self.G_mana} green mana"

class Test:
    def __init__(self, deck=None, win=int, games=int):
        self.deck = deck
        self.win = win
        self.games = games

    def __str__(self):
        ratio = (self.win/self.games)*100
        return f"With this deck without mulligans you should win {self.win} out of {self.games} games. This is {ratio}%"


def Get_Deck(file):
    #Getting the list from the txt file generated by goldfish.
    df = open(file).read().splitlines()
    deck = []
    for line in df:
        # Goldfish add sidebord after an empty line. As we do not want sideboard the for loop breaks after empty line.
        if line != "":
            for i in range(0,int(line[0])):
                deck.append(line[2:])
        else:
            break
    #Saving is as a list to pass it to convertet
    return(deck)

def Get_Hand(deck, cards):
    hand = random.choices(deck, k=cards)
    return(hand)

def Game_setup(hand, game=Game()):
    #Itterating through hand to get the game stat
    for cards in hand:
        game = converter.Converter(cards, game) #Using external converter to update the state of the game.

    return(game)

# Resetting game
def Game_reset(game=Game()):
    game.elf = False
    game.t2_damage = 0 
    game.G_mana = 0
    game.U_mana = 0
    game.Total_mana = 0

    return(game)

def Start(test=Test()):
    test.deck = Get_Deck("Deck.txt")
    test.games=0
    test.win=0

    return(test)

def Game_go(test=Test(),i=int):
    Current_game = Game()
    for a in range(i):
        test.games += 1
        Current_game = Game_reset(Current_game)
        Hand = Get_Hand(test.deck, 7)
        Current_game = Game_setup(Hand,Current_game)
        if Current_game.t2_damage >= 10:
           test.win += 1
        print(Current_game)
    
    return(test)

# Creating a new test with 10 repetitions. I will creaete some more fancy GUI in few days (hopefully xD)
Test1 = Test()
Test1 = Start(Test1)
Test1 = Game_go(Test1,10)

# Printing the results of the test. 
print(Test1)


