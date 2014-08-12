import random

def bogo(scrambled, match):
    scrambled = list(scrambled)
    MATCH = list(match)
    count = 0
    while scrambled != MATCH:
        random.shuffle(scrambled)
        count += 1
    print('ITERATIONS: {0}'.format(count))

bogo('lolhe', 'hello')
