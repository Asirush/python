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

player1_wins += {True: 1, False: 0}[player1 > player2]
player2_wins += {True: 1, False: 0}[player1 < player2]

player_win = lambda x, y, str1, str2: str1 if x > y else str2
        
def countPoints(playerId, cards) -> None:
    if playerId == 1:
        for deck_id, card in enumerate(cards['cards']):
            print(card['value'], card['suit'])
    elif playerId == 2:
        for deck_id, card in enumerate(cards['cards']):
            print(card['value'], card['suit'])

def countCardWeigth(value, suit):


def startGame():
        # Перемешиваем колоду
    deck_id = api.shuffle_deck()
        # Вытаскиваем и печатаем 5 карт
    cards = api.draw_card(deck_id, count=0)

    while cards['remaining']>=0:
        countPoints(1, api.draw_card(deck_id, count=5))
        countPoints(2, api.draw_card(deck_id, count=5))
        cards

if __name__ == "__main__":
    startGame()
        