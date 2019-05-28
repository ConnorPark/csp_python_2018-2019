from __future__ import print_function # use Python 3.0 printing 

def age_limit_output(age):
    '''Step 9a if-else example'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT)
    #%logstart -ort 1.3.3/logs/Park_1.3.3.#.log
def report_grade(percent):
    """Tells if the grade is good or bad"""
    if percent < 80:
        print('A grade of ', percent, ' percent does not incicate mastery ',
        'Seek extra practice or help')
    else:
        print('A grade of ', percent, ' indicates mastery. '
        'Keep up the great work!')
def vowel(letter):
    """Looks if aeiouAEIOU is inputed"""
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return False
    else:
        return True
# should check len(letter)==1
def letter_in_word(guess, word):
    '''guesses like a hangman game'''
    if guess in word:
        return True
    else:
        return False
def hint(color, secret):
    if color in secret:
        """Color guessing game"""
        print('The color' , color, 'IS in the secret sequence of colors')
    else:
        print('The color', color, 'IS NOT in the secret sequence of colors')
        

#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)
