def initialize_variables(filename):
    CONTENT = open(filename).readlines()
    TEXT = list(''.join(CONTENT).replace('\n', ''))
    player = TEXT[0]
    board = TEXT[1:]
    return player, board
