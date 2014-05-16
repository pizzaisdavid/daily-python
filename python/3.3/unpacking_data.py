def decompress(filename):
    key, compress = parse_input(filename)
    for physical_line in compress:
        translate(key, physical_line)

def parse_input(filename):
    key = ['is', 'my', 'hello', 'name', 'stan']
    compress = [['2!', '!', 'R', '1^', '3', '0', '4^', '.', 'E']]
    return key, compress

def translate(key, physical_line):
    SYMBOLS = '?!;:,.'
    indices = map(str, range(len(key)))
    phrase = ''
    for chunk in physical_line:
        if len(chunk) == 2:
            phrase += chunk_has_modifier(key, chunk)
        elif chunk in indices:
            phrase += key[int(chunk)]
        elif chunk in SYMBOLS:
            phrase = phrase[:-1] + chunk
        else:
            print phrase
            phrase = ''
            continue
        phrase += ' '

def chunk_has_modifier(key, command):
    UPPERCASE = '!'
    CAPITALISED = '^'
    index, modifier = command
    string = key[int(index)]
    if modifier is UPPERCASE:
        return string.upper()
    elif modifier is CAPITALISED:
        return string[0].upper() + string[1:]

decompress('compression.txt')
