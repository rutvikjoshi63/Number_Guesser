import random

print('Hello')
top_number = input('Type a number: ')
if top_number.isdigit():
    
    top_number = int(top_number)
    if top_number <= 0 :
        print('Please Enter number greater than 0 next time.')
        quit()
else:
    print('Please Enter number next time')
    quit()
rand = random.randrange(top_number)
#print(rand)
guess = 0
while True:
    guess += 1
    user_guess = input('Make a guess ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please Enter number')
        continue
    if user_guess == rand:
        print('You got LUCKY!!')
        break
    elif user_guess > rand:
        print('Wrong guess')
        print('You are above the guess, try lower')
    else :
        print('Wrong guess')
        print('You are below the guess, try higher')
    continue
print("Took you",guess, "many guesses")

