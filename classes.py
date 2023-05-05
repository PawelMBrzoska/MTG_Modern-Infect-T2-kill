import random
import converter

class Game:
    """
    This is the game class which holds information for each simulated game. 
    If you are greedy you could save each simulated game to check it manually later by saving this objects throughout simulation (e.g., at the beggining of the Game_reset() idk).
    """
    def __init__(self):
        self.elf: bool = False
        self.dmg_1: int = 0
        self.dmg_2: int = 0
        self.dmg_2_free: int = 0
        self.dmg_2_Groundswell: int = 0
        self.dmg_3: int = 0
        self.dmg_4: int = 0
        self.scale_up: bool = False
        self.assault_strobe: bool = False
        self.doublestrike: bool = False
        self.t2_damage: int = 0
        self.hex: int = 0
        self.g_mana: int = 0
        self.u_mana: int = 0
        self.r_mana: int = 0
        self.total_mana: int = 0

    def __str__(self):
        return f"""
                Game: Elf = {self.elf}, double strike = {self.doublestrike}, Total poison in T2 = {self.t2_damage}, 
                Total mana = {self.total_mana} including {self.g_mana} green mana and {self.r_mana} red mana
                """

    def Game_reset(self):
        self.elf = False
        self.dmg_1 = 0
        self.dmg_2 = 0
        self.dmg_2_free = 0
        self.dmg_2_Groundswell = 0
        self.dmg_3 = 0
        self.dmg_4 = 0
        self.scale_up = False
        self.assault_strobe = False
        self.doublestrike = False
        self.t2_damage = 0 
        self.hex = 0
        self.g_mana = 0
        self.u_mana = 0
        self.r_mana = 0
        self.total_mana = 0

    def Game_setup(self, deck, handsize):
        #Itterating through hand to get the game stat
        hand = random.choices(deck, k=handsize)

        for cards in hand:
            self = converter.Converter(cards, self) #Using external converter to update the state of the game.




class Test:
    def __init__(self, deck=None):
        self.deck = deck
        self.win = int
        self.elfs = int
        self.games = int
        self.poison = []
        self.manascrew = int
        self.pumpscrew = int
        self.window: Tk()

    def __str__(self):
        ratio_win = (self.win/self.games)*100
        ratio_elf = (self.elfs/self.games)*100
        ratio_manascrew = (self.manascrew/self.games)*100
        ratio_pumpscrew = (self.pumpscrew/self.games)*100
        return f"""
                With this deck without mulligans you should win {self.win} out of {self.games} games. This is {ratio_win}%.
                In {ratio_elf}% games you have T1 elf - so potential to up to {ratio_elf}% of wins in t2 :p
                Plans have been thwarted by manascrew {self.manascrew} times ({ratio_manascrew }%) 
                and {self.pumpscrew} by pumps shortage ({ratio_pumpscrew}%)
                """


    def Test_go(self, deck, i, handsize):

        self.deck = deck
        self.games=0
        self.win=0
        self.elfs=0
        self.poison = []
        self.manascrew = 0
        self.pumpscrew = 0

        Current_game = Game()

        for a in range(i):
            self.games += 1
            Current_game.Game_reset()
            Current_game.Game_setup(self.deck, handsize)

            Current_game.t2_damage = converter.Get_Damage(Current_game)
            if Current_game.doublestrike == True:
                Current_game.t2_damage *= 2

            if Current_game.elf == True:
                self.elfs += 1
                if Current_game.t2_damage >= 10:
                    self.win += 1
                else:
                    if Current_game.total_mana < 2:
                        self.manascrew += 1
                    else:
                        self.pumpscrew += 1
            
            self.poison.append(Current_game.t2_damage)       
        print("done")


