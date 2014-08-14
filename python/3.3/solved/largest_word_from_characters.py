def longest_word(filename):
    words, characters = setup(filename)
    passed = Passed()
    for word in words:
        if is_possible(word, list(characters)):
            passed.add(word)
    passed.longest()

def setup(filename):
    with open(filename) as file:
        return [line.strip().split(' ') for line in file]

def is_possible(word, available):
    return all([is_in(available, character) for character in word])

def is_in(available, character):
    try:
        available.remove(character)
    except ValueError:
        return False
    return True
    
class Passed:
    def __init__(self):
        self.words = {}

    def add(self, word):
        length = len(word)
        if length not in self.words:
            self.words[length] = []
        self.words[length].append(word)

    def longest(self):
        try:
            print(self.words[max(self.words.keys())])
        except ValueError:
            print('No Words Found')

longest_word('text.txt')
            
