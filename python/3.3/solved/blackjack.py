from random import randrange, shuffle

def black_jack():
    NUMBER_OF_DECKS = 3
    dealer = Dealer(NUMBER_OF_DECKS)
    score = Score()
    bet = 200
    while dealer.deck:
        score.record(dealer.deal(), bet)
    print_final(score)

class Dealer:
    def __init__(self, NUMBER_OF_DECKS=1):
        self.deck = Dealer.create_deck(NUMBER_OF_DECKS)
        shuffle(self.deck)

    def create_deck(NUMBER_OF_DECKS):
        DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        return DECK * NUMBER_OF_DECKS

    def deal(self):
        self.hand = 0
        try:
            Dealer.select(self, CARD_COUNT=2)
            Dealer.hit(self)
            return self.hand
        except IndexError:
            return None

    def select(self, CARD_COUNT):
        for iterator in range(CARD_COUNT):
            self.hand += self.deck.pop()

    def hit(self):
        LIMIT = 11
        if self.deck:
            if self.hand <= LIMIT:
                Dealer.select(self, CARD_COUNT=1)

class Score:
    def __init__(self, money=2000):
        self.money = money
        self.total = 0

    def record(self, hand, bet):
        WINNING_SCORE = 21
        winnings = bet * 2
        if hand is None:
            pass
        elif hand is WINNING_SCORE:
            self.money += winnings
        else:
            self.money -= bet
        self.total += 1

def print_final(score):
    STATISTICS = 'After {0} hands you have made {1} dollars.'
    print (STATISTICS.format(score.total, score.money))

black_jack()
