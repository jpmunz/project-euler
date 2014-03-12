from functools import total_ordering
from helpers import test

class Card(object):
    DIAMOND = 'D'
    CLUB = 'C'
    SPADE = 'S'
    HEART = 'H'

    FACE_VALUES = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    @staticmethod
    def parse_card(definition):
        '''
        Definition = <Rank><Suit>
        Suit = D | C | S | H
        Value = 2 - 9 | T | J | K | Q | A
        '''

        try:
            value = int(definition[0])
        except ValueError:
            value = Card.FACE_VALUES[definition[0]]
        suit = definition[1]

        return Card(value, suit)

@total_ordering
class Hand(object):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9

    def __init__(self, cards):
        self.cards = sorted(cards, lambda a, b: b.value - a.value)
        self.rank, self.rank_values = self.compute_rank()

    def compute_rank(self):
        flush = all(self.cards[0].suit == card.suit for card in self.cards)

        if flush and self.values == [14, 13, 12, 11, 10]:
            return Hand.ROYAL_FLUSH, self.values

        straight = all((self.cards[0].value - self.cards[s].value == s) for s in range(1, 5)) \
                   or (self.values == [14, 5, 4, 3, 2])

        if flush and straight:
            return Hand.STRAIGHT_FLUSH, self.values
        elif flush:
            return Hand.FLUSH, self.values
        elif straight:
            return Hand.STRAIGHT, self.values

        distinct = self.distinct_values

        distinct_counts = sorted(distinct.values())
        distinct_cards = sorted(distinct.keys(), lambda a, b: distinct[a] - distinct[b])

        if len(distinct) == 2:
            if distinct_counts[0] == 1:
                return Hand.FOUR_OF_A_KIND, [distinct_cards[1], distinct_cards[0]]
            elif distinct_counts[0] == 2:
                return Hand.FULL_HOUSE, [distinct_cards[1], distinct_cards[0]]
        elif len(distinct) == 3:
            if distinct_counts[2] == 3:
                return Hand.THREE_OF_A_KIND, [distinct_cards[2]] + sorted(distinct_cards[:2], lambda a, b: b-a)
            else:
                pairs = [max(distinct_cards[1], distinct_cards[2]),
                         min(distinct_cards[1], distinct_cards[2])]

                return Hand.TWO_PAIR, pairs + [distinct_cards[0]]
        elif len(distinct) == 4:
            return Hand.ONE_PAIR, [distinct_cards[3]] + sorted(distinct_cards[:3], lambda a, b: b-a)

        return Hand.HIGH_CARD, self.values

    @property
    def values(self):
        return [card.value for card in self.cards]

    @property
    def distinct_values(self):
        distinct = {}

        for card in self.cards:
            distinct.setdefault(card.value, 0)
            distinct[card.value] += 1

        return distinct

    def __lt__(self, other):
        return self.rank < other.rank \
                or (self.rank == other.rank and \
                    self.rank_values < other.rank_values)

    def __eq__(self, other):
        return self.rank == other.rank \
                and self.rank_values == other.rank_values

test(Card.parse_card('6D').suit, Card.DIAMOND)
test(Card.parse_card('6D').value, 6)
test(Card.parse_card('KD').value, 13)


def test_hand(cards, rank, rank_values):
    hand = Hand([Card.parse_card(card) for card in cards])
    test(hand.rank, rank)
    test(hand.rank_values, rank_values)

def test_win(winner, loser):
    winner_hand = Hand([Card.parse_card(card) for card in winner])
    loser_hand = Hand([Card.parse_card(card) for card in loser])

    test(winner_hand > loser_hand, True)

def test_tie(winner, loser):
    winner_hand = Hand([Card.parse_card(card) for card in winner])
    loser_hand = Hand([Card.parse_card(card) for card in loser])

    test(winner_hand == loser_hand, True)


test_hand(['AD', 'TD', 'JD', 'KD', 'QD'], Hand.ROYAL_FLUSH, [14, 13, 12, 11, 10])
test_hand(['AD', '4D', '3D', '2D', '5D'], Hand.STRAIGHT_FLUSH, [14, 5, 4, 3, 2])
test_hand(['8D', '4S', '5C', '6C', '7D'], Hand.STRAIGHT, [8, 7, 6, 5, 4])
test_hand(['8D', '4S', '4C', '4D', '4H'], Hand.FOUR_OF_A_KIND, [4, 8])
test_hand(['2D', '4S', '4C', '4D', '4H'], Hand.FOUR_OF_A_KIND, [4, 2])
test_hand(['8D', '8S', '8C', '3D', '3H'], Hand.FULL_HOUSE, [8, 3])
test_hand(['8D', '8S', '8C', '9D', '9H'], Hand.FULL_HOUSE, [8, 9])
test_hand(['JD', '4D', '8D', '2D', 'KD'], Hand.FLUSH, [13, 11, 8, 4, 2])
test_hand(['JD', '8H', '8D', '2D', '8C'], Hand.THREE_OF_A_KIND, [8, 11, 2])
test_hand(['JD', '8H', '8D', '2D', '2C'], Hand.TWO_PAIR, [8, 2, 11])
test_hand(['JD', '8H', '8D', '2D', '3C'], Hand.ONE_PAIR, [8, 11, 3, 2])
test_hand(['JD', '8H', 'QD', '2D', '3C'], Hand.HIGH_CARD, [12, 11, 8, 3, 2])

test_win(['8D', '8S', '8C', '3D', '3H'], ['JD', '8H', '8D', '2D', '3C'])
test_win(['8D', '8S', '8C', '9D', '9H'], ['8D', '8S', '8C', '3D', '3H'])
test_tie(['JD', '8H', '8D', '2D', '3C'], ['JD', '8H', '8D', '2D', '3C'])


def count_wins():
    wins = 0

    with open('poker.txt') as f:
        for line in f.readlines():
            cards = line.strip().split(' ')

            hand1 = Hand([Card.parse_card(card) for card in cards[:5]])
            hand2 = Hand([Card.parse_card(card) for card in cards[5:]])

            if hand1 > hand2:
                wins += 1

    return wins

print count_wins()

