def longest_two_character_substring(string):
    substrings = []
    for i, c in enumerate(string[:-1]):
        letters = string[i: i + 2]
        substrings.extend(occurrences(string, letters))
    print max(substrings, key = len)
    
def occurrences(sequence, find):substrings = ['']
	for item in sequence:
		if item in find:
			substrings[-1] += item
		else:
			substrings.append('')
	return substrings
	
longest_two_character_substring('abbxcccc')
longest_two_character_substring('abcabcabcabccc')
longest_two_character_substring('qwertyytrewq')
