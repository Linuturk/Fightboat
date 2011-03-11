#!/usr/bin/python

import random

print 'Welcome to Fight Boat!'
print 'Prepare to die!'

grid = ( 10, 10 )

def random_ships(grid):
        ships = {}
        while len(ships) <= 4:
                cord_x = random.choice(range(1, grid[0] + 1))
                cord_y = random.choice(range(1, grid[1] + 1))
                ships[cord_x] = cord_y
        return ships

player1 = random_ships(grid)
player2 = random_ships(grid)

print player1
print player2
