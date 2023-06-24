import random

# Creating a deck of 52 cards, and also their values
def create_deck():

    deck = []

    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

    ranks = ["Ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))

    random.shuffle(deck)
    return deck

# Deal out the cards
def deal_card(deck, hand):
    
    card = deck.pop()
    hand.append(card)
    return card


# calculating the the points for a hand
def calculate_points(hand):
    
    points = 0
    num_aces = 0

    for card in hand:
        rank = card[0]
        
        # A worth 1 or 11
        if rank == "Ace":
            points += 11
            num_aces += 1
        
        # K, J and Q are worth 10p
        elif rank in["Jack", "Queen", "King"]:
            points += 10
        
        # Cards have same value as rank
        else: 
            points += int(rank)
        
    # Adjusting points if points is under or 21
    while points > 21 and num_aces > 0:
        points -= 10
        num_aces -= 1
    
    return points

# Main function for the game
def play_blackjack():
    deck = create_deck()

    player_hand = []

    dealer_hand = []

    # Dealer takes two cards
    deal_card(deck, dealer_hand)
    deal_card(deck, dealer_hand)
    
    # Player takes two cards
    deal_card(deck, player_hand)
    deal_card(deck, player_hand)

    game_over = False

    while not game_over:
        player_points = calculate_points(player_hand)
        dealer_points = calculate_points(dealer_hand)

        print(f"Your hand: {player_hand}, points: {player_points}")
        print(f"Dealer first card: {dealer_hand[0]}")

        if player_points == 21 or dealer_points == 21 or player_points > 21:
            game_over = True
        else:
            continue_game = input("do you want to take one more card? Write Yes or No: ")

            if continue_game == "Yes":
                deal_card(deck, player_hand)
            else: 
                game_over = True

    while dealer_points < 17 and dealer_points != 21:
        deal_card(deck, dealer_hand)
        dealer_points = calculate_points(dealer_hand)

    print(f"Your hand: {player_hand}, points: {player_points}")
    print(f"Dealer hand: {dealer_hand}, points: {dealer_points}")

    if player_points <= 21 and (player_points > dealer_points or dealer_points > 21):
        print("You Won!")
    else:
        print("Dealer Won!")

play_blackjack()



 



