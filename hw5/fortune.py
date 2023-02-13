#!/usr/bin/env python3

from cards import GameCards as play

#text blocs for game
hello_text = 'Привіт, давай розпочнемо грати. Обери, гру, яку бажаєш спробувати:\n'
input_text2 = '1 - Гадання на картах\n2 - Щасливчик! Вгадай карту\nВвведи цифру:'
game1 = 'Ти обрав гадання на картах, зараз погадаю тобі!'
input_else = 'Упс, щось не те! Необхідно обрати один з 2 варіантів. Для цього введи цифри 1 або 2.'

def lets_play():
    '''Function for choose a game.
    
    Input int numbers 1 or 2 for start game'''
    print (hello_text)
    start = int(input(input_text2))

    try:
        if start == 1:
            print (game1)
            play.magic_play()

        elif start == 2:
            play.lacky_card()
        
        else:
            print (input_else)


    except Exception as ex:
        print (ex)
    
lets_play()