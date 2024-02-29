# import random

# is_playing = True

# while is_playing :

#     print(random.randint(1, 10))
#     response = input("\nWhat is your name? ")

#     if response.lower() == "quit":
#         is_playing = False
    
#     else:
#         print(f"Hello {response}!")

# print("Have a nice day!")

"""
    Requirements:
        - User enters their guess
        - User is told if their guess is too high or too low
            - continue guessing
        - User is told if they guessed correctly
            - print total number of guesses
            - end game
            - Thank the user for playing
"""

import random

is_playing = True
guess_count = 0
random_number = random.randint(1,9)

while is_playing:
    response = input('Make a guess: ')
    guess_count += 1
    if response == random_number:
        print(f'You got it in {guess_count} guess(es)')
        is_playing = False
    