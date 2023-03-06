# MTG_Modern-Infect-T2-kill
Simple app to calculating your winning chance in turn 2 agains goldfish with modern infect.

I assume T1 any land + elf, and in T2 going all in.

If you only want the results... well there are a lot of varaibility in decklists, and now the whole story with Rotpriest began and it need to be addressed in future. Anyway, for now with the old good UG infect, with more-or-less classical decklist the certain T2 kill in first 7 is ~1-3%. Not too good huh? The main problem is suprisingly not the scarcity of scale-ups and mutagenic growhts, but manascrew. Most decks plays like 18-20 land inluding 4 nexuses so 2 green sources in T2 is not so high... Deckbuilding like crazy with 4 scale ups all +4/+4 and 12 +3/+3, and with 20 UG lands the ods are ~ 15-20%. But this is of course nonoptimal for everything but T2 kill... so those 2% of T2 kills is the current state of the deck IMO. 

If you want to play test by yourself go on:

# Getting started

## Packages

First of all you need pandas for data processing. Easiest way is going for pip install.

> pip install pandas

# Running app

The script is easy and strightforward. It takes the decklist from Deck.txt. The format is the same as in the mtg goldfish so you can just copy-paste the imported decklist. Changing it manually is also OK since most of the cards necessary for T2 are already scripted (see converter.py). Anyway look up for typos. 

If you want to add cards see converter.py.