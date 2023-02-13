#!/usr/bin/env python3

from cards import GameCards as play

#text blocs for game
hello_text = 'Привіт, давай розпочнемо грати. Обери, гру, яку бажаєш спробувати:\n'
input_text2 = '1 - Гадання на картах\n2 - Щасливчик! Вгадай карту\nВвведи цифру:'
game1 = '\nТи обрав гадання на картах, зараз погадаю тобі!'
game2 = '\nТи обрав гру вгадай карту.\nНапиши ранк карти (6-10, J, Q, K, A) або масть: diamonds, hearts, clubs, spades.'
game2_1 = '\nВгадаєш карту отримаєш 20 очок і переможеш, вгадаєш масть отримаєш 10 очок.\nНабери 20 очок для перемоги.'
input_else = 'Упс, щось не те! Необхідно обрати один з 2 варіантів. Для цього введи цифри 1 або 2.'

def lets_play():
    '''Function for choose a game.
    
    Input int numbers 1 or 2 for start game'''
    print (hello_text)
    start = int(input(input_text2))

    while True:
        if start == 1:
            print (game1)
            return play.magic_play()

        elif start == 2:
            print (game2)
            print (game2_1)
            return play.lacky_card()
        else:
            print (input_else)
            start = int(input(input_text2))

lets_play()