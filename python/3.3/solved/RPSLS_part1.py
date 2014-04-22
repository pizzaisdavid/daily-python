from random import randint

def RPSLS():
    def get_input(options):
        choice = input('Enter: ').lower()
        while choice not in options:
            choice = input(options).lower()
        return choice

    def occurrences(sequence, find):
        for index, element in enumerate(sequence):
            if element == find:
                return False, index
        return True, None
    
            # 'thing': [beats these], [death move]
    rules = {
        'rock': (['scissors', 'lizard'], ['crushes', 'crushes']),
        'paper': (['spock', 'rock'], ['disproves', 'covers']),
        'scissors': (['paper', 'lizard'], ['cuts', 'decapitates']),
        'lizard': (['spock', 'paper'], ['poisons', 'eats']),
        'spock': (['rock', 'scissors'], ['vaporizes', 'smashes'])
        }
    options = list(rules.keys())
    human = get_input(options)
    computer = options[randint(0, 4)]
    print ('player pick: ' + human)
    print ('computer pick: ' + computer)
    print (' ')
    computer_is_winner, c_index = occurrences(rules[human][0], computer)
    player_is_winner, p_index = occurrences(rules[computer][0], human)
    if human == computer:
        print ('tie')
    elif computer_is_winner:
        print (computer + ' ' + rules[computer][1][p_index] + ' ' + human + '. computer wins!')
    else:
        print (human + ' ' + rules[human][1][c_index] + ' ' + computer + '. human wins!')
    RPSLS()

RPSLS()
