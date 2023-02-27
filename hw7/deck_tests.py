from deck import *

    #>>>> for tests
cards = [(7, '♥ hearts ♥'), (7, '♦ diamonds ♦'), (7, '♣ clubs ♣'), (8, '♠ spades ♠')]
one_card = [(7, '♦ diamonds ♦')]

deck_a = ClassicDeck()
deck_b = SmallDeck()
deck_c = SmallDeck()

    #>>>> for tests shuffle in GameCards class
#print (deck_b)
#deck_b.shuffle()
#print (deck_b)

    #>>>> for tests __len__ in GameCards class
print (len(deck_b))
print (len(deck_a))

    #>>>> for tests __getitem__ in GameCards class
#print (deck_b[0]) #return card with index 0
#print (deck_b[3:7]) #return cards with index 3-7
#print (deck_b[0:10:2]) #return cards with index 0, 2, 4, 6, and 8. 2 is a step value, it defaults to 1.
#print (deck_b[999]) #raise IndexError with my own text

    #>>>> for tests __add__ in GameCards class
#print (len(deck_b))
#deck_b = deck_a + deck_b #added a two decks
#print (len(deck_b))

#print (len(deck_c))
#deck_c += cards #added a 4 new cards to deck
#print (len(deck_c))


    #>>>> for tests __sub__ in GameCards class
#print (len(deck_c))
#deck_c - cards #minus 4 cards from deck. If cards not in deck_c they dont be remove.
#print (len(deck_c))

    #>>>> for tests __contains__ in GameCards class
#check_cards = [(7, '♥ hearts ♥'), (11, '♦ diamonds ♦'), (7, '♣ clubs ♣'), (12, '♠ spades ♠')]

#print ((7, '♥ hearts ♥') in deck_c) #return true
#print ((12, '♥ hearts ♥') in deck_c) #return False

#for items in check_cards:
#    if items in deck_c:
#        print(f"{items} is in the deck")
#    else:
#        print(f"{items} is not in the deck")

    #>>>> for tests __bool__ in GameCards class
#print (bool(deck_a)) #return false
#deck_a.shuffle()
#print (bool(deck_a)) #return true


    #>>>> for tests __eq__ in GameCards class
#print (deck_b == deck_c) #return true because decks have same cards
#print (deck_a == deck_c) #return false because decks have different cards