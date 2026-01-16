import random

def tonegenerator(tone): 
    if tone == "Harsh":
        prefix = ["Brutal", "Ultimate", "Vengful", "Savage", "Fierce", "Relentless"]
        name = ["Bulls", "Tigers", "Warriors", "Marauders", "Ravagers", "Ironclaws"] 
    elif tone == "Elagant": 
        prefix = ["Shining", "Victorious", "Hopeful", "Noble", "Radiant", "Glorious"]
        name = [, "Sanctum", "Concord", "Order", "Assembly", "Chronicle"]
    elif tone == "Whimsy": 
        prefix = ["Wacky", "Playful", "Wonky", "Zany", "Quirky", "Bubbly"]
        name = ["Tricksters", "Mischiefs", "Gigglefolk", "Bumblekins", "Jesters", "Jokers"]
    elif tone == "Mystical":
        prefix = ["Enchanted", "Arcane", "Mystic", "Ethereal", "Celestial", "Otherworldly"]
        name = ["Wizards", "Sorcerers", "Mystics", "Seers", "Oracles", "Spellbinders"]
    elif tone == "Futuristic":
        prefix = ["Cyber", "Neo", "Quantum", "Hyper", "Nano", "Techno"]
        name = ["Runners", "Synths", "Drones", "Cyborgs", "Mechs", "Bots"]
    else:
        return "Invalid Choice"

    return random.choice(prefix) + " " + random.choice(name)

print(tonegenerator("Harsh"))
print(tonegenerator("Elagant"))
print(tonegenerator("Whimsy"))