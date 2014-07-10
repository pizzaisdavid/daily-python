def compress(filename):
    lines, keywords = setup(filename)
    compressed = [convert_line(keywords, line) for line in lines]
    print_output(keywords, compressed)

def setup(filename):
    lines = [line.strip().split(' ') for line in open(filename)]
    words = [reformat(word) for line in lines for word in line]
    return lines, list(set(words))

def reformat(word):
    return remove_symbols(word.lower())

def remove_symbols(word):
    SYMBOLS = '.,?!;:'
    if word[-1] in SYMBOLS:
        return word[:-1]
    return word

def convert_line(keywords, line):
    return ''.join([convert(keywords, word) for word in line]) + 'R'

def convert(keywords, word):
    SYMBOLS = '.,?!;:'
    chunk = convert_word(keywords, word)
    last_character = word[-1]
    if word == word.capitalize():
        chunk += '^'
    elif word == word.upper():
        chunk += '!'
    if last_character in SYMBOLS:
        chunk += ' ' + last_character
    return chunk + ' '

def convert_word(keywords, word):
    return str(keywords.index(reformat(word)))

def print_output(*arguments):
    print(len(arguments[0]))
    [print_list(argument) for argument in arguments]
    print('E')

def print_list(sequence):
    [print(item) for item in sequence]

compress('compression1.txt')
