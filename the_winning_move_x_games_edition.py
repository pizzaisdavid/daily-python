def show_winning_move(filename):
    '''.'''
    def initilaize_variables(filename):
        '''.'''
        content = open(filename).readlines()
        text = list(''.join(content).replace('\n', ''))
        player = text[0]
        board = text[1:]
        return player, board
  
  
  
show_winning_move('the_winning_move_x_games_edition.txt')
