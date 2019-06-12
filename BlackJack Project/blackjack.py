from deck import Deck
from player import Player

def winner(player,dealer):
    playerdist = 21 - player.cards_sum()
    dealerdist = 21 - dealer.cards_sum()
    if (playerdist<0) and (dealerdist<0):
        return None
    elif (playerdist>=0) and (dealerdist<0):
        return player
    elif (playerdist<0) and (dealerdist>=0):
        return dealer
    elif playerdist<dealerdist:
        return player
    elif playerdist>dealerdist:
        return dealer
    elif playerdist==dealerdist:
        return None
    else:
        return None

def pick_card(player):
    return player.cards_sum() < 16

while True:
    print('WELCOME TO BLACK JACK')
    #Set the game
    dealer = Player('John',0,True)
    name = input('Insert name of the player: ')
    while True:
        try:
            balance = int(input('Insert initial balance: '))
        except:
            print('Not an integer. Try again')
            continue
        else:
            player = Player(name,balance,False)
            break

    #Create one deck
    deck = Deck()
    while True:
        try:
            ndecks = int(input('Insert number of decks: '))
        except:
            print('Not an integer. Try again')
            continue
        else:
            deck.new_decks(ndecks)
            break

    #START GAME
    print('Game started')
    rounds = 1
    while rounds > 0 and player.balance>0:
        dealer.cards = []
        player.cards = []
        print('Round {}'.format(rounds))
        while True:
            try:
                betamount = int(input('How much do u wanna bet? : '))
            except:
                print('Not an integer. Try again')
                continue
            else:
                player.bet(betamount)
                if player.betamount > 0:
                    break
                else:
                    print('Not enough money. Try again')
                    continue
        hits = 0
        player.cards.append(deck.take_card())
        print('Your initial card is {}'.format(player.cards[hits]))
        dealer.cards.append(deck.take_card())
        print("{}'s sum is {}".format(player.name,player.cards_sum()))

        while pick_card(dealer):
            dealer.cards.append(deck.take_card())

        another = input('Want another card? (Yes/No): ')
        while another.lower() not in 'yesno':
            print('Not a valid answer. Try again')
            another = input('Want another card? (Yes/No): ')
        if(another.lower()=='yes'):
            player.hit = True
            hits += 1
        else:
            player.hit = False

        while player.hit and player.cards_sum()<21:
            player.cards.append(deck.take_card())
            print('Your next card is {}'.format(player.cards[hits]))
            print("{}'s sum is {}".format(player.name,player.cards_sum()))
            another = input('Want another card? (Yes/No): ')
            while another.lower() not in 'yesno':
                print('Not a valid answer. Try again')
                another = input('Want another card? (Yes/No): ')
            if(another.lower()=='yes'):
                player.hit = True
                hits += 1
            else:
                player.hit = False

        print('Round {} ended.'.format(rounds))
        print('Dealers sum is {}'.format(dealer.cards_sum()))
        roundwinner = winner(player,dealer)
        if roundwinner == player:
            player.win()
            print("{} won {}$".format(player.name,player.betamount))
        elif roundwinner == dealer:
            player.lose()
            print("{} lost {}$".format(player.name,player.betamount))
        else:
            print('Its a draw!')

        print("{} has {}$ left".format(player.name,player.balance))

        anotherround = input('Another round? :')
        while anotherround.lower() not in 'yesno':
            print('Not a valid answer. Try again')
            another = input(' Want another card? (Yes/No): ')
        if(anotherround.lower()=='yes'):
            rounds += 1
            continue
        else:
            break

    print('GAME ENDEND. SEE YOU SOON')
    quit()
