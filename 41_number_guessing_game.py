import random



def guessing_game():
    guess_true=True
    while guess_true:
        random_number=random.randint(0,100)
        guess_input=int(input('Enter your guessing number >> '))
        if guess_input >= 0 and guess_input <= 101:
            if guess_input == 101:
                is_exit=input('Are you sure exit to game? : Only Yes or No >> ')
                if is_exit.lower() == 'Yes'.lower():
                    guess_true=False
                    print('Thanks for using our progam !')
                elif is_exit.lower() == 'No'.lower():
                    guess_true=True
                else:
                    print('Please insert only yes or no !')
            elif guess_input < random_number:
                print('Your number is too low !')
            elif guess_input > random_number:
                print('Your number is too high !')
            elif guess_input == random_number:
                print('Answer is Correct and you won the game !')
                is_try_again=input('Try again ? : Only Yes or No >> ')
                if is_try_again.lower() == 'Yes'.lower():
                    guess_true=True
                elif is_try_again.lower() == 'No'.lower():
                    guess_true=False
                    print('Thanks for using our progam !')
                else:
                    print('Please insert only yes or no !')
            
        else:
            print('Your number must be between 0 to 100 !')


guessing_game()