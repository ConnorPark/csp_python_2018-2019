#1 N/A
#2 N/A
#3 N/A
#4 N/A
#5
"""int can type out the number six million"""
#6
'''The second command give an error message because one is a string and the 
other is an integer. The first command works because the quotes are consistant
with each string'''
#7
"""When you are counting from the start, the first letter is considered as a 0
while when you are counting backwards (using an negative), the first letter is 
not 0 but it is actually 1"""
#8
'''I put down slogan[17:]'''
#9 N/A
#10 
'''The first input is showing how the len function works. If you put a variable 
inside the len function, you get the amount of letters in the variable. The 
second input shows how there is no difference when using len and not using it 
concatenation.'''
#11
"""Boolean will come out as true if the characters are in the variable or string
it will return as false if its not there."""
#12
def how_eligible(essay):
    """Tells you if the essay is eligible for the contest"""
    points=0
    if '?' in essay:
        points += 1
    if '"' in essay:
        points += 1
    if ',' in essay:
        points += 1
    if '!' in essay:
        points += 1
    print points

#1.3.5 Function Test
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))
'''I got 4 and 1. I think I did this asignment correctly, because it did what it
was supposed to do.'''