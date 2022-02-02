# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half. 
# Then the cards in the two halves are perfectly interleaved, 
# such that the original bottom card is still on the bottom and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, 
# gives ['ace', 'four', 'two', 'five', 'three', 'six']
# 
# Write a program that receives a single string (cards separated by space) and 
# on the second line receives a count of faro shuffles that should be made. Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.


cards_deck = input().split(' ')
number_of_shuffles = int(input())
print_deck = cards_deck

for _ in range(number_of_shuffles):
    top_half = print_deck[:len(print_deck)//2]
    bottom_half = print_deck[len(print_deck)//2:]
    print_deck.clear()
    for i in range(len(top_half)):
        print_deck.append(top_half[i])
        print_deck.append(bottom_half[i])

print(print_deck)

