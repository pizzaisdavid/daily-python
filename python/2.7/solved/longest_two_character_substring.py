def longest_two_character_substring(string):
    def occurrences(sequence, find):
        array = ['']
        for element in sequence:
            if element in find:
                array[-1] += element
            else:
                array.append('')
        return array
    
    substrings = []
    for i, c in enumerate(string[:-1]):
        letters = string[i: i + 2]
        substrings.extend(occurrences(string, letters))
    print max(substrings, key = len)

longest_two_character_substring('abbxcccc')
longest_two_character_substring('abcabcabcabccc')
longest_two_character_substring('qwertyytrewq')
