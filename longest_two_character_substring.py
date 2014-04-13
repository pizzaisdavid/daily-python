def longest_two_character_substring(string):
    '''.'''
    def longest(iterable):
        longest = ''
        for item in iterable:
            if len(longest) < len(item):
                longest = item
        return longest
        
    def occurrences(iterable, item):
        '''Return all occurrences of item in iterable as a list.'''
        # return [i for i, x in enumerate(iterable) if x == item]
        array = ['']
        for x in iterable:
            if x in item:
                array[:-1] = array[:-1] + x
            else:
                array.append('')
        return array
    
    list_of_strings = []
    for i, character in enumerate(string[:-1]):
        letters = string[i: i + 1]
        list_of_strings = occurrences(string, letters)
        
