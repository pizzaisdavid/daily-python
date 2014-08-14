def longest_word(filename):
    words, characters = setup(filename)
    accepted = {}
    for word in words:
        if is_possible(list(word), characters):
            add(accepted, word)
    output(accepted)

def setup(filename):
    with open(filename) as file:
        return [line.strip().split(' ') for line in file]

def is_possible(word, available):
    for character in available:
        delete(word, character)
    return word == []

def delete(sequence, element):
    try:
        sequence.remove(element)
    except ValueError:
        pass
        
def add(sequence, element):
    length = len(element)
    if length not in sequence:
        sequence[length] = []
    sequence[length].append(element)

def output(dictonary):
    try:
        print(dictonary[max(dictonary.keys())])
    except ValueError:
        print('No Words Found')
    
longest_word('text.txt')
