def march_madness_bracket(string):

    def occurrences(string, substring):
        indices = []
        for index, character in enumerate(string):
            if character in substring:
                indices.append(index)
        return indices

    def closest_closing_bracket(string):
        return min(occurrences(string, '}])'))

    def opening_bracket_left_of_closing(string, closing):
        open_bracket = occurrences(string, '{([')
        for index in sorted(open_bracket, reverse=True):
            if closing > index:
                return index

    def error(s, opening, closing):
        if s[opening] + s[closing] in '(){}[]':
            return False
        return True
        
    closing = closest_closing_bracket(string)
    opening = opening_bracket_left_of_closing(string, closing)
    if error(string, opening, closing):
        print 'ERROR!'
        break

decode('(2{[0]1})')
        
def occurrences(string, brackets):
  array = []
  for symbol in brackets:
    array += [i for i, x in enumerate(string) if x == symbol]
  return array

def opening(string, last):
  for n in reversed(sorted(occurrences(string, '([{'))):
    if n < last:
      return n

def closing(string):
  return min(occurrences(string, ')]}'))

def trim(s, n1, n2):
  return s[n1 + 1: n2].strip() + ' '

def cut(s, n1, n2):
  return s[:n1] + s[n2 + 1:]

def solve(string):
  phrase = ''
  while len(string):
    last = closing(string)
    first = opening(string, last)
    phrase += trim(string, first, last)
    string = cut(string, first, last)
  print phrase.replace('  ', ' ')

solve('{years [four score] ago (and seven) our fathers}')
solve('[racket for {brackets (matching) is a} computers]')
