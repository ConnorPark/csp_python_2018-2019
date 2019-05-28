from __future__ import print_function # must be first in file 
import random
#1
def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
    
    '''
    1a: 
    The code is from line 17
    1b: 
    i:Orange causes line 15 to run
    ii:Apple and banana causes line 17 to run
    iii:Banana and potato causes lin 20 to run
    iv:everything else causes line 22 to run
    1c: the fruit command is already running so there is no need for the starchy 
    line to run anymore.
    '''
#2 N/A
def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    # Add tests so that all lines of code are visited during test
    
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False
#3
def f(n):
    """Tells you if the number is an integer even, and if its divisible by 6"""
    if int(n) == n:
        if n % 2:
            print ('The number is odd')
        else:
            if n % 3:
                print ('The number is even')
            else:
                print ('The number is a multiple by 6')
    else:
        print ('The number is not an integer')
#4
'''You can try integers, numbers that are divisible by 6, and numbers that are
    even. '''
#5
def f_test():
    '''Testing for code on #5 to see if it works, returns true is it works'''
    works = True
    if f(1) != 'The number is odd':
        works = 'something wrong'
    if f(4) != 'The number is a multiple of 6':
        works = 'something wrong'
    if f(1.4)!= 'The number is an integer':
        works = 'something wrong'
    if f(2) != 'The number is even':
        works = 'something wrong'
    if works == True:
        print ('Alright!')
        return True
    else:
        print (works)
        return False
#7
"""The difference between + as a concatenation and + as numerical addition is that
concatenation is adding string and numerical addition is adding numbers"""
#8
def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess >= secret:
        print('Too high - my number was', secret)
    if guess <= secret:
        print('Too low -  my number was', secret)
    if guess == secret:
        print('Right, my number is', guess, end='!\n')
    #a
    '''Line 11(102)print thats the user guessed the number correctly'''
    #1.3.4 Function Test
#9
def quiz_decimal (low, high):
    decimal =  random.randint 
    print ('Type a number between ', low, 'and ', high)
    guesss = int(raw_input('Guess: '))
    if guesss >= decimal:
        print ('No, ', guesss, 'is greater than', high)
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)

