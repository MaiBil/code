"""
This is the second Milestone Proyect of Udemy's "Python Bootcamp"
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
          'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.rank = random.choice(ranks)
        self.suit = random.choice(suits)
        self.card = (self.rank, self.suit)

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_str = ''
        for card in self.deck:
            deck_str += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_str

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        print("\nYou have 100 chips.\n")
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        return self.total

    def lose_bet(self):
        self.total -= self.bet
        return self.total


def take_bet(chips):

    while True:
        while True:
            try:
                chips.bet = int(input("Make a bet: "))
            except ValueError:
                print("That was not a valid bet! Please try again")
                continue
            else:
                break
        if chips.total - chips.bet < 0:
            print("You don't have that many chips! Please try again")
            continue
        else:
            break

    return chips.bet


def hit(deck, hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck, hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value, sep='\n ')


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


# Print an opening statement
print("Welcome to BlackJack!\nRemember, if you come closer to 21 than \
the dealer (but not over 21), you win!\n\nBest of luck\n\n\n")

# Set up the Player's chips
chips = Chips()

while True:

    # Create & shuffle the deck, deal two cards to each player
    playing = True
    mydeck = Deck()
    mydeck.shuffle()
    player = Hand()
    dealer = Hand()
    player.add_card(mydeck.deal())
    dealer.add_card(mydeck.deal())
    player.add_card(mydeck.deal())
    dealer.add_card(mydeck.deal())

    # Prompt the Player for their bet
    take_bet(chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player, dealer)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(mydeck, player)

        if playing:

            # Show cards (but keep one dealer card hidden)
            show_some(player, dealer)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player, dealer, chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21:
        if dealer.value > 17:
            show_all(player, dealer)

        while dealer.value < 17:
            hit(mydeck, dealer)

            # Show all cards
            show_all(player, dealer)

        # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(player, dealer, chips)
        elif player.value > dealer.value:
            player_wins(player, dealer, chips)
        elif player.value < dealer.value:
            dealer_wins(player, dealer, chips)
        else:
            push(player, dealer)

    # Inform Player of their chips total
    print(f"\nYou now have {chips.total} chips\n")

    # Ask to play again
    play_again = input("Would you like to play again? Y/N ").upper()
    if play_again == 'Y':
        continue
    else:
        break
