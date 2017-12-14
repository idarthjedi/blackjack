#!/usr/bin/env python
import random
import os
import sys
import time

from random import shuffle
from sys import platform

if sys.version_info[0] < 3:
    print("This script requires Python version 3 or greater!")
    sys.exit(1)


def clearscreen():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == 'win32':
        os.system('cls')
    elif platform == 'darwin':
        pass


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def introduction():
    clearscreen()
    print(BColors.HEADER + '\t\t\tWelcome to Blackjack.  You will bet against the dealer.')
    print(BColors.HEADER + '\t\t\tYour goal is to get as close to 21 without going over, or get the dealer to go '
                           'over 17.')
    print(BColors.HEADER + '\t\t\tCards have face value [2-10], with King, Queen and Jack equaling 10.')
    print(BColors.HEADER + '\t\t\tNote: Aces can count as as 1 or 11.')
    print(BColors.HEADER + '\t\t\t\t\t\t\t\t\tGood luck!')
    print(BColors.ENDC)


class Person(object):
    """
    Class for Person
    """
    cardhand = []

    def __init__(self, name):
        self.name = name
        pass

    def greet(self):
        print("Hello %s, welcome to BlackJack!" % self.name)

    def cleanhand(self):
        self.cardhand.clear()

    @property
    def cards(self):
        return self.cardhand

    def addcards(self, cards):
        self.cardhand = self.cardhand + cards


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
        print()
        animation = "|/-\\"
        idx = 0
        loop = 0
        while loop < 30:
            print('Shuffling card deck, please wait: ' + BColors.FAIL +
                  animation[idx % len(animation)] + BColors.ENDC +
                  '\r', end='')
            idx += 1
            loop += 1
            time.sleep(0.1)

        # Shuffle 3 times to make sure it's really good!
        for loop in range(1, 4):
            #print(self.cardcollection)
            shuffle(self.cardcollection)

    def deal(self, count):
        if (count < 1) or (count > len(self.cardcollection)):
            print(BColors.FAIL + "Not enough cards left in the deck" + BColors.ENDC)
        else:
            tempcollection = []
            for card in range(0,count):
                tempcollection.append(self.cardcollection.pop(0))
            #print("Popped Cards %s" % tempcollection)
            #print("Left over collection %s" % self.cardcollection)
            return tempcollection


def main():
    introduction()

    username = input("Please enter your name: ")
    # Create objects for both the user and the dealer
    user = Person(username)
    dealer = Person("Dealer")

    # Greet the user
    user.greet()

    # Generate the Deck
    d = Deck()

    # Shuffle the Deck
    d.shuffle()

    # Deal the first two cards
    user.addcards(d.deal(2))
    dealer.addcards(d.deal(2))


main()

# use this URL for details on how to do random shuffling, selecitng $$ etc.
# https://docs.python.org/3/library/random.html

