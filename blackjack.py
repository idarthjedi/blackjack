#!/usr/bin/env python
import random
import os
import sys
import time
import codecs

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
    print()
    print()
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
    __cardhand = []

    def __init__(self, name):
        self.name = name
        pass

    def greet(self):
        print()
        print("Hello %s, welcome to BlackJack!" % self.name)

    def cleanhand(self):
        """
        Empty out all the cards for the user object
        """
        self.__cardhand.clear()

    def getcardvalue(self, card, currenttotal=0, ignoreace=True):
        """
        Pass this method a card, it will return the value of the card
        :param card: a Card in the format [FaceValue: Suit]
        :param currenttotal: The current running hand total used when ignoreace = False to determine Ace value
        :param ignoreace: instructs the method to ignore Ace Values
        :return: A value for the card
        """
        cardtype = card.split(":")[0]

        if (cardtype == "J") or (cardtype == "Q") or (cardtype == "K"):
            self.printcardvalue(card, 10)
            return 10
        elif cardtype == 'A':
            if not ignoreace:
                if currenttotal > 11:
                    self.printcardvalue(card, 1)
                    # count the A as a 1
                    return 1
                else:
                    # count the A as a 10
                    self.printcardvalue(card, 10)
                    return 10
            else:
                return 0
        else:
            self.printcardvalue(card, int(cardtype))
            return int(cardtype)

    def printcardvalue(self, card, value):
        print("Total value for %s is %d" % (card, value))

    @property
    def cards(self):
        return self.__cardhand

    @property
    def displaycards(self):
        """
        This method will tally up and print a list of all the cards in the users hand
        :return: Total value of all cards in the hand
        """
        value = 0
        for s in self.__cardhand:
            value += self.getcardvalue(s)

        # after looping through all the cards, let's go back and review the
        # total # of A's and determine whether we should value them at 10 or 1
        # for this program, I will make an assumption that we will use 10 if (cards - A) + A < 21

        acelist = filter(lambda x: 'A:' in x, self.__cardhand)
        for acard in acelist:
            value += self.getcardvalue(acard, value, False)

        print("Total hand value is %d" % value)
        return value

    def addcards(self, cards):
        self.__cardhand = self.__cardhand + cards


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

    __cardcollection = [str(y) + ':' + x for y in
                      [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
                      for x in ['S', 'H', 'D', 'C']]

    def __init__(self):
        pass

    @property
    def cards(self):
        return self.__cardcollection

    def __str__(self):
        return str(self.__cardcollection)

    def shuffle(self):
        print()
        animation = "|/-\\"
        idx = 0
        loop = 0
        while loop < 30:
            print('\tShuffling card deck, please wait: ' + BColors.FAIL +
                  animation[idx % len(animation)] + BColors.ENDC + '\r', end=" ")
            idx += 1
            loop += 1
            time.sleep(0.1)

        # Shuffle 3 times to make sure it's really good!
        for loop in range(1, 4):
            shuffle(self.__cardcollection)
            print()

    def deal(self, count):
        if (count < 1) or (count > len(self.__cardcollection)):
            print(BColors.FAIL + "Not enough cards left in the deck" + BColors.ENDC)
        else:
            tempcollection = []
            for card in range(0,count):
                tempcollection.append(self.__cardcollection.pop(0))
            return tempcollection

def displayuserscards(user):
    print(BColors.FAIL)
    print("Display %s's hand" % user.name)
    print(BColors.ENDC)

    return user.displaycards

def hitorstay():
    validanswer = False
    while not validanswer:
        answer = input("Would you like to [h] or [s]: (h/s) ")
        if (str(answer).lower() == "s") or (str(answer).lower() == "h"):
            validanswer = True
            return answer

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

    usertotal = displayuserscards(user)

    print(BColors.FAIL)
    print("Display %s's hand" % dealer.name)
    print(BColors.ENDC)
    dealer.getcardvalue(dealer.cards[0], 0, False)
    print()

    answer = hitorstay()
    if answer == "h":
        user.addcards(d.deal(1))
        usertotal = displayuserscards(user)

    # display all the dealers cards
    dealertotal = displayuserscards(dealer)
    if ((usertotal <= 21) and (usertotal > dealertotal)):
        print()
        print(BColors.OKGREEN)
        print("You won!")
        print(BColors.ENDC)
    else:
        print()
        print(BColors.FAIL)
        print("You lost!")
        print(BColors.ENDC)


main()

# use this URL for details on how to do random shuffling, selecitng $$ etc.
# https://docs.python.org/3/library/random.html

