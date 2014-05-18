def compress(filename):
    lines = [line.strip() for line in open(filename).readlines()]
    keywords = add_keywords(lines)
    compressed = []
    for physical_line in lines:
        compressed.append(translate_line(keywords, physical_line))
    print_output(keywords, compressed)

def add_keywords(lines):
    keywords = []
    for physical_line in lines:
        words = physical_line.split(' ')
        for word in words:
            word = remove_symbols_and_capitalization(word)
            if word not in keywords:
                keywords.append(word.lower())
    return keywords

def remove_symbols_and_capitalization(word):
    return remove_symbols(remove_capitalization(word))

def remove_symbols(word):
    SYMBOLS = '.,?!;:'
    last_character = word[-1]
    if last_character in SYMBOLS:
        return word[:-1]
    return word

def remove_capitalization(word):
    return word.lower()

def translate_line(keywords, physical_line):
    chunks = ''
    for keyword in physical_line.split(' '):
        chunks += keyword_to_chunk(keywords, keyword)
    return chunks + 'R'

def keyword_to_chunk(keywords, keyword):
    SYMBOLS = '.,?!;:'
    chunk = convert_to_chunk(keywords, keyword)
    last_character = keyword[-1]
    if keyword == keyword.capitalize():
        chunk += '^'
    elif keyword == keyword.upper():
        chunk += '!'
    if last_character in SYMBOLS:
        chunk += ' ' + last_character
    return chunk + ' '


def convert_to_chunk(keywords, keyword):
    keyword = remove_symbols_and_capitalization(keyword)
    for index, word in enumerate(keywords):
        if word == keyword:
            return str(index)

def print_output(keywords, compressed):
    print(len(keywords))
    print_loop(keywords)
    print_loop(compressed)
    print('E')


def print_loop(sequence):
    for item in sequence:
        print(item)

compress('compression1.txt')
