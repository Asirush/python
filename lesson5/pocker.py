import pockerApi as api

PLAYER1_COUNT = 0
PLAYER2_COUNT = 0
PLAYER1_WINRATE = 0
PLAYER2_WINRATE = 0
CART_SUTES = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]
CARTS = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jacket",
    "Queen",
    "King",
    "Ace"
]

# player1_wins += {True: 1, False: 0}[player1 > player2]
# player2_wins += {True: 1, False: 0}[player1 < player2]

# player_win = lambda x, y, str1, str2: str1 if x > y else str2
        
def countCardWeigth(value, suit):
    result = 0
    result += CARTS.find(value) + 2
    result *= CART_SUTES.find(suit) + 1
    return result
        
def countPoints(playerId, cards) -> None:
    player1, player2 = 0, 0
    if playerId == 1:
        for card in enumerate(cards['cards']):
            player1 += countCardWeigth(card["value"], card["suit"])
    elif playerId == 2:
        for card in enumerate(cards['cards']):
            player2 += countCardWeigth(card["value"], card["suit"])
    return player1, player2

def startGame():
        # Перемешиваем колоду
    deck_id = api.shuffle_deck()
        # Вытаскиваем и печатаем 5 карт
    cards = api.draw_card(deck_id, count=0)
    game1, game2 = 0, 0
    while cards['remaining']>0:
        game1 += countPoints(1, api.draw_card(deck_id, count=5))
        game2 += countPoints(2, api.draw_card(deck_id, count=5))
    
    player_win = lambda x, y, str1, str2: str1 if x > y else str2
    player_win(game1, game2, "player1", "player2")

if __name__ == "__main__":
    startGame()
        