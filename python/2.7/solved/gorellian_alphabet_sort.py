def gorellian_alphabet_sort():
    '''Sorts words given a specific ordering.'''
    words = ['ANTLER','ANY','COW','HILL','HOW','HOWEVER','WHATEVER','ZONE']
    order = 'UVWXYZNOPQRSTHIJKLMABCDEFG'.lower()
    if is_alphabet(order):
        groups = group(order, words)
        for key in sorted(groups):
            groups[key] = sort(order, groups[key])
        print_output(groups)

def is_alphabet(possible_alphabet):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    return sorted(possible_alphabet) == alphabet
        
def group(order, sequence):
    dictionary = {}
    for element in sequence:
        key = order.find(element[0].lower())
        if key not in dictionary:
            dictionary[key] = []
        dictionary[key].append(element)
    return dictionary

def sort(order, sequence):
    for i, _ in enumerate(sequence):
        sequence[i: i+2] = compare(order, sequence[i: i+2])
    return sequence

def compare(order, words):
    if len(words) == 2:
        for character in zip(words[0], words[1]):
            index_1 = order.find(character[0].lower())
            index_2 = order.find(character[1].lower())
            if index_1 > index_2:
                return [words[0], words[1]]
            elif index_1 < index_2:
                return [words[1], words[0]]
    return words

def print_output(dictonary):
    for key in sorted(dictonary):
        for item in dictonary[key]:
            print (item)

gorellian_alphabet_sort()
