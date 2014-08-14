def longest_word(filename):
    words, characters = setup(filename)
    valid = []
    for word in words:
        if is_possible(list(word), characters):
            valid.append(word)
    output(valid)

def setup(filename):
    with open(filename) as file:
        return [line.strip().split(' ') for line in file]

def is_possible(word, available):
    for character in available:
        delete(word, character)
    return word == []

def delete(sequence, item):
    try:
        sequence.remove(item)
    except ValueError:
        pass

def output(sequence):
    try:
        length = len(max(sequence, key=len))
        print([item for item in sequence if length == len(item)])
    except ValueError:
        print('No Words Found')
    
longest_word('text.txt')
