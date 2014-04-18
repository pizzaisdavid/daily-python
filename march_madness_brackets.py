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
        
