from random import randrange

def black_jack():
    NUMBER_OF_DECKS = 3
    dealer = Dealer(NUMBER_OF_DECKS)
    score = Score()
    deck = dealer.get_shuffled_deck()
    while deck:
        score.record(dealer.deal())
    print_final(score)

class Dealer:
    def __init__(self, NUMBER_OF_DECKS=1):
        self.NUMBER_OF_DECKS = NUMBER_OF_DECKS
        self.decks = []

    def get_shuffled_deck(self):
        Dealer.create_deck(self)
        Dealer.shuffle(self)
        return self.deck

    def create_deck(self):
        NUMBER_OF_SUITS = 4
        CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.deck = CARDS * NUMBER_OF_SUITS * self.NUMBER_OF_DECKS

    def shuffle(self):
        LENGTH = len(self.deck)
        for _ in range(LENGTH):
            random_card = self.deck.pop(randrange(LENGTH))
            self.deck.append(random_card)

    def deal(self):
        try:
            hand = self.deck.pop() + self.deck.pop()
            return Dealer.hit(self, hand)
        except IndexError:
            return None, None

    def hit(self, hand):
        LIMIT = 11
        if self.deck:
            if hand <= LIMIT:
                hand += self.deck.pop()
        return hand

class Score:
    def __init__(self, wins=0, total=0):
        self.wins = wins
        self.total = total

    def record(self, hand):
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

black_jack()
