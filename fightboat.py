#!/usr/bin/python

import random

# Debug
DEBUG = 1

# Number of ships for each player
player_ships = 5

# Grid Dimensions
max_x = 9
max_y = 9

# Maximum number of ships that can be placed on the grid
max_ships = max_x * max_y

# Possible coordinate status
status = {'hit': 1, 'miss': 2, 'ship': 3}

def create_grid(max_x, max_y):
        '''Creates a nested list structure full of 0's. Pass the max_x and max_y values to determine grid size.'''
        return [[0] * max_x for x in range(max_y)]

def display_grid(grid):
        '''Takes a nested list structure as created by create_grid() as the argument. Displays the current status of the grid with appropriate labels and legend.'''
        count = max_y
        for coordinate in grid:
                print count, coordinate
                count = count - 1
        xaxis_label()
        legend()
        return None

def xaxis_label():
        '''Label the xaxis of the grid.'''
        print '\n ', range(1, max_x + 1), '\n'
        return None

def legend():
        '''Shows the user what the symbols in the grid mean.'''
        print status['hit'], '= Hit', status['miss'], '= Miss', status['ship'], '= Ship\n'
        return None

def insert_into_grid(grid, x, y, status):
        '''Inserts the status passed at the x and y coordinates provided into the grid provided.'''
        message = 'Inserting %s into grid at (%d, %d)' % (status, x+1, y)
        debug(message)
        grid[-y][x] = status
        return None

def random_coordinate():
        '''Returns a set of random coordinates inside the grid.'''
        x = random.choice(range(0, max_x))
        y = random.choice(range(1, max_y + 1))
        return x, y

def random_ship_placement(grid, number_ships):
        '''Places random ships on the grid.'''
        if number_ships > max_ships:
                debug('Too many ships are defined.')
        else:
                while number_ships > 0:
                        x, y = random_coordinate()
                        if grid[-y][x] == 0:
                                insert_into_grid(grid, x, y, status['ship'])
                                number_ships = number_ships - 1
                        else:
                                message = 'Coordinate duplication for ship placement. Trying again.'
                                debug(message)
        return None

def debug(string):
        '''Pass a string to print as a debug message if debugging is activated.'''
        if DEBUG == 1:
                print 'Debug===>', string
        return None

# Create a grid of 0's to hold coordinate status
grid1 = create_grid(max_x, max_y)

# Display grid to the user
display_grid(grid1)

random_ship_placement(grid1, player_ships)
display_grid(grid1)
