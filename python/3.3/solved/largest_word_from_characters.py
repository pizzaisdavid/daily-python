def longest_word(filename):
    words, characters = setup(filename)
    passed = Passed()
    for word in words:
        if is_possible(list(word), characters):
            passed.add(word)
    passed.longest()

def setup(filename):
    with open(filename) as file:
        return [line.strip().split(' ') for line in file]

def is_possible(word, available):
    for character in available:
        delete(word, character)
    return word == []

def delete(sequence, element):
    try:
        sequence.remove(element)
    except ValueError:
        pass
        
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
            words = self.words
            print(words[max(words.keys())])
        except ValueError:
            print('No Words Found')

longest_word('text.txt')
            
