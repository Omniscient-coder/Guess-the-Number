import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess !=random_number:
        guess = int(input(f"Guess a number between 1 and {x}. "))
        if guess < random_number:
            val = f"Sorry The guess {guess} is too small"
            print(val)
        elif guess> random_number:
            val = f"Sorry The guess {guess} is too big"
            print(val)

    print("Yay! you guessed correctly")


def computer_guess(y):
    low = 1
    high = y 
    feedback = ""

    while feedback != "c" :
        
        if low != high:
            guess = random.randint(low,high)
        else :
            guess = low
        feedback = input(f"Is the guess {guess} correct(c), too high(h) or too low(l)?? : ").lower()        
        if feedback =="h":
            high = guess - 1      
        elif feedback == "l":
            low = guess + 1
    
    print(f"Yay! the computer gussed your number. ")

    
user = input("Welcome! How would you like to play?\n1. You guess the number.\n2. The computer guesses the number.")
if user == "1":
    return guess()                       #enter the end point of the number you want to guess
elif user == "2":
    return computer_guess()              #enter the end point of the number computer want to guess
        

        


