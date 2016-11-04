from random import shuffle
from cards import Deck





def get_hand_value(cards):
    value = 0
    aces = 0
    for card in cards:
        if card.rank in ('10', 'J', 'Q', 'K'):
            value += 10
        elif card.rank in ('2', '3', '4', '5', '6', '7', '8', '9'):
            value += int(card.rank)
        elif card.rank == 'A':
            if value <= 10:
                value += 11
                aces += 1
        else:
            raise ValueError('Unknown rank')
    while value > 21 and aces:
        aces -= 1
        value -= 10 


#    for k in range(aces):
#        if value > 21:
#            value -= 10
    return value

if __name__ == '__main__':
    deck = Deck()
    shuffle(deck)
    new_game = 'y'
    player_value = 0

    while new_game == 'y':
        player = []
        dealer = []
        player.append(deck.draw())
        dealer.append(deck.draw())
        player.append(deck.draw())
        dealer.append(deck.draw())
        print('Your cards is: ', player)
        print('Dealers card is: ', dealer[1:])

        player_value = get_hand_value(player)

        while player_value < 21:
            decision = str(input('Card? (yes/no) '))
            if decision in ('n', 'no'):
                break
            elif decision in ('y', 'yes'):
                player.append(deck.draw())
                player_value = get_hand_value(player)
                print('Your cards is: ', player)
                print(player_value)
            else:
                print('Available decisions is "yes" and "no"')
        else:
            if player_value > 21:
                print('You lose!')
            elif player_value == 21:
                print('You win!')

        if player_value < 21:
            print('Dealers card is: ', dealer)
            dealer_value = get_hand_value(dealer)

            while dealer_value < 21 or dealer_value < player_value:
                dealer.append(deck.draw())
                dealer_value = get_hand_value(dealer)

            else:
                if dealer_value > 21:
                    print('You win!')
                elif dealer_value > player_value:
                    print('You lose!')
                else:
                    print('Standoff')
        print('Player card is:', player)
        print('Dealer card is:', dealer)
        n = len(deck)
        if n < len(Deck()) / 3:
            deck = Deck()
            shuffle(deck)
        new_game = str(input('Another game? (y/n)'))
        if new_game in ('n', 'no'):
            print('till next time')
