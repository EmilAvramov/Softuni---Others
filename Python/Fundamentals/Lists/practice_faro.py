cards = str(input()).split(' ')
shuffles = int(input())

mid = len(cards) // 2
shuffled_list = []

for index_shuffles in range(shuffles):
    shuffled_list = []
    for index_cards in range(mid):
        shuffled_list.append(cards[index_cards])
        shuffled_list.append(cards[mid])
        mid += 1
    cards = shuffled_list
    mid = len(cards) // 2

print(shuffled_list)
