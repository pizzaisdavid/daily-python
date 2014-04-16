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
        
    def label(order, words):
        placement = {}
        for word in words:
            index = order.find(word[0].lower())
            if index not in placement.keys():
                placement[index] = [word]
            else:
                placement[index].append(word)
        return placement

    words, order = initialize_variables('d')
    if is_alphabet(order):
        print sorted(label(order, words).keys())

gorellian_alphabet_sort('d')
