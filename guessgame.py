import random

# set number equal to a random integer between 1 and 20

num = random.randint(1,20)
flag = True
guess = 0

#end prevents new line at the end of the string ( no \n )
print('guess my nymber 1 - 20', end = '')


#while flag remains = True
while flag :
    guess = input()
    if not guess.isdigit(): #
        print('invalid - enter a number 1 - 20')
        break
    elif int(guess) < num :
        print('Too low, try again', end = '')
    elif int(guess) > num :
        print('Too high, try again', end = '')
    else :
        print('Correct... My number is ' + guess)
        flag = False # ends the while loop
