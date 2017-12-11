import random
from random import shuffle


class Person(object):
    """
    Class for Person
    """
    def __init__(self, name):
        self.name = name
        pass

    def greet(self):
        print("Hello %s, welcome to BlackJack!" % self.name)


class Deck(object):
    """
    Class for deck of cards
    S[2-10,JQKA] = spade
    C[2-10,JQKA] = club
    H[2-10,JQKA] = heart
    D[2-10,JQKA] = diamonds

    cardcollection = [x + ':' + str(y) for x in ['H', 'S', 'C', 'D']
                          for y in [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']]
    use a set and random.shuffle to mix the card deck
    """

    cardcollection = [x + ':' + str(y) for x in ['H', 'S', 'C', 'D']
                      for y in [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']]

    def __init__(self):
        pass

    @property
    def cards(self):
        return self.cardcollection

    def __str__(self):
        return str(self.cardcollection)

    def shuffle(self):
        shuffle(self.cardcollection)


def main():
    username = input("Please enter your name: ")

    user = Person(username)
    user.greet()


main()

# use this URL for details on how to do random shuffling, selecitng $$ etc.
# https://docs.python.org/3/library/random.html

