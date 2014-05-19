from random import randrange

def black_jack(number_of_decks):
    dealer = Dealer(number_of_decks)
    score = Score()
    deck = dealer.get_deck()
    while deck:
        score.tally(dealer.deal())
    print_final(score)

class Dealer:
    def __init__(self, number_of_decks=1):
        self.number_of_decks = number_of_decks

    def get_deck(self):
        Dealer.create_deck(self)
        Dealer.shuffle(self)
        return self.deck

    def create_deck(self):
        CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        NUMBER_OF_SUITS = 4
        self.deck = CARDS * NUMBER_OF_SUITS * self.number_of_decks

    def shuffle(self):
        LENGTH = len(self.deck)
        for count in range(LENGTH):
            random_card = self.deck.pop(randrange(LENGTH))
            self.deck.append(random_card)

    def deal(self):
        try:
            self.hand = self.deck.pop() + self.deck.pop()
            return Dealer.hit(self)
        except IndexError:
            return None, None

    def hit(self):
        LIMIT = 11
        if self.deck:
            if self.hand <= LIMIT:
                self.hand += self.deck.pop()
        return self.hand

class Score:
    def __init__(self, wins=0, total=0):
        self.wins = wins
        self.total = total

    def tally(self, hand):
        INCREMENT = 1
        WINNING_SCORE = 21
        if hand is None:
            pass
        elif hand is WINNING_SCORE:
            self.wins += INCREMENT
        self.total += INCREMENT

def print_final(score):
    STATISTICS = 'After {0} hands there was {1} at {2}%'
    print (STATISTICS.format(
                        score.total,
                        score.wins,
                        percentage(score)))

def percentage(score):
    DECIMAL_PLACE = 2
    CONVERT_TO_PERCENT = 100
    percent = score.wins / float(score.total) * CONVERT_TO_PERCENT
    return round(percent, DECIMAL_PLACE)

black_jack(2)
