def show_winning_move(filename):
    '''If there is a winning move, find and print it.'''
    def initialize_variables(filename):
        '''.'''
        content = open(filename).readlines()
        text = list(''.join(content).replace('\n', ''))
        player = text[0]
        board = text[1:]
        return player, board
        
    player, board = initialize_variables(filename)
  
  
  
show_winning_move('the_winning_move_x_games_edition.txt')
