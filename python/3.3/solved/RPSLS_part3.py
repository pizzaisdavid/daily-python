from random import randint

def main():
    score = reset_score()
    options = ['lizard', 'spock', 'paper', 'scissors', 'rock']
    TYPE = introduction(options)
    score = game(TYPE, options, score)
    scoreboard(TYPE, score)
    
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

def get_input(options, stop=['']):
    combine = options + stop
    choice = input('Enter: ').lower()
    while choice not in combine:
        choice = input(options).lower()
    return choice

def game(TYPE, options, score):
    quits = ['exit', 'stop']
    rules = {
        # 'option': (['things it beats'], ['attack'], ['it loses to'])
        'rock': (['scissors', 'lizard'], ['crushes', 'crushes'], ['paper', 'spock']),
        'paper': (['spock', 'rock'], ['disproves', 'covers'], ['scissors', 'lizard']),
        'scissors': (['paper', 'lizard'], ['cuts', 'decapitates'], ['rock', 'spock']),
        'spock': (['rock', 'scissors'], ['vaporizes', 'smashes'], ['paper', 'lizard']),
        'lizard': (['spock', 'paper'], ['poisons', 'eats'], ['rock', 'scissors'])
        }
    ai = initialize_AI(TYPE, rules, options)
    while True:
        human = get_input(options, quits)
        computer = ai.select(TYPE)
        if human in quits:
            break
        print ('player pick: ' + human)
        print ('computer pick: ' + computer)
        computer_is_winner, computer_index = occurrences(rules[human][0], computer)
        human_is_winner, human_index = occurrences(rules[computer][0], human)
        if human == computer:
           print ('tie')
           score.ties += 1
           ai.tied = (True, human)
        elif computer_is_winner:
            attack = rules[computer][1][human_index]
            print (computer, attack, human, 'computer wins!', sep=' ')
            score.computer += 1
        elif human_is_winner:
            attack = rules[human][1][computer_index]
            print (human, attack, computer, 'human wins!', sep=' ')
            score.human += 1
        ai.played[human] += 1
        print (' ')
    return score

def initialize_AI(TYPE, rules, options):
    played = {
    'lizard': 0,
    'spock': 0,
    'paper': 0,
    'scissors': 0,
    'rock': 0
    }
    tied = (False, '')
    return AI(TYPE, rules, options, played, tied)

class AI:
    
    def __init__(self, TYPE='', rules={}, options=[], played={}, tied=()):
        self.TYPE = TYPE
        self.rules = rules
        self.options = options
        self.played = played
        self.tied = tied
    
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

    def select(self, TYPE):
        if TYPE == 'random':
            return AI.random(self)
        elif TYPE == 'learning':
            return AI.learning(self)
        elif TYPE == 'counter':
            return AI.counter(self)

def occurrences(sequence, find):
    for index, element in enumerate(sequence):
        if element == find:
            return False, index
    return True, None

def highest(dictonary):
    return max(dictonary, key=lambda x: x[0])
        
class reset_score:
    
    def __init__(self, human=0, computer=0, ties=0):
        self.human = human
        self.computer = computer
        self.ties = ties
        
    def total(self):
        return self.human + self.computer + self.ties
    
def percentage(wins, total):
    DECIMAL_PLACE = 2
    CONVERT_TO_PERCENT = 100
    percent = wins / float(total) * CONVERT_TO_PERCENT
    return str(round(percent, DECIMAL_PLACE)) + '%'
    
def scoreboard(TYPE, score):
    total = score.total()
    human = score.human
    computer = score.computer
    ties = score.ties
    banner = '~~~~~~~~FINAL~SCORE~~~~~~~~'
    print (banner)
    print ('TIES:', ties, percent(ties, total), sep=' ')
    print ('HUMAN:', human, percent(human, total), sep=' ')
    print ('COMPUTER(' + TYPE + '):', computer, percent(computer, total), sep=' ')
    print (banner)

main()
