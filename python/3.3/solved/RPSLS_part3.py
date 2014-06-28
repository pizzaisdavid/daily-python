from random import randint

def main():
    score = Score()
    options = ['lizard', 'spock', 'paper', 'scissors', 'rock']
    TYPE = introduction(options)
    game(TYPE, options, score)
    score.board(TYPE)
    
def introduction(options):
    print ('WELCOME TO ROCK, PAPER, SCISSORS, SPOCK, LIZARD')
    print ('Which AI would you like to play against? [random/learning/counter]')
    TYPE = get_input(['random', 'learning', 'counter'])
    print ('PICK ONE OF THE FOLLOWING:')
    for item in options:
        print (item)
    print ('TYPE EXIT TO QUIT')
    print (' ')
    return TYPE

def get_input(options, STOP=[]):
    choice = input('Enter: ').lower()
    while choice not in options + STOP:
        choice = input(options).lower()
    return choice

def game(TYPE, options, score):
    rules = {
        # 'option': (['things it beats'], ['attack'], ['it loses to'])
        'rock': (['scissors', 'lizard'], ['crushes', 'crushes'], ['paper', 'spock']),
        'paper': (['spock', 'rock'], ['disproves', 'covers'], ['scissors', 'lizard']),
        'scissors': (['paper', 'lizard'], ['cuts', 'decapitates'], ['rock', 'spock']),
        'spock': (['rock', 'scissors'], ['vaporizes', 'smashes'], ['paper', 'lizard']),
        'lizard': (['spock', 'paper'], ['poisons', 'eats'], ['rock', 'scissors'])
        }
    ai = AI(TYPE, rules, options)
    while True:
        STOP = ['exit', 'stop', 'no']
        human = get_input(options, STOP)
        computer = ai.pick()
        if human in STOP:
            break
        print ('player pick: {0}'.format(human))
        print ('computer pick: {0}'.format(computer))
        computer_is_winner, computer_index = occurrences(rules[human][0], computer)
        human_is_winner, human_index = occurrences(rules[computer][0], human)
        if human == computer:
           print ('tie')
           score.ties += 1
           ai.tied = (True, human)
        elif computer_is_winner:
            attack = rules[computer][1][human_index]
            print ('{0} {1} {2} computer wins!'.format(computer, attack, human))
            score.losses += 1
        elif human_is_winner:
            attack = rules[human][1][computer_index]
            print ('{0} {1} {2} human wins!'.format(human, attack, computer))
            score.wins += 1
        ai.played[human] += 1
        print (' ')

class AI:
    def __init__(self, TYPE, rules, options):
        self.TYPE = TYPE
        self.rules = rules
        self.options = options
        self.played = {
                    'lizard': 0,
                    'spock': 0,
                    'paper': 0,
                    'scissors': 0,
                    'rock': 0
                    }
        self.tied = (False, '')

    def pick(self):
        if self.TYPE == 'random':
            return AI.random(self)
        elif self.TYPE == 'learning':
            return AI.learning(self)
        elif self.TYPE == 'counter':
            return AI.counter(self)
    
    def random(self):
        return self.options[randint(0, 4)]

    def learning(self):
        random = randint(0, 1)
        if self.tied[0]:
            return self.rules[self.tied[1]][2][random]
        return self.rules[highest(self.played)][2][random]

    def counter(self):
        counter_counters = {
            'rock': 'lizard',
            'paper': 'rock',
            'scissors': 'paper',
            'spock': 'scissors',
            'lizard': 'spock',
            }
        return counter_counters[highest(self.played)]

def occurrences(sequence, find):
    for index, element in enumerate(sequence):
        if element == find:
            return False, index
    return True, None

def highest(dictonary):
    return max(dictonary, key=lambda x: x[0])
        
class Score:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
    
    def percent(total, numerator):
        DECIMAL_PLACE = 2
        CONVERT_TO_PERCENT = 100
        percent = numerator / float(total) * CONVERT_TO_PERCENT
        return round(percent, DECIMAL_PLACE)
        
    def board(self, TYPE):
        BANNER = '~~~~~~~~FINAL~SCORE~~~~~~~~'
        total = self.wins + self.losses + self.ties
        print(BANNER)
        print('TIES: {0} {1}%'.format(self.ties, Score.percent(total, self.ties)))
        print('HUMAN: {0} {1}%'.format(self.wins, Score.percent(total, self.wins)))
        print('COMPUTER({0}) {1} {2}%'.format(TYPE, self.losses, Score.percent(total, self.losses)))
        print(BANNER)

main()
