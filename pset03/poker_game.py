from cards import (deal, poker_classification)

def play():
    # ask for numbers of players
    response = input("Enter the number of players(2-10):")
    response = response.strip().lower()
    if response in ("bye", "exit"):
        raise SystemExit
    if not response.isdigit():
        print("input integer")
        return play()
    number_of_players = int(response)
    if number_of_players < 2 or number_of_players > 10:
        print("Value between 2 and 10")
        return play()
    print

    hands = deal(number_of_players, 5)

    for hand in hands:
        line = ' '.join(str(card) for card in hand)
        line += f'is a {poker_classification(hand)}'
        print(line)
    
    play()

play()