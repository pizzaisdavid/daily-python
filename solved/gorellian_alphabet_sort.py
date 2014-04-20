def gorellian_alphabet_sort():
    '''Sorts words given a specific ordering.'''
    def initialize_variables():
        order = 'ZYXWVuTSRQpONMLkJIHGFEDCBa'.lower()
        words = ['go', 'aLL', 'ACM', 'teamS', 'Go']
        return words, order
        
    def is_alphabet(possible_alphabet):
        '''Checks if the inputs contains all 26 letters.'''
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for letter in alphabet:
            if letter not in possible_alphabet:
                return False
        return True
            
    def group(order, sequence):
        dictionary = {}
        for element in sequence:
            key = order.find(element[0].lower())
            if key not in dictionary:
                dictionary[key] = []
            dictionary[key].append(element)
        return dictionary

    def length(x):
        '''Takes a list that has a length of two and returns shorter, longer'''
        if len(x[1]) < len(x[0]):
            return x[1], x[0]
        return x[0], x[1]

    def compare(order, words):
        if len(words) == 2:
            shorter, longer = length(words)
            for index, character in enumerate(shorter):
                shorter_index = order.find(shorter[index].lower())
                longer_index = order.find(shorter[index].lower())
                if shorter_index > longer_index:
                    return [shorter, longer]
                elif shorter_index < longer_index:
                    return [longer, shorter]
            return [shorter, longer]
        return words

    def sorting(order, sequence):
        for d, s in enumerate(sequence):
            for i, element in enumerate(sequence):
                sequence[i: i+2] = compare(order, sequence[i: i+2])
        return sequence

    def format_input(dictonary):
        for key in sorted(dictonary.keys()):
            for item in dictonary[key]:
                print item

    words, order = initialize_variables()
    if is_alphabet(order):
        groups = group(order, words)
        for key in sorted(groups.keys()):
            groups[key] = sorting(order, groups[key])
        format_input(groups)

gorellian_alphabet_sort()


#/////
#   THIS CODE WORKS
#/////

def is_alphabet(possible_alphabet):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in possible_alphabet:
            return False
    return True

def indices(order, sequence):
    temp = []
    for element in sequence:
        temp.append(order.find(element.lower()))
    return temp

order = 'ZYXWVuTSRQpONMLkJIHGFEDCBa'.lower()
words = ['go', 'aLL', 'ACM', 'teamS', 'Go']
indices_and_words = []

if is_alphabet(order):
    for word in words:
        indices_and_words.append((indices(order, word), word))
    ouput = sorted(indices_and_words, key = lambda x: x[0])
    for x in ouput:
        print x[1]


    
