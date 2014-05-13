from random import randrange

def black_jack(number_of_decks):
    deck = create_and_shuffle_deck(number_of_decks)
    wins, total = 0, 0
    while deck:
        try:
            hand = deck.pop() + deck.pop()
            hand, deck = hit_me_again(hand, deck)
            wins, total = wins + score(hand), total + 1
        except IndexError:
            break
    print_output(wins, total)

def create_and_shuffle_deck(number_of_decks):
    CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    NUMBER_OF_SUITS = 4
    return shuffle(CARDS * NUMBER_OF_SUITS * number_of_decks)

def shuffle(deck):
    LENGTH = len(deck)
    for count in range(LENGTH):
        random_card = deck.pop(randrange(LENGTH))
        deck.append(random_card)
    return deck

def hit_me_again(hand, deck):
    LIMIT = 11
    if deck and hand <= LIMIT:
        hand += deck.pop()
    return hand, deck

def score(value):
    WINNER = 21
    if value == WINNER:
        return 1
    return 0

def print_output(wins, total):
    DECIMAL_PLACE = 2
    percent = str(round(wins / float(total) * 100, DECIMAL_PLACE)) + '%'
    print 'After', total, 'hands there was', wins, 'at', percent

black_jack(2)
