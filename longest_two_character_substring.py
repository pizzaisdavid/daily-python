def longest_two_character_substring(string):
    '''.'''
    def longest_string(iterable):
        longest = ''
        for string in iterable:
            if len(longest) < len(string):
                longest = string
        return longest
    
    length = 0
    longest_of = []
    for i, character in enumerate(string[1:]):
        temp = ''
        letter_1 = string[i]
        letter_2 = string[i + 1]
        for c in string:
            if letter_1 == c or letter_2 == c:
                temp = temp + c
            else:
                temp = temp + ' '
        temp = temp.strip().split(' ')
        longest_of.append(longest_string(temp))
    print longest_string(longest_of)
