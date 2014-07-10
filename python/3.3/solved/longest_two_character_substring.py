def longest_two_character_substring(string):
    substrings = []
    for pair in get_unique_pairs(string):
        substrings.extend(get_substrings_made_up_of_a_group(string, pair))
    print(max(substrings, key=len))

def get_unique_pairs(sequence):
    pairs = get_n_length_character_combinations(sequence, length=2)
    return set(pairs) & set(map(reformat, pairs))

def get_n_length_character_combinations(sequence, length):
    return [sequence[i: i + length] for i, _ in enumerate(sequence)]

def reformat(string):
    return ''.join(sorted(string))

def get_substrings_made_up_of_a_group(string, group):
    SPLITTER = ', '
    substrings = [is_in(SPLITTER, group, character) for character in string]
    return ''.join(substrings).split(SPLITTER)

def is_in(SPLITTER, check, character):
    if character in check:
        return character
    return SPLITTER

longest_two_character_substring('abbccc')
longest_two_character_substring('abcabcabcabccc')
longest_two_character_substring('qwertyytrewq')
