# BUGS:
# rock ('rock', 'crushes') lizard human wins!
# paper ('paper', 'disproves') spock human wins!
# paper ('paper', 'covers') rock human wins!

from random import randint

def game():
    def introduction(options):
        print ('PICK ONE OF THE FOLLOWING:')
        for item in options:
            print (item)
        print ('TYPE EXIT TO QUIT')
        print (' ')
    
    def get_input(options, stop):
        combine = options + stop
        choice = input('Enter: ').lower()
        while choice not in combine:
            choice = input(options).lower()
        return choice

    def RPSLS(rules, human, score):
        def occurrences(sequence, find):
            for index, element in enumerate(sequence):
                if element == find:
                    return False, index
            return True, None

        human_wins, computer_wins, ties = score
        computer = options[randint(0, 4)]
        print ('player pick: ' + human)
        print ('computer pick: ' + computer)
        computer_is_winner, c_index = occurrences(rules[human][0], computer)
        player_is_winner, p_index = occurrences(rules[computer][0], human)
        if human == computer:
           print ('tie')
           return (human_wins, computer_wins, ties + 1), human
        elif computer_is_winner:
            winner = computer
            move = rules[computer][1][p_index]
            loser = human
            who = 'computer'
            computer_wins += 1
        else:
            winner = human
            move = human, rules[human][1][c_index]
            loser = computer
            who = 'human'
            human_wins += 1
        print (winner, move, loser, who, 'wins!', sep=' ')
        print (' ')
        return (human_wins, computer_wins, ties), human
        
    score = [0, 0, 0]
    rules = {
        'rock': (['scissors', 'lizard'], ['crushes', 'crushes']),
        'paper': (['spock', 'rock'], ['disproves', 'covers']),
        'scissors': (['paper', 'lizard'], ['cuts', 'decapitates']),
        'lizard': (['spock', 'paper'], ['poisons', 'eats']),
        'spock': (['rock', 'scissors'], ['vaporizes', 'smashes'])
        }
    options = list(rules.keys())
    stop = ['exit', 'stop']
    played = {'lizard': 0, 'spock': 0, 'paper': 0, 'scissors': 0, 'rock': 0}
    human = 'rock'
    introduction(options)
    while True:
        human = get_input(options, stop)
        if human in stop:
            break
        score, human = RPSLS(rules, human, score)
        played[human] += 1
    human_wins, computer_wins, ties = score
    print ('~~~~~~~~FINAL~SCORE~~~~~~~~')
    print ('TIES: ', ties)
    print ('HUMAN: ', human_wins)
    print ('COMPUTER: ', computer_wins)
    print ('~~~~~~~~FINAL~SCORE~~~~~~~~')

game()
