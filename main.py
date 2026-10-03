#Blackjack game

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
""""Random cards withdraw"""
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
"""Calculating score of cards"""
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score==c_score:
        return "Draw"
    elif c_score==0:
        return "Lose,Opponent has a Blackjack"
    elif u_score==0:
        return "Win!,You got a Blackjack"
    elif u_score>21:
        return "You went over.You Loose!"
    elif c_score>21:
        return "Computer went over.You Win!"
    elif u_score>c_score:
        return "You Win!"
    else:
        return "You Lose!"

def play_game_again():
    print(logo)
    user_cards=[]
    computer_cards=[]
    computer_score=-1
    user_score=-1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards are:{user_cards},Your scores:{user_score}")
        print(f"Computer's first card is:{computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_choice=input("Type 'y' to get another card or type 'n' to pass")
            if user_choice=='y':
                user_cards.append(deal_card())
            else:
                is_game_over=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"Your final hand:{user_cards},final scores:{user_score}")
    print(f"Computer's final hand:{computer_cards},final scores:{computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to restart the game of Blackjack.Type 'y' to restart")=="y":
    print("\n"*20)
    play_game_again()