import itertools
import random

class GameCards():
    '''Class for Game Cards.'''
    ranks_classic = list(range(2, 10+1)) + list ('JQKA')
    ranks_small = list(range(6, 10+1)) + list ('JQKA')
    suits = ['\u2660 spades \u2660', 
        '\u2665 hearts \u2665',
        '\u2666 diamonds \u2666',
        '\u2663 clubs \u2663']
    cards_shuffle = False

    def shuffle(self):
        '''Method shuffle card deck.
        Returns:
            list: shuffles card deck.'''
        random.shuffle(self.cards)
        self.cards_shuffle = True
        return self.cards
    
    def __len__(self):
        '''Returns number of cards in deck'''
        return len(self.cards)

    def __getitem__(self, index):
        '''Method for get card from deck by index number.
        Args:
            index (int, slice): number of card in deck, exemple: 3 or 3:5 or 3:5:2, 2 is index step.
        Returns:
            list: card or cards list from deck by index.'''
        if isinstance(index, int):
            try:
                return self.cards[index]
            except IndexError:
                raise IndexError(f'Oops... The card number {index} is out of range.')
        
        elif isinstance(index, slice):     
            try:
                return self.cards[index.start:index.stop:index.step or 1]
            except Exception as ex:
                return f"Oops.. Something wrong\n{ex}"
        
        else:
            raise TypeError(f'You need provides only numbers. Exemple [1], [1:2].')
    
    
    def __add__(self, new):
        '''Method for adding decks or cards to deck.
        Args:
            new (list): a list of cards or deck.
        Returns:
            list: a new deck with added cards.'''
        try:
            if isinstance(new, list):
                self.cards += new
                return self.cards

        except Exception as ex:
            return f'OOpss.. Something wrong\n{ex}'   
             
    def __sub__(self, del_cards):
        '''Method for remove decks or cards to deck.
        Args:
            del_cards (list): a list of cards or deck.
        Returns:
            list: a new deck without removed cards.'''
        try:
            if isinstance(del_cards, list):
                for card in del_cards:
                    self.cards.remove(card)
            else:
                self.cards.remove(del_cards)
            return self.cards
        
        except Exception as ex:
            return f'OOpss.. Something wrong\n{ex}'

    def __contains__(self, cont):
        '''Method for check cards in deck.
        Args:
            cont (list): a list of cards or deck.
        Returns:
            bool: shows if there is actually a card in the deck.'''
        for card in self.cards:
            if cont[0] == card[0] and cont[1] == card[1]:
                return True
        return False
    
    def __bool__(self):
        '''Method for checking the presence of cards in the deck and was the deck shuffled.
        Returns:
            bool: shows if the deck has been shuffled and if there are cards in it.'''       
       
        if bool(self.cards) and self.cards_shuffle == True:
           return True
        else:
           return False

    def __eq__(self, other_deck):
        '''A method of checking the identity of two decks.
        Returns:
            bool: are the decks really the same.'''          
        if self.cards == other_deck.cards:
            return True
        return False


class ClassicDeck(GameCards):
    '''Method describe Classic deck with 52 cards.'''
    def __init__(self):
        '''Method  initializate class and create a deck with 52 cards'''        
        self.cards = []
        self.create_deck()

    def create_deck(self):
        '''Method create a deck of cards
        
        Method use 'itertools.product' and lists of rank and suite for create deck.

        Returns:
            list: deck of cards'''          
        self.cards = list(itertools.product(GameCards.ranks_classic, GameCards.suits))
        return self.cards
    
    def __str__(self):
        '''Method return string with cards in deck'''  
        return str(self.cards)
    

class SmallDeck(GameCards):
    '''Method describe Small deck with 36 cards.'''
    def __init__(self):
        '''Method initializate class and create a deck with 36 cards'''             
        self.cards = []
        self.create_deck()

    def create_deck(self):
        '''Method create a deck of cards
        
        Method use 'itertools.product' and lists of rank and suite for create deck.

        Returns:
            list: deck of cards'''  
        self.cards = list(itertools.product(GameCards.ranks_small, GameCards.suits))
        return self.cards
    
    def __str__(self):
        '''Method return string with cards in deck'''     
        return str(self.cards)


if __name__ == '__main__':
    cards = [(7, '♥ hearts ♥'), (7, '♦ diamonds ♦'), (7, '♣ clubs ♣'), (8, '♠ spades ♠')]
    one_card = [(7, '♦ diamonds ♦')]

    deck_a = ClassicDeck()
    deck_b = SmallDeck()
    deck_c = SmallDeck()


            #>>>> for tests __iter__ for deck

            #EXPLANATION: anything we can handle with a 'for' is iterable
            #             deck is list with items (item contain rank and suits) so we can iter them
            #             usind cycle 'for'. Exemple below.               
    #for items in deck_a:
            #print (f'{items}')


            #>>>> for tests shuffle in GameCards class
    #print (deck_b)
    #deck_b.shuffle()
    #print (deck_b)


        #>>>> for tests __len__ in GameCards class
    #print (len(deck_b))
    #print (len(deck_a))


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