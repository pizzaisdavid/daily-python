from random import randrange

def game(filename):
    LENGTH, COUNT = introduction()
    words = Words('words.txt', LENGTH, COUNT)
    selected_words = words.random
    guesses_left = 4
    guess = ''
    words.output()
    while guesses_left:
        message = 'You have guesses ' + str(guesses_left) + ' left '
        guess = get_input(selected_words, message)
        guesses_left -= 1
        if guess == words.winner:
            print('you win')
            break
        else:
            print(get_number_correct(words.winner, guess), '/', LENGTH, 'correct')

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

class Words:
    def __init__(self, filename, LENGTH, COUNT):
        self.filename = filename
        self.LENGTH = LENGTH
        self.COUNT = COUNT
        self.proper_length_words = Words.get_same_length_words(self)
        self.random = Words.randomly_select_words(self)
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
        selected = []
        for i in range(self.COUNT):
            random_index = randrange(len(self.proper_length_words))
            selected.append(self.proper_length_words.pop(random_index))
        return selected

    def randomly_select_a_word(self):
        random_index = randrange(self.COUNT)
        return self.random[random_index]

    def output(self):
        for word in self.random:
            print(word.upper())

def get_number_correct(word, comparison):
    word, comparison = word.lower(), comparison.lower()
    count = 0
    for index, character in enumerate(word):
        if character == comparison[index]:
            count += 1
    return count

game('words.txt')
