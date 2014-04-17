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
        
    def place(order, sequence):
        indices = []
        for sequence in element:
            indices.append(order.find(i))
        return (indices, element)
            
    def label(order, sequence):
        placement = []
        for element in sequence:
            placement.append(place(order, element))
        return placement
            

    words, order = initialize_variables('d')
    if is_alphabet(order):
        print label(order, words)

gorellian_alphabet_sort('d')

    
