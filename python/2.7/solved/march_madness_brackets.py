def solve(string):
    phrase = ''
    if error(string):
        print 'error'
    else:
        while string:
            last = first_closing_bracket(string)
            first = opening_bracket_left_of_closing(string, last)
            phrase += trim(string, first, last)
            string = cut(string, first, last)
        print phrase.replace('  ', ' ')

def error(string):
    last = first_closing_bracket(string)
    first = opening_bracket_left_of_closing(string, last)
    return string[first] + string[last] not in '(){}[]'

def first_closing_bracket(string):
    return min(occurrences(string, brackets='}])'))

def occurrences(string, brackets):
    indices = []
    for symbol in brackets:
        indices += [i for i, x in enumerate(string) if x == symbol]
    return indices

def opening_bracket_left_of_closing(string, closing):
    open_bracket = occurrences(string, brackets='{([')
    for index in sorted(open_bracket, reverse=True):
        if closing > index:
            return index

def trim(string, start, end):
  return string[start + 1: end].strip() + ' '

def cut(string, start, end):
  return string[:start] + string[end + 1:]

solve('{years [four score] ago (and seven) our fathers}')
solve('[racket for {brackets (matching) is a} computers]')
