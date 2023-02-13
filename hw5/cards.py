#!/usr/bin/env python3

import itertools
import random
import re

'''Text blocks for game'''
magic_rules = 'У цій грі я передбачу твоє майбтунє!'
magic_text0 = 'Так, дивимося, шо тебе чекає:\n'
magic_text1 = 'Хм...  Ця карта мені не подобається. Будь обережним!\n'
magic_text2 = 'Мммм... Щось гаряченьке чекає тебе наступного тижня!\n'
magic_text3 = 'Воу! В тебе є всі шанси знайти мільйони доларів наступного тижня!\n'
magic_text4 = 'Справи йдуть непогано, спробуй інтенсивніше вчити Пайтон!\n'
lacky_text0 = 'Ввведи ранк карти:'
lacky_text1 = 'ХА-ХА, Ти програв. Твої очки: '
lacky_text2 = 'Гру завершено, ти переміг. Твої очки: '
lacky_text3 = '. Твої очки: '
lacky_text4 = 'Нічого собі! Ти вгадав карту: '
lacky_text5 = 'Молодець! Ти вгадав масть: '
lacky_text6 = 'Спробуй ще раз\n Була карта: '

class GameCards():
    __slot__ = ('ranks', 'suits')

    ranks = list(range(6, 10+1)) + list ('JQKA')
    suits = ['\u2660 spades \u2660', 
    '\u2665 hearts \u2665',
    '\u2666 diamonds \u2666',
    '\u2663 clubs \u2663']
        
    @classmethod    
    def deck(cls):
        return list(itertools.product(cls.ranks, cls.suits))

    @classmethod
    def magic(cls): 
        deck = list(itertools.product(cls.ranks, cls.suits))
        return random.sample(deck, 4)

    def magic_play():
        four_cards = GameCards.magic()
        print (magic_text0)
        
        for card in four_cards:
            print (f'{card[0]}  {card[1]}')

            if card[0] == 6:
                print (magic_text1)

            elif card[1] == '\u2665 hearts \u2665' and card[0] == 'A':
                print (magic_text2)

            elif card[0] == 'A':
                print (magic_text3)
            
            elif 'diamonds' in card[1] and card[0] == 10:
                print (magic_text4)

    def lacky_card():
        points = 0

        while True:
            card = str(random.choice(GameCards.magic()))
            card = re.sub("[\(\)\'\"]", "", card)
            string = str(input(lacky_text0))

            if points <= -20:
                print (lacky_text1, points)
                break        

            elif points >= 20:
                print (lacky_text2, points)
                break

            if card.startswith(string):
                points += 15
                print (lacky_text4, card, lacky_text3, points)
            
            elif string in card:
                points += 7
                print (lacky_text5, card, lacky_text3, points)

            else:
                points -= 5
                print (lacky_text6, card, lacky_text3, points)

if __name__ == '__main__':
    GameCards()