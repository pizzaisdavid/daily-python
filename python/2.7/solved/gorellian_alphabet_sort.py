def gorellian_alphabet_sort():
    '''Sorts words given a specific ordering.'''
    def is_alphabet(possible_alphabet):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        possible_alphabet = ''.join(sorted(possible_alphabet))
        if possible_alphabet == alphabet:
            return True
        return False
            
    def group(order, sequence):
        dictionary = {}
        for element in sequence:
            key = order.find(element[0].lower())
            if key not in dictionary:
                dictionary[key] = []
            dictionary[key].append(element)
        return dictionary

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

    def sort(order, sequence):
        for i, element in enumerate(sequence):
            sequence[i: i+2] = compare(order, sequence[i: i+2])
        return sequence

    def format_input(dictonary):
        for key in sorted(dictonary):
            for item in dictonary[key]:
                print item

    words = ['ANTLER','ANY','COW','HILL','HOW','HOWEVER','WHATEVER','ZONE']
    order = 'UVWXYZNOPQRSTHIJKLMABCDEFG'.lower()
    if is_alphabet(order):
        groups = group(order, words)
        for key in sorted(groups):
            groups[key] = sort(order, groups[key])
        format_input(groups)

gorellian_alphabet_sort()
