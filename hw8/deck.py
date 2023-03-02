import itertools
import random
import shelve

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
    
    def save_deck(self, deck_name):
        '''Method for save deck in database
        Args:
            deck_name(str): the name of saved deck
        Returns: 
            string: with result of saving'''
        with shelve.open (deck_name, writeback=True) as deckfile:
            deckfile['deck'] = self.cards
            return f'Deck successfully saved!'
    
    @classmethod
    def load_deck(self, deck_name):
        '''Method for load deck from database
        Args:
            deck_name(str): the name of saved deck
        Returns: 
            list: with saved deck'''
        with shelve.open (deck_name, writeback=True) as deckfile:
            self.cards = deckfile['deck']
            #print(f'Deck successfully loaded from database!')
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

    deck_a = ClassicDeck()
    deck_b = SmallDeck()
    deck_c = SmallDeck()

    #print(deck_a.save_deck('First_saved_deck'))
    #get_deck = ClassicDeck().load_deck('First_saved_deck')
    #print(get_deck)



