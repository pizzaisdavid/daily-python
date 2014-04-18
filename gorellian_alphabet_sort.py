def gorellian_alphabet_sort(filename):
    '''.'''
    def initialize_variables(filename):
        order = 'ZYXWVuTSRQpONMLkJIHGFEDCBa'.lower()
        words = ['go', 'aLL', 'ACM', 'teamS', 'Go']
        return words, order
        
    def is_alphabet(possible_alphabet):
        '''.'''
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
        print sequence
        if len(sequence) == 2:
            longer = max(sequence, key=len)
            if len(longer) == len(sequence[0]):
                return sequence[1], sequence[0]
            return sequence[0], sequence[1]
        elif len(sequence) == 1:
            return sequence[0]

    def compare(order, words):
        shorter, longer = length(words)
        for index in range(len(shorter)):
            shorter_index = order.find(shorter[index].lower())
            longer_index = order.find(shorter[index].lower())
            if shorter_index < longer_index:
                return [shorter, longer]
            elif shorter_index > longer_index:
                return [longer, shorter]
        return [shorter, longer]

    def sorting(order, sequence):
        sort = []
        while len(sequence) > 1:
            for index in reversed(range(len(sequence))):
                compare(order, sequence[index-2: index])
            sort.append(sequence[0])
            del sequence[0]
        return sort
            
            
        
    words, order = initialize_variables('d')
    if is_alphabet(order):
        groups = label(order, words)
        for key in sorted(groups.keys()):
            groups[key] = sorting(order, groups[key])
        print groups

gorellian_alphabet_sort('d')

    
