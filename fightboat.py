#!/usr/bin/python

import random

DEBUG = 1 # Debug switch
PLAYER_SHIPS = 5 # Number of ships for each player
MAX_X = 9 # Grid Dimensions
MAX_Y = 9 # Grid Dimensions
MAX_SHIPS = MAX_X * MAX_Y # Maximum number of ships that can be placed on the grid
STATUS = {'hit': 1, 'miss': 2, 'ship': 3} # Possible coordinate status

def create_grid():
        '''Creates a nested list structure full of 0's.'''
        return [[0] * MAX_X for x in range(MAX_Y)]

def display_grid(grid):
        '''Takes a nested list structure as created by create_grid() as the argument. Displays the current status of the grid with appropriate labels and legend.'''
        count = MAX_Y
        for coordinate in grid:
                print count, coordinate
                count = count - 1
        xaxis_label()
        legend()
        return None

def xaxis_label():
        '''Label the xaxis of the grid.'''
        print '\n ', range(1, MAX_X + 1), '\n'
        return None

def legend():
        '''Shows the user what the symbols in the grid mean.'''
        print STATUS['hit'], '= Hit', STATUS['miss'], '= Miss', STATUS['ship'], '= Ship\n'
        return None

def insert_into_grid(grid, x, y, status):
        '''Inserts the status passed at the x and y coordinates provided into the grid provided.'''
        message = 'Inserting %s into grid at (%d, %d)' % (status, x+1, y)
        debug(message)
        grid[-y][x] = status
        return None

def random_coordinate():
        '''Returns a set of random coordinates inside the grid.'''
        x = random.choice(range(0, MAX_X))
        y = random.choice(range(1, MAX_Y + 1))
        return x, y

def random_ship_placement(grid):
        '''Places random ships on the grid.'''
        if PLAYER_SHIPS > MAX_SHIPS:
                debug('Too many ships are defined.')
        else:
                count = PLAYER_SHIPS
                while count > 0:
                        x, y = random_coordinate()
                        if grid[-y][x] == 0:
                                insert_into_grid(grid, x, y, STATUS['ship'])
                                count = count - 1
                        else:
                                message = 'Coordinate duplication for ship placement. Trying again.'
                                debug(message)
        return None

def debug(string):
        '''Pass a string to print as a debug message if debugging is activated.'''
        if DEBUG == 1:
                print 'Debug===>', string
        return None

def player_status(player):
        '''Takes a player dictionary and shows that player's status.'''
        print '=' * 80
        print player['name']
        print '=' * 80
        display_grid(player['target'])
        display_grid(player['home'])
        return None

def still_alive(grid):
        '''Searches through the grid for a ship. If no ships are found, returns False.'''
        count = 0
        for status in grid:
                count = count + status.count(STATUS['ship'])
        if count > 0: return True
        else: return False

# Introduction
print 'Welcome to Fightboat!'
print 'Prepare for carnage!'

wants_to_play = 'y'
first_run = 1

while wants_to_play == 'y':
        if first_run == 1:
                # Define empty dictionaries for each player.
                p1 = {}
                p2 = {}
                
                # Ask the player's their names, and assign their grids.
                p1['name'] = raw_input('Player 1\'s name: ')
                p1['home'] = create_grid()
                p1['target'] = create_grid()
                
                p2['name'] = raw_input('Player 2\'s name: ')
                p2['home'] = create_grid()
                p2['target'] = create_grid()
                
                # Insert random ships into their home grid.
                random_ship_placement(p1['home'])
                random_ship_placement(p2['home'])
                
                # Deactivate first run
                first_run = 0
        
        # Show each player's status
        player_status(p1)
        raw_input('Enter to continue . . . ')
        player_status(p2)
        raw_input('Enter to continue . . . ')
        
        # Still alive?
        if still_alive(p1['home']) == False:
                print p2['name'], 'Wins!'
        elif still_alive(p2['home']) == False:
                print p1['name'], 'Wins!'
        else:
                # Want to play again?
                wants_to_play = raw_input('Want to play again? (y/n) ')

