import random
import time
already_chosen = False
def start_of_game():
    ''''''
    print ('Welcome to the sequel of the dating sim by Connor and Ryan!')
    time.sleep(0.5)
    print ('We hope you have a good time guessing the words!')
    actual_game()
def actual_game():
    ''''''
    name = raw_input('Please type your name:')
    print ('Hi ' + name + '! Nice to meet you!')
    gender = raw_input('Do you want to play with a girl or a boy?')
    if gender in ['boy', 'Boy']:
        print ('Hi ' + name + '!My name is Jeremy!')
        guyhangman()
    elif gender in ["girl", 'Girl']:
        print ('Sup')
        girlhangman()
    else:
        print ('Please type a valid answer')
    actual_game()
def girlhangman():
    ''''''
    gi
def guyhangman():
    ''''''

