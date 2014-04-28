from random import randint

def main():
    
    def get_input(options, stop=['']):
        combine = options + stop
        choice = input('Enter: ').lower()
        while choice not in combine:
            choice = input(options).lower()
        return choice
        
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
    
    def AI(AI_TYPE, rules, options, played, tied):
    
        def highest(dictonary):
            return max(dictonary, key=lambda x: x[0])
        
        def random(options):
            return options[randint(0, 4)]

        def learning(rules, played, tied):
            random = randint(0, 1)
            if tied[0]:
                return rules[tied[1]][2][random]
            return rules[highest(played)][2][random]

        def counter(rules, played, tied):
            counter_counters = {
                'rock': 'lizard',
                'paper': 'rock',
                'scissors': 'paper',
                'spock': 'scissors',
                'lizard': 'spock',
                }
            return counter_counters[highest(played)]
        
        if AI_TYPE == 'random':
            return random(options)
        elif AI_TYPE == 'learning':
            return learning(rules, played, tied)
        return counter(rules, played, tied)
        
    class set_score():
        def __init__(self, human=0, computer=0, ties=0):
            self.human = human
            self.computer = computer
            self.ties = ties
            
        def total(self):
            return self.human + self.computer + self.ties
        
    def game(AI_TYPE, options):
        
        def occurrences(sequence, find):
                for index, element in enumerate(sequence):
                    if element == find:
                        return False, index
                return True, None
                
        quits = ['exit', 'stop']
        played = {
            'lizard': 0,
            'spock': 0,
            'paper': 0,
            'scissors': 0,
            'rock': 0
            }
        rules = {
            # 'option': (['things it beats'], ['attack'], ['it loses to'])
            'rock': (['scissors', 'lizard'], ['crushes', 'crushes'], ['paper', 'spock']),
            'paper': (['spock', 'rock'], ['disproves', 'covers'], ['scissors', 'lizard']),
            'scissors': (['paper', 'lizard'], ['cuts', 'decapitates'], ['rock', 'spock']),
            'spock': (['rock', 'scissors'], ['vaporizes', 'smashes'], ['paper', 'lizard']),
            'lizard': (['spock', 'paper'], ['poisons', 'eats'], ['rock', 'scissors'])
            }
        tied = (False, '')
        while True:
            human = get_input(options, quits)
            computer = AI(AI_TYPE, rules, options, played, tied)
            if human in quits:
                break
            print ('player pick: ' + human)
            print ('computer pick: ' + computer)
            computer_is_winner, computer_index = occurrences(rules[human][0], computer)
            human_is_winner, human_index = occurrences(rules[computer][0], human)
            if human == computer:
               print ('tie')
               score.ties += 1
               tied = (True, human)
            elif computer_is_winner:
                attack = rules[computer][1][human_index]
                print (computer, attack, human, 'computer wins!', sep=' ')
                score.computer += 1
            elif human_is_winner:
                attack = rules[human][1][computer_index]
                print (human, attack, computer, 'human wins!', sep=' ')
                score.human += 1
            print (' ')
        
    def scoreboard(AI_TYPE):
        
        def percent(numerator):
            percent = numerator / score.total() * 100
            DECIMAL_PLACES = 2
            return str(round(percent, DECIMAL_PLACES)) + '%'

        banner = '~~~~~~~~FINAL~SCORE~~~~~~~~'
        print (banner)
        print ('TIES:', score.ties, percent(score.ties), sep=' ')
        print ('HUMAN:', score.human, percent(score.human), sep=' ')
        print ('COMPUTER(' + AI_TYPE + '):', score.computer, percent(score.computer), sep=' ')
        print (banner)

    score = set_score()
    options = ['lizard', 'spock', 'paper', 'scissors', 'rock']
    AI_TYPE = introduction(options)
    game(AI_TYPE, options)
    scoreboard(AI_TYPE)

main()
