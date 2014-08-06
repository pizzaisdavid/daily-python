def thue_morse_sequence(count):
    header()
    current = '0'
    for n in range(0, count + 1):
        current += inverse(current)
        ouput(n, current)

def header():
    print('NTH   SEQUENCE')
    print('-' * 30)

def inverse(sequence):
    return ''.join([switch(element) for element in sequence])

def switch(character):
    if int(character):
        return '0'
    return '1'

def output(n, current):
    SPACING = 3
    print(n, ' ' * SPACING, current)

thue_morse_sequence(6)
