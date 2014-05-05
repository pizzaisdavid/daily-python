def longest_two_character_substring(string):
	'''Returns the longest two character substring.'''
	pairs = unique_pairs(string)
	substrings = []
	longest = ''
	for pair in pairs:
		substrings.extend(occurrences(string, pair))
	print (max(substrings, key = len))

def unique_pairs(sequence):
	'''Returns unique two character tuples in a list.'''
	return unique_combinations(get_pairs(sequence))

def get_pairs(sequence):
	'''Iterates over the sequence creating pairs.'''
	pairs = []
	for index, item in enumerate(sequence):
		try:
			pairs.append((item, sequence[index + 1]))
		except IndexError:
			pass
	return pairs

def unique_combinations(sequence):
	'''Pairs must be two unique characters. Removes duplicates, order doesn't matter.'''
	unique = []
	for pair in sequence:
		combination = sorted(set(pair))
		if len(combination) == 2 and combination not in unique:
			unique.append(combination)
	return unique

def occurrences(sequence, find):
	'''Returns a list of substrings that are made of find.'''
	substrings = ['']
	for item in sequence:
		if item in find:
			substrings[-1] += item
		else:
			substrings.append('')
	return substrings
longest_two_character_substring('abbxcccc')
