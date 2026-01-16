import random

def tonegenerator(tone): 
    if tone == "Harsh":
        prefix = ["Brutal", "Ultimate", "Vengful", "Savage", "Fierce", "Relentless"]
        name = ["Bulls", "Tigers", "Warriors", "Marauders", "Ravagers", "Ironclaws"] 
    elif tone == "Elagant": 
        prefix = ["Shining", "Victorious", "Hopeful", "Noble", "Radiant", "Glorious"]
        name = ["Saints", "Sanctum", "Concord", "Order", "Assembly", "Chronicle"]
    elif tone == "Whimsy": 
        prefix = ["Wacky", "Playful", "Wonky", "Zany", "Quirky", "Bubbly"]
        name = ["Tricksters", "Mischiefs", "Gigglefolk", "Bumblekins", "Jesters", "Jokers"]
    else:
        return "Invalid Choice"

        