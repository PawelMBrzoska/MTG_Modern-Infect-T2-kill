# Converter. Convert specific card to a game state
import classes

#Converting decklist to object readable by other functions using the CONVERTER dictionary
def Converter(card, game):
    
    #Lands

    ## Fetches
    if card == "Misty Rainforest":
        game.g_mana += 1
        game.u_mana += 1
        game.r_mana += 1
        game.total_mana += 1
    
    if card == "Windswept Heath":
        game.g_mana += 1
        game.u_mana += 1
        game.r_mana += 1
        game.total_mana += 1

    if card == "Wooded Foothills":
        game.g_mana += 1
        game.u_mana += 1
        game.r_mana += 1
        game.total_mana += 1  

    ## Duals

    if card == "Botanical Sanctum":
        game.g_mana += 1
        game.u_mana += 1
        game.total_mana += 1  

    if card == "Blooming Marsh":
        game.g_mana += 1
        game.total_mana += 1       

    if card == "Nurturing Peatland":
        game.g_mana += 1
        game.total_mana += 1  

    if card == "Breeding Pool":
        game.g_mana += 1
        game.u_mana += 1
        game.total_mana += 1

    if card == "Waterlogged Grove":
        game.g_mana += 1
        game.u_mana += 1
        game.total_mana += 1

    if card == "Copperline Gorge":
        game.g_mana += 1
        game.r_mana += 1
        game.total_mana += 1  

    if card == "Karplusan Forest":
        game.g_mana += 1
        game.r_mana += 1
        game.total_mana += 1  
    
    if card == "Grove of the Burnwillows":
        game.g_mana += 1
        game.r_mana += 1
        game.total_mana += 1  

    if card == "Stomping Ground":
        game.g_mana += 1
        game.r_mana += 1
        game.total_mana += 1  

    ## monoG lands

    if card == "Forest":
        game.g_mana += 1
        game.total_mana += 1

    if card == "Boseiju, Who Endures":
        game.g_mana += 1
        game.total_mana += 1

    if card == "Pendelhaven":
        game.g_mana += 1
        game.total_mana += 1
        
    ## Pumps

    if card == "Mutagenic Growth":
        game.dmg_2_free += 1

    if card == "Might of Old Krosa":
        game.dmg_4 += 1

    if card == "Giantic Growth":
        game.dmg_3 += 1

    if card == "Groundswell": 
        game.dmg_2_Groundswell += 1 #If there is a > 1 land card change to dmg_4

    if card == "Scale Up":
        game.scale_up = True

    if card == "Snakeskin Veil":
        game.dmg_1 += 1
        game.hex += 1

    if card == "Blossoming Defense":
        game.dmg_1 += 1
        game.hex += 1

    if card == "Assault Strobe":
        game.assault_strobe = True
        
    # ELF!

    if card == "Glistener Elf":
        game.elf = True
        
    # Return

    return(game)


def Get_Damage(game):

    if game.total_mana > 1:
        mana = 2
    else:
        mana = game.total_mana

    if game.g_mana > 1:
        mana_g = 2
    else:
        mana_g = game.g_mana

    if game.r_mana > 1:
        mana_r = 2
    else:
        mana_r = game.r_mana

    # for T2 combo
    if game.elf == True and mana > 0:
        game.t2_damage += 1
    else:
        return(0)
    #First of all use scale up
    if mana > 0 and game.scale_up == True:
        game.t2_damage += 5
        mana_g -= 1
        mana -= 1

    if game.dmg_2_free > 0:
        game.t2_damage += 2*game.dmg_2_free
        game.dmg_2_free = 0

    while mana > 0:

        if game.assault_strobe == True:
            mana_r -= 1
            mana -= 1
            game.doublestrike = True
            game.assault_strobe = False

        if game.dmg_2_Groundswell > 0 and game.total_mana > 1: # checking if the groundsfells landfall triger
            game.t2_damage += 4
            game.dmg_2_Groundswell -= 1
            mana_g -= 1
            mana -= 1
            continue

        if game.dmg_4 > 0:
            game.t2_damage += 4
            game.dmg_4 -= 1
            mana_g -= 1
            mana -= 1
            continue

        if game.dmg_3 > 0:
            game.t2_damage += 3
            game.dmg_3 -= 1
            mana_g -= 1
            mana -= 1
            continue

        if game.dmg_2 > 0:
            game.t2_damage += 2
            game.dmg_2 -= 1
            mana_g -= 1
            mana -= 1
            continue

        if game.dmg_1 > 0:
            game.t2_damage += 1
            game.dmg_1 -= 1
            mana_g -= 1
            mana -= 1
            continue

        # at this point there is no pumps left despite aveilable mana. So returning the score:
        return(game.t2_damage)

    else:
        return(game.t2_damage)


        


        





    
        


