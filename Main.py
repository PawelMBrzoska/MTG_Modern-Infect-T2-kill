# Main of MTG Modern Infect T2 kill chance calculator
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import converter
import classes

#Setting directory
os.chdir(os.path.dirname(sys.argv[0]))

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

def Start(wait, Test, Deck):
    while wait == True:
        try:
            i = int(input("How many itterations you want to make during the test? (Suggesting: 10.000)"))
        except ValueError:
            print("Itteration number have to be a positive whole number.")
            continue
        
        try:
            handsize = int(input("How many cards in hand? (Suggesting: 7)"))
        except ValueError:
            print("Card number in hand have to be a positive whole number.")
            continue

        wait = False
    
    Test.Test_go(Deck, i, handsize) # i = number of itterations

    print(Test)
    pd.Series(Test.poison).value_counts().sort_index().plot(kind='bar')
    plt.show()

    Start(True, Test, Deck)

if __name__ == "__main__":

    Deck = Get_Deck("Deck.txt")
    Test = classes.Test()
    Start(True, Test, Deck)


