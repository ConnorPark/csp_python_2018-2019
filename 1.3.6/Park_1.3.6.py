#1 N/A
#2 N/A
#3 N/A
#4
(5,7,12)
#5
'''A convention in HTML is the amount of tabs that you put between each line.'''
#6
'''a) the value that comes out is 2 because when counting in python, you start
at 0 and then progress.
b) the output is ('a', 'b') because python is showing the values of 0 and 1, 
not 2.'''
#7
'''When there is a defined variable in the equation, even if you change a, the 
Tuple will not change because it is not immunable. 
a)It would return as true because the variable is automatically changed to the 
number. 
b) It would return as 10 because tuples dont output defined variables.'''
#8
'''The values that are outputed is 'b' and 3. The stepper would start at b and 
keep going until there are no more values.'''
#9
'''The output is false because strings are different from numbers'''
#10
'''a)We get the normal list with the new values at the very end. This happens 
because you added two integers to values, which adds them to the end, not the 
front.
b)I got the normal list with the new value at the end, only the end value is a 
list inside of a list. LISTCEPTION!'''
#11
'''You cannot add integers, and you can only add lists, so this command doesn't 
work when you try it.'''
#12
'''I got 18. a was multiplied by 3 using the shorthand commands so it changed 
the variable.'''
#13 N/A
#14
import random
def roll_two_dice():
    '''"Rolls" two dice and tells you what you get'''
    return random.randint(1,6) + random.randint(1,6)
#Conclusions
#1
'''a is a word, b is a tuple, and c is a list'''
#2
'''Each variable type is used differently and have different use cases, so 
programmers can have more tool to use.'''
#3
'''There are many functions that you can use in python. In a way, the functions 
are a lot like scratch, with each line being a block from that language'''
#1.3.6 Function Test
print(roll_two_dice())