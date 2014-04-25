from random import randint

def game():
    def introduction(options):
        print ('WELCOME TO ROCK, PAPER, SCISSORS, SPOCK, LIZARD')
        print ('Which AI would you like to play against? [random/learning/counter]')
        AI_TYPE = get_input(['random', 'learning', 'counter'])
        print ('PICK ONE OF THE FOLLOWING:')
        for item in options:
            print (item)
        print ('TYPE EXIT TO QUIT')
        print (' ')
        return AI_TYPE
    
    def get_input(options, stop=['']):
        combine = options + stop
        choice = input('Enter: ').lower()
        while choice not in combine:
            choice = input(options).lower()
        return choice
    
    def AI(rules, played, tied, AI_TYPE):
    
        def highest(dictonary):
            return max(dictonary, key=lambda x: x[0])
        
        def random(options):
            return options[randint(0, 4)]

        def learning(rules, played, tied):
            random = randint(0, 1)
            if tied[0]:
                return rules[tied[1]][2][random]
            most_played = highest(played)
            return rules[most_played][2][random]

        def counter(rules, played, tied):
            counter_counters = {'rock': 'lizard',
                                'paper': 'rock',
                                'scissors': 'paper',
                                'spock': 'scissors',
                                'lizard': 'spock',
                                }
            if tied[0]:
                return tied[1]
            return counter_counters[highest(played)]
        
        options = list(rules.keys())
        if AI_TYPE == 'random':
            return random(options)
        elif AI_TYPE == 'learning':
            return learning(rules, played, tied)
        return counter(rules, played, tied)

    def RPSLS(rules, human, score, tied, AI_TYPE):
        
        def occurrences(sequence, find):
            for index, element in enumerate(sequence):
                if element == find:
                    return False, index
            return True, None

        human_wins, computer_wins, ties = score
        computer = AI(rules, played, tied, AI_TYPE)
        print ('player pick: ' + human)
        print ('computer pick: ' + computer)
        computer_is_winner, c_index = occurrences(rules[human][0], computer)
        player_is_winner, p_index = occurrences(rules[computer][0], human)
        if human == computer:
           print ('tie')
           return (human_wins, computer_wins, ties + 1), human, (True, human)
        elif computer_is_winner:
            winner = computer
            move = rules[computer][1][p_index]
            loser = human
            who = 'computer'
            computer_wins += 1
        else:
            winner = human
            move = rules[human][1][c_index]
            loser = computer
            who = 'human'
            human_wins += 1
        print (winner, move, loser, who, 'wins!', sep=' ')
        print (' ')
        return (human_wins, computer_wins, ties), human, (False, '')

    def percentage(numerator, denominator):
        decimal_place = 2
        percent = numerator / denominator * 100
        return str(round(percent, decimal_place)) + '%'
        
    score = [0, 0, 0]
    rules = {
        # 'option': (['things it beats'], ['moves'], ['it loses to'])
        'rock': (['scissors', 'lizard'], ['crushes', 'crushes'], ['paper', 'spock']),
        'paper': (['spock', 'rock'], ['disproves', 'covers'], ['scissors', 'lizard']),
        'scissors': (['paper', 'lizard'], ['cuts', 'decapitates'], ['rock', 'spock']),
        'spock': (['rock', 'scissors'], ['vaporizes', 'smashes'], ['paper', 'lizard']),
        'lizard': (['spock', 'paper'], ['poisons', 'eats'], ['rock', 'scissors'])
        }
    options = list(rules.keys())
    stop = ['exit', 'stop']
    played = {'lizard': 0, 'spock': 0, 'paper': 0, 'scissors': 0, 'rock': 0}
    human = 'rock'
    tied = (False, '')
    AI_TYPE = introduction(options)
    while True:
    #for i in range(10000):
        human = AI(rules, played, tied, 'counter')
        if human in stop:
            break
        score, human, tied = RPSLS(rules, human, score, tied, AI_TYPE)
        played[human] += 1
    human_wins, computer_wins, ties = score
    total = sum(score)
    print ('~~~~~~~~FINAL~SCORE~~~~~~~~')
    print ('TIES:', ties, percentage(ties, total), sep=' ')
    print ('HUMAN:', human_wins, percentage(human_wins, total), sep=' ')
    print ('COMPUTER:', computer_wins, percentage(computer_wins, total), sep=' ')
    print ('~~~~~~~~FINAL~SCORE~~~~~~~~')

game()
