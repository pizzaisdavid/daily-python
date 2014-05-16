import sys

def decompress(filename):
    KEY, compress = parse_input(filename)
    for physical_line in compress:
        translate(KEY, physical_line)

def parse_input(filename):
    KEY = ['is', 'my', 'hello', 'name', 'stan']
    compress = [['2!', '!', 'R', '1^', '3', '0', '4^', '.', 'E']]
    return KEY, compress

def translate(KEY, physical_line):
    string = ''
    for chunk in physical_line:
        if has_modifier(chunk):
            string += chunk_has_modifier(KEY, chunk)
        elif is_symbol(chunk):
            string = add_symbol(string, chunk)
        elif is_key(KEY, chunk):
            string += add_key(KEY, chunk)
        else:
            print (string)
            string = ''
            continue
        string += ' '

def has_modifier(string):
    HAS_MODIFIER = 2
    return len(string) == HAS_MODIFIER

def is_symbol(string):
    SYMBOLS = '?!;:,.'
    return string in SYMBOLS

def add_symbol(string, symbol):
    return string[:-1] + symbol

def is_key(KEY, string):
    indices = [str(x) for x in list(range(len(KEY)))]
    return string in indices

def add_key(KEY, index):
    return KEY[int(index)]

def chunk_has_modifier(KEY, command):
    CAPS_LOCK = '!'
    CAPITALISED = '^'
    index, modifier = command
    string = KEY[int(index)]
    if modifier is CAPS_LOCK:
        return string.upper()
    elif modifier is CAPITALISED:
        return string[0].upper() + string[1:]

decompress('compression.txt')

