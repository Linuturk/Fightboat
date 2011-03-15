#!/usr/bin/python

import random

# Grid Dimensions
MAX_X = 10
MAX_Y = 10

MAX_SHIPS = 5 # Number of ships for each player

def introduction():
        '''Displays an introduction to the game.'''
        print 'Welcome to Fight Boat!'
        print 'Prepare to fight!'
        return None

def random_locations(quantity):
        '''Takes an integer that determines how many locations to return.'''
        locations = {}
        cord_y = [] # Create an empty list for the y values
        while len(locations) <= quantity - 1:
                cord_x = random.choice(range(1, MAX_X + 1))
                cord_y.append(random.choice(range(1, MAX_Y + 1)))
                locations[cord_x] = cord_y
                print len(locations)
        return locations

def are_all_ships_dead(player):
	'''Pass a player's ships as a dictionary. This will check and see if the player has any ships left.'''
	if len(player) == 0: return True
	else: return False

def get_valid_input(question):
        '''Takes a string as the question being asked and makes sure the value returned is an int.'''
        try:
                guess = int(raw_input('%s:\n' % question))
                return guess
        except ValueError:
                print 'Sorry input was invalid, please provide a number'
                return get_valid_input(question)

def enter_a_shot():
        '''The player enters their guess for a shot. This function takes user input and returns values to append to a dictionary of the user's shots.'''
        x_guess = get_valid_input('Enter your x guess')
        y_guess = get_valid_input('Enter your y guess')
        
        guess = {x_guess: y_guess}
        
        print 'You guessed', guess
        yes_or_no = raw_input('Is this correct? (y or n) ').lower()
        
        if yes_or_no == 'n': return take_a_shot()
        elif x_guess > MAX_X or y_guess > MAX_Y:
                print 'Guess is outside the grid. Try again.'
                return take_a_shot()
        elif x_guess < 1 or y_guess < 1:
                print 'Guess is outside the grid. Try again.'
                return take_a_shot()
        elif yes_or_no == 'y': return guess
        else:
                print 'Invalid Entry. Try again.'
                return take_a_shot()

# Display introduction to the game.
introduction()

# Get number of human players
human_players = 0 # Let the CPU fight itself for now

# Request player names
player1 = raw_input('Enter a name for player 1: ')
player2 = raw_input('Enter a name for player 2: ')

# Setup random ship locations for both players.
player1_ships = random_locations(MAX_SHIPS)
player2_ships = random_locations(MAX_SHIPS)

# Flip a coin to see who goes first.
initiative = random.choice((player1, player2))
print initiative, 'goes first.'

# Only show ship locations if both players are CPU
if human_players == 0:
        print player1, 'ship locations:'
        print player1_ships
        print player2, 'ship locations:'
        print player2_ships

# Random shots
print random_locations(20)

print 'Game Over'
