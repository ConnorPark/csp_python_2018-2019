from __future__ import print_function
#1-3 N/A
#4
def days():
    ''' Puts days on the end of the letter, and prints out that it is the 6,
    7,8 in september.'''
    for day in 'MTWTFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')
#5
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random

def picks():
    a = [] # make an empty list
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])]
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('picks')
#6
def roll_hundred_pair():
    '''rolls a dice 100 times and makes an histogram'''
    dice = []
    for item in range(100):
        dice.append(random.randint(2,12))
    plt.hist(dice)
    plt.savefig('hist1')
def dice(n):
    dice = []
    """Tells you the sum of n dice rolls."""
    for item in range(n):
        dice.append(random.randint(1,6))
        total = sum(dice)
    print (total)  
#7
def validate():
    guess = '' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
'''You need the guess function because if you don't have it, the program does 
not have a test value for the variable'''
#8
def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''
    This functions primary goal is to find out which person has won the
    award, by letting the player guess between 4 players. 
    '''
    winner = random.choice(players) 

    ####
    ''' This section is reveibing the guess and counting how many guesses the 
    player has'''
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: #This presents the options to type
        print(p+', ', end='')
    print(players[len(players)-1]) #This prints the options

    ####
    # This tells what happens if you guessed the winner or if you guessed wrong
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses    
#9
def go_guess(guess = random.randint(1,20)):
    '''Has a number between 1 and 20 to let the player guess the number.'''
    answer = random.randint(1,20)
    print('I have a number between 1 and 20 inclusive. ') 
    guess = int(raw_input("Enter an integer from 1 to 20: "))
    guessed = 0 
    while guess != answer:
        if guess < answer:
            print (guess," is too low")
            guessed += 1
            guess = int(raw_input("Enter an integer from 1 to 20: "))
        elif guess > answer:
            print (guess, " is too high")
            guess = int(raw_input("Enter an integer from 1 to 20: "))
            guessed += 1
        
    print ("You guessed it!")
    print ('in ', guessed, "tries!")
#10
'''You would need 5999 tries to guarantee the right answer. '''
#11a
def matches(ticket, winners):
    '''Sees how many tickets match with the winners. '''
    match = 0
    for ticket in winners:
        match += 1
    return match
#11b
def report(guess, secret):
    '''Mastermind in python'''
    right_place = 0
    wrong_place = -2
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            right_place += 1
        elif guess[i] != secret[i]:
            wrong_place +=1
    return [right_place, wrong_place]
#Conclusion
#1
'''The loops can go on forever, making it impossible to work with if you want 
the loop to end in a certain point. '''
#2
'''Iteration changes the data that you have while analysis only looks at the 
data and leaving it eactly as it is. '''
#3
'''For loops go on forever and keeps iterating data, and while loops run code to
see if it is true or not.'''
#4
'''Me and my partner both try different ways to approach this topic, which gives
us other ways to handle the problem at hand. '''
#1.3.7 Function test
days()
picks()
roll_hundred_pair()
dice(3)
guess_winner()
go_guess()
matches([11, 12, 13, 14, 15], [3, 8, 12, 13, 17])
guess = ['red','red','red','green','yellow']
secret = ['red','red','yellow','yellow','black']
print (report(guess, secret))