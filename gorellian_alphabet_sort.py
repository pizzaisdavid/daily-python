def initialize_variables(filename):
    CONTENT = open(filename).readlines()
    TEXT = list(''.join(CONTENT).replace('\n', ''))
    word_count = TEXT[0]
    board = TEXT[1:]
    return player, board

def contains(iterable, required):
    for x in required:
        if x not in iterable:
            return False
    return True
