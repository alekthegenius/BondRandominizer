from random import randint
import math

bond_list = ["Dr. No", "From Russia with Love", "Goldfinger", "Thunderball", "You Only Live Twice", "On Her Majesty's Secret Service", "Diamonds are Forever", "Live and Let Die", "The Man with the Golden Gun", "The Spy Who Loved Me", "Moonraker", "For Your Eyes Only", "Octopussy", "A View to a Kill", "The Living Daylights", "License to Kill", "Golden Eye", "Tomorrow Never Dies", "The World is Not Enough", "Dies Another Day", "Casino Royale", "Quantum of Solace", "Skyfall", "Spectre", "No Time to Die"]

zeros = [0] * 25

bond_placeholder = dict(map(lambda i,j : (i,j) , bond_list, zeros))

for i in range(0, 2500000):
    rand = randint(0, len(bond_list) - 1)

    bond_placeholder[bond_list[rand]] += 1

final = dict(sorted(bond_placeholder.items(), 
                          key=lambda item: item[1]))

for i in final:
    print(i, bond_placeholder[i])

