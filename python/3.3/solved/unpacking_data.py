def decompress(filename):
    KEYWORDS, compress = parse_input(filename)
    for physical_line in compress:
        translate_line(KEYWORDS, physical_line)

def parse_input(filename):
    lines = map(lambda x: x.strip(), open(filename).readlines())
    INDEX_KEYWORDS_END = int(lines[0]) + 1
    KEYWORDS = lines[1: INDEX_KEYWORDS_END]
    compress = format_compress(lines[INDEX_KEYWORDS_END:])
    return KEYWORDS, compress

def format_compress(lines):
    return map(lambda x: x.split(' '), lines)

def translate_line(KEYWORDS, physical_line):
    string = ''
    for chunk in physical_line:
        string = chunk_to_keyword(KEYWORDS, chunk, string)

def chunk_to_keyword(KEYWORDS, chunk, string):
    if has_modifier(chunk):
        string += add_keyword_with_modifier(KEYWORDS, chunk)
    elif is_keyword(chunk):
        string += add_keyword(KEYWORDS, chunk)
    elif is_symbol(chunk):
        string = add_symbol(string, chunk)
    elif is_linebreak(chunk):
        print (string.replace('- ', '-'))
        return ''
    return string + ' '

def has_modifier(possibly_contains_modifier):
    MODIFIER = ['!', '^']
    for character in possibly_contains_modifier:
        if character in MODIFIER:
            return True
    return False

def add_keyword_with_modifier(KEYWORDS, command):
    CAPS_LOCK, CAPITALISED = '!', '^'
    index, modifier = unpack(command)
    string = add_keyword(KEYWORDS, index)
    if modifier is CAPS_LOCK:
        return string.upper()
    elif modifier is CAPITALISED:
        return string[0].upper() + string[1:]
    else:
        return ''

def unpack(command):
    MODIFIER = ['!', '^']
    for index, character in enumerate(command):
        if character in MODIFIER:
            return int(command[:index]), command[index]

def is_symbol(possible_symbol):
    SYMBOLS = '?!;:,.-'
    return possible_symbol in SYMBOLS

def add_symbol(string, symbol):
    return string[:-1] + symbol

def is_keyword(possible_keyword):
    try:
        int(possible_keyword)
        return True
    except ValueError:
        return False

def add_keyword(KEYWORDS, index):
    return KEYWORDS[int(index)]

def is_linebreak(possible_linebreak):
    LINEBREAK = 'ER'
    return possible_linebreak in LINEBREAK

decompress('compression.txt')

