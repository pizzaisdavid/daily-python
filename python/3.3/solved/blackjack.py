from random import randrange

def black_jack(number_of_decks):
    deck = create_and_shuffle_deck(number_of_decks)
    score = Score()
    while deck:
        deck, hand = deal(deck)
        score.check(hand)
    print_output(score)

def create_and_shuffle_deck(number_of_decks):
    return shuffle(create_deck(number_of_decks))

def create_deck(number_of_decks):
    CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    NUMBER_OF_SUITS = 4
    return CARDS * NUMBER_OF_SUITS * number_of_decks

def shuffle(deck):
    LENGTH = len(deck)
    for count in range(LENGTH):
        random_card = deck.pop(randrange(LENGTH))
        deck.append(random_card)
    return deck

class Score:
    def __init__(self, wins=0, total=0):
        self.wins = wins
        self.total = total

    def check(self, hand):
        INCREMENT = 1
        WINNING_SCORE = 21
        if hand is None:
            pass
        elif hand is WINNING_SCORE:
            self.wins += INCREMENT
        self.total += INCREMENT

def deal(deck):
    try:
        deck, hand = hit(deck, hand=deck.pop() + deck.pop())
        return deck, hand
    except IndexError:
        return None, None

def hit(deck, hand):
    LIMIT = 11
    if deck:
        if hand <= LIMIT:
            hand += deck.pop()
    return deck, hand

def print_output(score):
    STATISTICS = 'After {0} hands there was {1} at {2}%'
    print (STATISTICS.format(score.total, score.wins, percentage(score)))

def percentage(score):
    DECIMAL_PLACE = 2
    CONVERT_TO_PERCENT = 100
    percent = score.wins / float(score.total) * CONVERT_TO_PERCENT
    return round(percent, DECIMAL_PLACE)

black_jack(1)
