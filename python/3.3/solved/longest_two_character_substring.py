def longest_two_character_substring(string):
	pairs = unique_pairs(string)
	substrings = []
	longest = ''
	for pair in pairs:
		substrings.extend(occurrences(string, pair))
	print (max(substrings, key = len))

def unique_pairs(sequence):
	return unique_combinations(get_pairs(sequence))

def get_pairs(sequence):
	pairs = []
	for index, item in enumerate(sequence):
		try:
			pairs.append((item, sequence[index + 1]))
		except IndexError:
			pass
	return pairs

def unique_combinations(sequence):
	unique = []
	for pair in sequence:
		combination = sorted(set(pair))
		if len(combination) == 2 and combination not in unique:
			unique.append(combination)
	return unique

def occurrences(sequence, find):
	substrings = []
	substring = ''
	for item in sequence:
		if item in find:
			substring += item
		else:
			substrings.append(substring)
			substring = ''
	substrings.append(substring)
	return substrings

longest_two_character_substring('abbxcccc')
