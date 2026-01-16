import random

def tonegenerator(tone): 
    if tone == "Harsh":
        prefix = ["Brutal", "Ultimate", "Vengful", "Savage", "Fierce", "Relentless", "Ruthless"]
        name = ["Bulls", "Tigers", "Warriors", "Marauders", "Ravagers", "Ironclaws", "Destroyers"] 
    elif tone == "Elegant": 
        prefix = ["Shining", "Victorious", "Hopeful", "Noble", "Radiant", "Glorious", "Majestic"]
        name = ["Sanctum", "Concord", "Order", "Assembly", "Chronicle", "Legion", "Dynasty"]
    elif tone == "Whimsy": 
        prefix = ["Wacky", "Playful", "Wonky", "Zany", "Quirky", "Bubbly", "Cheerful", "Jolly"]
        name = ["Tricksters", "Mischiefs", "Gigglefolk", "Bumblekins", "Jesters", "Jokers", "Pranksters"]
    elif tone == "Mystical":
        prefix = ["Enchanted", "Arcane", "Mystic", "Ethereal", "Celestial", "Otherworldly", "Divine"]
        name = ["Wizards", "Sorcerers", "Mystics", "Seers", "Oracles", "Spellbinders", "Charmers"]
    elif tone == "Futuristic":
        prefix = ["Cyber", "Neo", "Quantum", "Hyper", "Nano", "Techno", "Digital", "Virtual"]
        name = ["Runners", "Synthesis", "Drones", "Cyborgs", "Mechs", "Bots", "Riders", "Hackers"]
    else:
        return "Invalid Choice"

    return random.choice(prefix) + " " + random.choice(name)

input_tone = input("Tone Choice(Harsh, Elegant, Whimsy, Mystical, Futuristic): ")
number_of_names = int(input("Number of Names to Generate: "))
for i in range(number_of_names):
    generator = tonegenerator(input_tone)
    print(generator)