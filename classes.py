

class Game:
    def __init__(self):
        self.elf = bool()
        self.dmg_1 = int
        self.dmg_2 = int
        self.dmg_2_free = int
        self.dmg_2_Groundswell = int
        self.dmg_3 = int
        self.dmg_4 = int
        self.scale_up = bool
        self.assault_strobe = bool
        self.doublestrike = bool
        self.t2_damage = int 
        self.hex = int
        self.g_mana = int
        self.u_mana = int
        self.r_mana = int
        self.total_mana = int

    def __str__(self):
        return f"""
                Game: Elf = {self.elf}, double strike = {self.doublestrike}, Total poison in T2 = {self.t2_damage}, 
                Total mana = {self.total_mana} including {self.g_mana} green mana and {self.r_mana} red mana
                """


class Test:
    def __init__(self, deck=None):
        self.deck = deck
        self.win = int
        self.elfs = int
        self.games = int
        self.poison = []
        self.manascrew = int
        self.pumpscrew = int

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
    
