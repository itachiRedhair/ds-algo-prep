import sys
from abc import ABC, abstractmethod


class Suit:
    Club = 0
    Diamond = 1
    Heart = 2
    Spade = 3


class Card(ABC):
    __available = False

    def __init__(self, face_value, suit_type):
        self.face_value = face_value
        self.suit_type = suit_type

    @abstractmethod
    def value(self):
        pass

    def suit(self):
        return self.suit_type

    def is_available(self):
        return self.__avaialble

    def mark_unavailable(self):
        self.__available = False

    def mark_available(self):
        self.__available = True


class Deck:
    __cards = []
    __dealt_index = 0

    def __init__(self):
        pass

    def set_deck_of_cards(self, cards):
        self.__cards = cards

    def shuffle(self):
        pass

    def remaining_cards(self):
        return len(self.__cards) - self.__dealt_index

    def deal_hand(self, number):
        pass

    def deal_card(self):
        pass


class Hand:
    __cards = []

    def __init__(self):
        pass

    def score(self):
        score = 0
        for card in self.__cards:
            score += card.value()

        return score

    def add_card(self, card):
        self.__cards.append(card)


class BlackJackCard(Card):
    def __init__(self, face_value, suit_type):
        super().__init__(face_value, suit_type)

    def value(self):
        return super().value()

    def value(self):
        if self.is_ace():
            return 1
        elif self.face_value >= 11 and self.face_value <= 13:
            return 10
        else:
            return self.face_value

    def minValue(self):
        if self.is_ace():
            return 1
        else:
            return value()

    def maxValue(self):
        if self.is_ace():
            return 11
        else:
            return value()

    def is_ace(self):
        return self.face_value == 1

    def isFaceCard(self):
        return self.face_value >= 11 and self.face_value <= 13


class BlackJackHand(Hand):
    def score(self):
        scores = []

        max_under = sys.maxsize
        min_over = -sys.maxsize+1

        for score in scores:
            if score > 21 and score < min_over:
                min_over = score
            elif score < 21 and score > max_under:
                max_under = score

        return min_over if max_under == (-sys.maxsize+1) else max_under

    def __possible_score(self):
        pass

    def busted(self):
        return score > 21
