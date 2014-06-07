from random import randrange

def fallout_hacking(filename):
    LEGNTH, COUNT = introduction()
    words = Words('words.txt', LENGTH, COUNT)
    game = Game(words)
    player = Player()
    words.output()
    while player.has_guesses:
        game.turn(player)

class Words:
    def __init__(self, filename, LENGTH, COUNT):
        self.LENGTH = LENGTH
         self.COUNT = COUNT
        self.filename = filename
        self.proper_length = Words.get_same_length_words(self)
        self.group = Words.randomly_select_words(self)
        self.winner = Words.randomly_select_a_word(self)

    def get_same_length_words(self):
        words = []
        lines = open(self.filename).readlines()
        for word in lines:
            word = word.strip()
            if len(word) == self.LENGTH:
                words.append(word)
        return words

    def randomly_select_words(self):
        words = self.proper_length
        selected = []
        for i in range(self.COUNT):
            random_index = randrange(len(words))
            word = words.pop(random_index)
            selected.append(word)
        return selected

    def randomly_select_a_word(self):
        random_index = randrange(self.COUNT)
        return self.group[random_index]

    def output(self):
        for word in self.group:
            print(word.upper())

def introduction():
    difficulty = ['1', '2', '3', '4', '5']
    message = 'Difficulty (1-5)?'
    level = get_input(difficulty, message)
    LENGTH, COUNT = set_difficulty(level)
    return LENGTH, COUNT

def get_input(options, message):
    choice = input(message).lower()
    while choice not in options:
        choice = input(options).lower()
    return choice

def set_difficulty(level):
    level = int(level)
    LENGTH = 5 + 2 * level
    COUNT = level ** 2
    return LENGTH, COUNT

class Player:
    def __init__(self):
        self.has_guesses = 4

class Game:
    def __init__(self, words):
        self.group = words.group
        self.winner = words.winner
        self.LENGTH = words.LENGTH

    def turn(self, player):
        message = 'You have guesses ' + str(player.has_guesses) + ' left '
        guess = get_input(self.group, message)
        if guess == self.winner:
            player.has_guesses = False
            print('you win')
        else:
            correct = get_number_of_matches(self.winner, guess)
            print(correct, '/', self.LENGTH, ' correct', sep='')
            player.has_guesses -= 1

def get_number_of_matches(word, comparison):
    count = 0
    for letter, character in zip(word, comparison):
        if letter == character:
            count += 1
    return count

fallout_hacking('words.txt')
