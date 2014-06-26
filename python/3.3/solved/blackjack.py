from random import randrange, shuffle

def black_jack():
    NUMBER_OF_DECKS = 3
    dealer = Dealer(NUMBER_OF_DECKS)
    score = Score(200)
    player = Player()
    while dealer.deck:
        score.record(dealer.deal(), player.bet)
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
        Dealer.select(self, CARD_COUNT=2)
        Dealer.hit(self)
        return self.hand

    def select(self, CARD_COUNT):
        try: 
            for iterator in range(CARD_COUNT):
                self.hand += self.deck.pop()
        except IndexError:
            pass

    def hit(self):
        LIMIT = 11
        if self.hand <= LIMIT:
            Dealer.select(self, CARD_COUNT=1)
        
class Score:
    def __init__(self, money):
        self.money = money
        self.total = 0

    def record(self, score, bet):
        WINNING_SCORE = 21
        winnings = bet * 2
        if score is None:
            pass
        elif score is WINNING_SCORE:
            self.money += winnings
        else:
            self.money -= bet
        self.total += 1

class Player:
    def __init__(self):
        self.bet = 1

def print_final(score):
    STATISTICS = 'After {0} hands you have made {1} dollars.'
    print (STATISTICS.format(score.total, score.money))

black_jack()
