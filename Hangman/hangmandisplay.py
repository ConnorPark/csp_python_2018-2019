def hangman_display(guessed, secret):
    '''This function take in 2 arguments, a guess and the secret word. If the 
    guess is inside the secret, it will append the letter. If the secret is a 
    space, then it will append a space. If there is a letter in the guess that
    doesn't appear in the secret, it will append a dash. Everything in the 
    output will be put in order after all of the appending. Finally, it will 
    output the final product.'''
    finalword = ''
    for character in secret:
        if character in guessed:
            finalword += character
        elif ' ' == character:
            finalword += ' '
        else: 
            finalword += '-'
    return finalword
    