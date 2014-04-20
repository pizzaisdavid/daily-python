def main(filename):
    def setup_variables(filename):
        content = open(filename).readlines()
        text = list(''.join(content).replace('\n', ''))
        player = text[0]
        board = text[1:]
        return player, board
    
    def occurrences(iterable, find):
        indices = []
        for i, x in enumerate(iterable):
            if x == find:
                indices.append(i)
        return indices

    def contains_two_of_three(player, current):
        temp = [['-', player, player],
                [player, '-', player],
                [player, player, '-']
                ]
        if current in temp:
            return True
        return False

    def print_board(board, winning, player):
        board[winning] = player
        for i in range(0, 9, 3):
            print ''.join(board[i: i + 3])
    
    player, board = setup_variables(filename)
    open_spots = occurrences(board, '-')
    player_spots = occurrences(board, player)
    ways_to_win = [[0,1,2], [3,4,5], [6,7,8], [0,3,6],
                   [1,4,7], [2,5,8], [0,4,8], [2,4,6]
                   ]
    winning_move = ''
    for i in ways_to_win:
        current = [board[i[0]], board[i[1]], board[i[2]]]
        if contains_two_of_three(player, current):
            winning_move = occurrences(current, '-')
    for winning in winning_move:
        print_board(board, winning, player)
main('the_winning_move_X_games.txt')
