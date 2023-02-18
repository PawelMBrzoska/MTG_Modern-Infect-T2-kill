# Converter. Convert specific card to a game state


class Game:
    def __init__(self, elf=bool, t2_damage=int, G_mana=int, U_mana=int, Total_mana=int):
        self.elf = False
        self.t2_damage = 0 
        self.G_mana = 0
        self.U_mana = 0
        self.Total_mana = 0


#Converting decklist to object readable by other functions using the CONVERTER dictionary
def Converter(card, game):
    
    if card == "Misty Rainforest":
        game.G_mana += 1
        game.U_mana += 1
        game.Total_mana += 1
    
    if card == "Breeding Pool":
        game.G_mana += 1
        game.U_mana += 1
        game.Total_mana += 1

    if card == "Glistener Elf":
        game.elf = True

    return(game)

