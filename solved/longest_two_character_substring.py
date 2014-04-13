def longest_two_character_substring(string):
    def occurrences(iterable, item):
        array = ['']
        for x in iterable:
            if x in item:
                array[-1] = array[-1] + x
            else:
                array.append('')
        return array
    
    list_of_strings = []
    for i, c in enumerate(string[:-1]):
        letters = string[i: i + 2]
        list_of_strings.extend(occurrences(string, letters))
    print max(list_of_strings, key = len)

# longest_two_character_substring('abbxcccc')
# longest_two_character_substring('abcabcabcabccc')
# longest_two_character_substring('qwertyytrewq')

