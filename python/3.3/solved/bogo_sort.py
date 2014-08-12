import random

def bogo(scrambled, match):
    scrambled, MATCH = reformat(scrambled), reformat(match)
    count = 0
    while scrambled != MATCH:
        random.shuffle(scrambled)
        count += 1
    print('ITERATIONS: ', count)

def reformat(string):
    return list(string.lower())

bogo('lolhe', 'hello')

