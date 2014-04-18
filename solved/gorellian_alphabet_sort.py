def gorellian_alphabet_sort(filename):
    def initialize_variables(filename):
        order = 'ZYXWVuTSRQpONMLkJIHGFEDCBa'.lower()
        words = ['go', 'aLL', 'ACM', 'teamS', 'Go']
        return words, order
        
    def is_alphabet(possible_alphabet):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for letter in alphabet:
            if letter not in possible_alphabet:
                return False
        return True
            
    def label(order, sequence):
        placement = {}
        for element in sequence:
            index = order.find(element[0].lower())
            if index in placement.keys():
                placement[index].append(element)
            else:
                placement[index] = [element]
        return placement

    def length(sequence):
        longer = max(sequence, key=len)
        if len(longer) == len(sequence[0]):
            return sequence[1], sequence[0]
        return sequence[0], sequence[1]

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

    words, order = initialize_variables('d')
    if is_alphabet(order):
        groups = label(order, words)
        for key in sorted(groups.keys()):
            groups[key] = sorting(order, groups[key])
        format_input(groups)

gorellian_alphabet_sort('d')

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


    
