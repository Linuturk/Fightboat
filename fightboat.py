#!/usr/bin/python

import random

# Debug information switch
DEBUG = 1

# Grid Dimensions
MAX_X = 10
MAX_Y = 10

MAX_SHIPS = 5 # Number of ships for each player

def introduction():
        '''Displays an introduction to the game.'''
        print 'Welcome to Fight Boat!'
        print 'Prepare to die!'
        return None

def random_ships():
        '''Takes a tuple (x,y) where x and y are the boundry for the playing field.'''
        ships = {}
        while len(ships) <= MAX_SHIPS - 1:
                cord_x = random.choice(range(1, MAX_X + 1))
                cord_y = random.choice(range(1, MAX_Y + 1))
                ships[cord_x] = cord_y
        return ships

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

def take_a_shot():
        '''The player takes a shot. This function takes user input and returns values to append to a dictionary of the user's shots.'''
        x_guess = get_valid_input('Enter your x guess')
        y_guess = get_valid_input('Enter your y guess')

        x_guess = int(x_guess)
        y_guess = int(y_guess)
        guess = {x_guess: y_guess}

        print 'You guessed', guess
        yes_or_no = raw_input('Is this correct? (y or n) ').lower()

        if yes_or_no == 'y': return guess
        elif yes_or_no == 'n': return take_a_shot()
        else:
                print 'Invalid Entry. Try again.'
                return take_a_shot()

def coin_flip():
        '''Returns heads (True) or tails (False)'''
        flip = random.choice((True, False))
        if flip == True: return 'Heads'
        else: return 'Tails'

# Display introduction to the game.
introduction()

# Setup random ship locations for both players.
player1_ships = random_ships()
player2_ships = random_ships()

# Flip a coin to see who goes first.

# Display debugging information
if DEBUG == 1:
        print 'Player 1 Ship Locations:', player1_ships
        print 'Player 2 Ship Locations:', player2_ships
        print 'Is player 1 dead?:', are_all_ships_dead(player1_ships)
        print 'Is player 2 dead?:', are_all_ships_dead(player2_ships)
        print 'Coin Flip:', coin_flip()
        print 'Test Shot:'
        test_shot = take_a_shot()
        print test_shot

print 'Game Over'
