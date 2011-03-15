#!/usr/bin/python

import random

# Number of ships for each player
max_ships = 5

# Grid Dimensions
max_x = 9
max_y = 9

# Possible coordinate status
hit = 1
miss = 2
ship = 3

def create_grid(max_x, max_y):
        '''Creates a nested list structure full of 0's. Pass the max_x and max_y values to determine grid size.'''
        return [[0] * max_x for x in range(max_y)]

def display_grid(grid):
        '''Takes a nested list structure as created by create_grid() as the argument. Displays the current status of the grid with appropriate labels and legend.'''
        xaxis_label()
        count = 1
        for coordinate in grid:
                print count, coordinate, count
                count = count + 1
        xaxis_label()
        legend()
        return None

def xaxis_label():
        '''Label the xaxis of the grid.'''
        print '\n ', range(1, max_x + 1), '\n'
        return None

def legend():
        '''Shows the user what the symbols in the grid mean.'''
        print hit, '= Hit', miss, '= Miss', ship, '= Ship'
        return None

def insert_grid(grid, x, y, status):
        '''Inserts the status passed at the x and y coordinates provided into the grid provided.'''
        grid[y].insert(x, status)
        return None

# Create a grid of 0's to hold coordinate status
grid = create_grid(max_x, max_y)

# Display grid to the user
display_grid(grid)
