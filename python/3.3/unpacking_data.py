def decompress(filename):
    KEYWORDS, compress = parse_input(filename)
    for physical_line in compress:
        translate(KEYWORDS, physical_line)

def parse_input(filename):
    KEYWORDS = ['is', 'my', 'hello', 'name', 'stan']
    compress = [['2!', '!', 'R', '1^', '3', '0', '4^', '.', 'E']]
    return KEYWORDS, compress

def translate(KEYWORDS, physical_line):
    string = ''
    for chunk in physical_line:
        string = convert(KEYWORDS, chunk, string)
        if is_linebreak(chunk):
            print (string)
            string = ''

def convert(KEYWORDS, chunk, string):
    if has_modifier(chunk):
        string += chunk_has_modifier(KEYWORDS, chunk)
    elif is_keyword(chunk):
        string += add_keyword(KEYWORDS, chunk)
    elif is_symbol(chunk):
        string = add_symbol(string, chunk)
    return string + ' '

def has_modifier(possibly_contains_modifier):
    HAS_MODIFIER = 2
    return len(possibly_contains_modifier) is HAS_MODIFIER

def chunk_has_modifier(KEYWORDS, command):
    CAPS_LOCK, CAPITALISED = '!', '^'
    index, modifier = command
    string = add_keyword(KEYWORDS, index)
    if modifier is CAPS_LOCK:
        return string.upper()
    elif modifier is CAPITALISED:
        return string[0].upper() + string[1:]

def is_symbol(possible_symbol):
    SYMBOLS = '?!;:,.'
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

