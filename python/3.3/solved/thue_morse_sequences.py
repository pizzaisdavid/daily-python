def thue_morse_sequence(count):
    header()
    current = ['0']
    for n in range(0, count + 1):
        current.extend(invert(current))
        ouput(n, current)

def header():
    print('NTH   SEQUENCE')
    print('-' * 30)

def inverse(sequence):
    return [switch(element) for element in sequence]

def switch(character):
    return '0' if int(character) else '1'

def output(n, current):
    SPACING = 3
    print(n, ' ' * SPACING, ''.join(current))

thue_morse_sequence(6)
