from random import randint
def black_jack(number_of_decks):
	score = deal(initialize_deck(number_of_decks))
	total = score.wins + score.loses
	print 'After', total, 'hands there was', score.wins, 'at', percent(score.wins, total)

def deal(deck):
	score = reset_count()
	while deck:
		hand = deck.pop(random(deck)) + deck.pop(random(deck))
		hand, deck = hit_me_again(hand, deck)
		score = check(hand, score)
	return score

def initialize_deck(number_of_decks):
	cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
	NUMBER_OF_SUITS = 4
	return cards * NUMBER_OF_SUITS * number_of_decks

class reset_count:
	def __init__(self, wins=0, loses=0):
		self.wins = wins
		self.loses = loses

def random(sequence):
	return randint(0, len(sequence) - 1)

def check(value, score):
	WINNER = 21
	if value == WINNER:
		score.wins += 1
	else:
		score.loses += 1
	return score

def hit_me_again(hand, deck):
	LIMIT = 11
	if deck and hand <= LIMIT:
		hand += deck.pop(random(deck))
	return hand, deck

def percent(numerator, denominator):
    percent = numerator / float(denominator) * 100
    DECIMAL_PLACES = 2
    return str(round(percent, DECIMAL_PLACES)) + '%'

black_jack(2)
