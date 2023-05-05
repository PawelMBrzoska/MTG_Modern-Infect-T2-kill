# Main of MTG modern infect T2 kill chance calculator (v1.3)
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import os
import sys
import converter
import classes

#Setting directory
os.chdir(os.path.dirname(sys.argv[0]))

def Start(Test):

    def Run():
        Deck = Get_Deck()
        try: 
            i = int(Iterations_textbox.get("1.0", "end-1c")) # this .get("1.0", "end-1c") means from the beginning to end
            handsize = int(Handsize_textbox.get("1.0", "end-1c"))
            Test.Test_go(Deck, i, handsize) 
            print(Test)
            pd.Series(Test.poison).value_counts().sort_index().plot(kind='bar')
            plt.show() 
        except ValueError:
            print("Simulation broke. Iterations number and handsize have to be numbers.")
         
    def Save_deck():
        text = Deck_textbox.get("1.0", "end-1c")
        with open("Deck.txt", "w") as file:
            file.write(text)
        print("Deck saved")

    def Get_Deck():
        #Getting the list from the txt file generated by goldfish.
        text = Deck_textbox.get("1.0", "end-1c") # Get the whole textbox as text
        df = text.splitlines()
        deck = []
        for line in df:
            # Goldfish add sidebord after an empty line. As we do not want sideboard the for loop breaks after empty line.
            if line != "":
                for i in range(0,int(line[0])):
                    deck.append(line[2:])
            else:
                break
        #Saving as a list to pass it to convertet
        return(deck)

    frm = ttk.Frame(Test.window, padding=10) #Creating the GUI frame
    frm.grid()

    #Creating stuff and placing it on the frame 

    Label(frm, text="The Deck").grid(column=1, row=1)

    Button(frm, text="Run the simulation", command=Run).grid(column=2, row=6)
    Button(frm, text="Quit", command=Test.window.destroy).grid(column=2, row=12)
    Button(frm, text="Save the deck", command=Save_deck).grid(column=2, row=7)

    Deck_textbox = Text(frm, height=18, width=28)
    Deck_textbox.grid(column=1, row=2, rowspan=11) # Eddit the rowspan to line up with buttons!
    Deck_textbox.insert(END, open("Deck.txt").read())

    Label(frm, text="Iterations number:").grid(column=2, row=2)
    Iterations_textbox = Text(frm, height=1, width=8)
    Iterations_textbox.grid(column=2, row=3) 
    Iterations_textbox.insert(END, "10000")

    Label(frm, text="Handsize:").grid(column=2, row=4)
    Handsize_textbox = Text(frm, height=1, width=3)
    Handsize_textbox.grid(column=2, row=5) 
    Handsize_textbox.insert(END, "7")

    # Running the mainloop
    Test.window.mainloop()

if __name__ == "__main__":

    Test = classes.Test()
    Test.window = Tk()
    Start(Test)


