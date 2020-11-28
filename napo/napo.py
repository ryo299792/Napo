from deck import Deck 
from hand import Hand


deck = Deck(1)

print("YAMA FUDA")
print(deck.cards)

# カードの枚数 104
print(len(deck.cards))

# カードを5枚引く[♣︎-2, ❤︎-2, ♣︎-2, ♦︎-4, ❤︎-1]
# 引いたカードはリストから削除される
nakaoki=Hand(deck.get_card(4))
nakaoki.print_hand()

cards_player=[]
for i in range(5):
    cards_player.append(Hand(deck.get_card(10)))

for i in range(5):
    cards_player[i].print_hand()
