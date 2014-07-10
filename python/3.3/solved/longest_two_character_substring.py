def longest_two_character_substring(string):
    substrings = []
    for pair in get_unique_combinations(string):
        substrings.extend(get_substrings_of_consecutive_letters(string, pair))
    print(max(substrings, key=len))

def get_unique_combinations(sequence):
    combinations = get_n_length_character_combinations(sequence)
    return set(combinations) & set(map(reformat, combinations))

def get_n_length_character_combinations(sequence, length=2):
    return [sequence[i: i + length] for i, _ in enumerate(sequence)]

def reformat(string):
    return ''.join(sorted(string))

def get_substrings_of_consecutive_letters(string, group):
    SPLIT = ', '
    substrings = [letter if letter in group else SPLIT for letter in string]
    return ''.join(substrings).split(SPLIT)

longest_two_character_substring('abbccc')
longest_two_character_substring('abcabcabcabccc')
longest_two_character_substring('qwertyytrewq')
