def show_winning_move(filename):
    '''Print the winning move if there is one.'''
    def initialize_variables(filename):
        '''.'''
        CONTENT = open(filename).readlines()
        TEXT = list(''.join(CONTENT).replace('\n', ''))
        player = TEXT[0]
        board = TEXT[1:]
        return player, board
        
    player, board = initialize_variables(filename)
  
  
  
show_winning_move('the_winning_move_x_games_edition.txt')
