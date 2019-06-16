import random


class Deck:
    cards_total = []

    def __str__(self):
        strng_deck = []
        for entry in Deck.cards_total:
            strng_deck.append(str(entry))
        return "Cards drawn: " + '\n\n' + '\n'.join(strng_deck)

    def start(self):
        suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
        Deck.cards_total.clear()
        for suit in suits:
            for value in values:
                Deck.cards_total.append(Card(suit, value))

    def draw(self):
        card = random.choice(Deck.cards_total)
        Deck.cards_total.remove(card)
        return card


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.point = Card.points(self)

    def __str__(self):
        return "A " + str(self.value) + " of " + self.suit

    def __repr__(self):
        return self.__str__()

    def points(self):
        amnt = 0
        if type(self.value) == int:
            amnt = self.value
        elif self.value in ['Jack', 'Queen', "King"]:
            amnt = 10
        elif self.value == 'Ace':
            amnt = 11
        return amnt


class Player:
    def __init__(self, wallet=100):
        self.wallet = wallet
        self.point_total = 0
        self.hand_list = []
        self.aces = 0

    def hit(self):
        d = deck.draw()
        self.hand_list.append(d)
        self.point_total += d.point
        if d.value == "Ace":
            self.aces += 1

    def ace_points(self):
        self.point_total -= 10
        self.aces -= 1

    def start(self):
        self.hand_list.clear()
        self.point_total = 0


repeat = 'yes'
deck = Deck()
human = Player()
dealer = Player()
while repeat.lower() == 'yes':
    print("\n"*100)
    stay = False
    s = False
    dbust = False

    human.start()
    dealer.start()
    deck.start()

    print("What is your bet? You have: $" + str(human.wallet))
    wager = float(input())
    while wager > human.wallet:
        print('too poor, try again')
        wager = float(input())
    human.wallet -= wager

    human.hit()
    human.hit()
    dealer.hit()
    dealer.hit()

    pbust = False
    while not stay and not pbust:
        print("\n" * 100)
        print("You have:")

        strng_hand = []
        for entry in human.hand_list:
            strng_hand.append(str(entry))
        print("\n" + '\n'.join(strng_hand))
        print(human.point_total)

        print("\n" * 3 + "The dealer has:")
        print("\n" + str(dealer.hand_list[0]) + "\n")

        print('\n\n\t\tHit or Stay?')
        choice = input()

        if choice.lower() == 'hit':
            human.hit()
            print(human.point_total)
        elif choice.lower() == 'stay':
            stay = True

        while human.point_total > 21 and not pbust:
            if human.ace_points() == 0:
                pbust = True
                break
            else:
                human.ace_points()


    while not s:
        if dealer.point_total < 17:
            dealer.hit()
        else:
            s = True
        if dealer.point_total > 21:
            dbust = True
            break
    print("\n"*100)
    print("########## FINAL ##########")
    print("You have:")

    strng_hand = []
    for entry in human.hand_list:
        strng_hand.append(str(entry))
    print("\n" + '\n'.join(strng_hand))

    print("\n" * 2 + "The dealer has:")
    strng_hand = []
    for entry in dealer.hand_list:
        strng_hand.append(str(entry))
    print("\n" + '\n'.join(strng_hand) + '\n')

    if pbust:
        print('You busted and lost .')
        wager = 0
    elif dbust:
        print('The Dealer busted, so you win!')
        human.wallet += (wager * 2)
        wager = 0
    elif human.point_total <= dealer.point_total:
        print('You lose.')
        wager = 0
    elif human.point_total > dealer.point_total:
        print('You win!')
        human.wallet += (wager * 2)
        wager = 0

    print("You have $" + str(human.wallet))
    print("Do you want to play again? (yes/no)")
    repeat = input()
