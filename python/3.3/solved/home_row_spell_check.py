def spellcheck(sentence):
    words = sentence.split()
    DICTIONARY = [word.strip() for word in open('words.txt')]
    SPACE = ' '
    correct_message = ''
    for word in words:
        no_format = remove_format(word)
        if is_word(DICTIONARY, no_format):
            correct_message += word
        else:
            correct_message += find_misspelled_word(DICTIONARY, no_format)
        correct_message += SPACE
    print(correct_message)

def remove_format(string):
    PUNCTUATION = '.'
    return string.replace(PUNCTUATION, '').lower() 

def find_misspelled_word(DICTIONARY, string):
    for shift in range(-2, 3):
        possible = create_possible_word(string, shift)
        if is_word(DICTIONARY, possible) and same_length(string, possible):
            return '{' + possible + '}'

def is_word(DICTIONARY, string):
    return string in DICTIONARY

def same_length(x, y):
    return len(x) == len(y)

def create_possible_word(string, shift):
    ROWS = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    possible = ''
    for character in string:
        for row in ROWS:
            try:
                index = find(row, character)
                letter = row[index - shift]
                possible += letter
            except:
                pass
    return possible

def find(sequence, locate):
    for index, element in enumerate(sequence):
        if element == locate:
            return index

spellcheck('The quick ntpem fox jumped over rgw lazy dog.')
