def longest_two_character_substring(string):
    substrings = []
    for pair in get_unique_pairs(string):
        substrings.extend(get_substrings_made_from_pair(string, pair))
    print(max(substrings, key=len))

def get_unique_pairs(sequence):
    pairs = get_character_combinations(sequence)
    return set(pairs) & set(map(reformat, pairs))

def get_character_combinations(sequence):
    LENGTH = 2
    return [sequence[i: i + LENGTH] for i, _ in enumerate(sequence)]

def reformat(string):
    return ''.join(sorted(string))

def get_substrings_made_from_pair(sequence, pair):
    SPLITTER = ', '
    strings = [is_in(SPLITTER, pair, item) for item in sequence]
    return ''.join(strings).split(SPLITTER)

def is_in(SPLITTER, check, item):
    if item in check:
        return item
    return SPLITTER

longest_two_character_substring('abbccc')
longest_two_character_substring('abcabcabcabccc')
longest_two_character_substring('qwertyytrewq')
