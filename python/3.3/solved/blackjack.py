from random import randint

def black_jack(number_of_decks):
    deck = shuffle(initialize_deck(number_of_decks))
    wins = 0
    loses = 0
    while deck:
        try:
            hand = deck.pop() + deck.pop()
            hand, deck = hit_me_again(hand, deck)
            wins, loses = score(hand, wins, loses)
        except IndexError:
            break
    print_output(wins, loses)

def initialize_deck(number_of_decks):
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    NUMBER_OF_SUITS = 4
    return cards * NUMBER_OF_SUITS * number_of_decks

def shuffle(deck):
    length = len(deck)
    for count in range(length):
        index = randint(0, length - 1)
        card = deck.pop(index)
        deck.append(card)
    return deck

def hit_me_again(hand, deck):
    LIMIT = 11
    if deck and hand <= LIMIT:
        hand += deck.pop()
    return hand, deck

def score(value, wins, loses):
    WINNER = 21
    if value == WINNER:
        return wins + 1, loses
    return wins, loses + 1

def print_output(wins, loses):
    total = wins + loses
    print 'After', total, 'hands there was', wins, 'at', percent(wins, total)

def percent(numerator, denominator):
    percent = numerator / float(denominator) * 100
    DECIMAL_PLACES = 2
    return str(round(percent, DECIMAL_PLACES)) + '%'

black_jack(2)
