from random import randint
def black_jack(number_of_decks):
	number_of_cards = 2
	cards = deal(number_of_decks, number_of_cards)

def deal(number_of_decks, number_of_cards):
	NUMBER_OF_CARDS_IN_A_DECK = 52
	deck = initialize_deck(number_of_decks)
	while deck:
		indices = draw_two(deck)
	print (cards)

def initialize_deck(number_of_decks):
	deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
	NUMBER_OF_SUITS = 4
	return deck * NUMBER_OF_SUITS * number_of_decks

def draw_two(deck):
	indices = []
	while len(indices) < 2:
		indices.append(randint(0, len(deck)))
		set(indices)
	return indices


def cut(sequence, index, length=1):
	return sequence[:index] + sequence[index + length:]

black_jack(2)
