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
            if index in placement.key():
                placement[index].append(element)
            else:
                palcement[index] = [element]
        return placement
            

    words, order = initialize_variables('d')
    if is_alphabet(order):
        print label(order, words)

gorellian_alphabet_sort('d')

    
