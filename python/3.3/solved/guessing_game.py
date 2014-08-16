import random

def game(lower=1, upper=101):
    response = ''
    count = 0
    while response != 'correct':
        guess = random.randrange(lower, upper)
        response = get_user_input(guess)
        lower, upper = set_bounds(response, lower, upper, guess)
        count += 1
    print_statistics(guess, count)

def get_user_input(guess):
    response = input('Is {0} higher, lower, or correct?'.format(guess)).lower()
    options = ['higher', 'lower', 'correct']
    while response not in options:
        response = input(options).lower()
    return response

def set_bounds(response, lower, upper, guess):
    if response == 'lower':
        return lower, guess
    return guess, upper

def print_statistics(guess, count):
    print('The number is {0}, and it took {1} trys.'.format(guess, count))

game()
