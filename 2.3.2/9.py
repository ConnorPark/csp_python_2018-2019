def algor(numone, numtwo):
    p = numone -1
    q = numtwo -1
    newnum = p * q + 1.0
    for i in range(newnum/2):
        if(newnum%i == 0.0):
            print(i, newnum/i)
    
            
