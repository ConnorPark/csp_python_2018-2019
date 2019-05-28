import random
import time
def start_of_game():
    '''
    This function covers everything but the mechanics. Its sole purpose is to 
    tell the reader who created the game, and to wish them luck on their 
    journey
    '''
    print ('Welcome to the sequel of the dating sim by Connor and Ryan!')
    time.sleep(0.5)
    print ('We hope you have a good time guessing the words!')
    actual_game()
def actual_game():
    '''Sets the game. The name function stores the name of the player so they can
    see their name in the game. The function also asks if you want to play with a 
    girl or a boy. If they chose girl, they will get vocab that We chose 
    specifically for girls on the next function. If the player choses boy, they 
    will get boy words that we chose for boy words. '''
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
    secret = "testing"
    finalword = ""
    guesses = 10
    while guesses > 0:
        fail = 0
        for character in secret:
            if character in finalword:
                print finalword
            elif ' ' == character:
                print ' '
            else: 
                print '-'
                fail += 1
        print finalword
        print ('You have ' + str(guesses) + " guesses left")
        if fail == 0:
            print ('You won! Congrats!')
            winrestart = raw_input ('Do you want to play again:')
            if winrestart in ["yes", "Yes"]:
                start_of_game()
            else:
                break
        guessed = raw_input('Type a character')
        finalword += guessed
        if guessed not in secret:
            guesses -= 1
        if guesses == 0:
            print ('You lost! The answer was:' + secret + '!')
            loserestart = raw_input ('Do you want to play again:')
            if loserestart in ['yes',"Yes"]:
                start_of_game()
            elif loserestart in ['No', 'no']:
                break
            else:
                break
def guyhangman():
    ''''''

start_of_game()