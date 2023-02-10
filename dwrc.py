import random
TITLE = 'Daily water rate calculator.'
print (f'{TITLE:.^70}')
'''I use contruction ".^70" to decorate a title.
  Where "." - decorative symbol
  Where "^" - this сenters the text. Also can use "<", ">", "=".
  Where "70" - symbol count in title'''

def user_data():
    '''
    In this function i collect user data.
    i use a loop to avoid an error when the user enters incorrect data.
    '''
    name = input(f'Hello!\n'
    f'Please tell me your name to start a calc:')

    while True:
      try:
        act = float(input(f'Thanks, {name}\n Now tell me how many hours of sport activities do you have every day. '
        f'Choose from 0 to 6:'))
        break
      except Exception:
        print ('Ups, something wrong! \n Enter a float number. Let`s try again!') 
    
    while True:
      try:  
        mass = float(input('Ok! And tell me your weight in kg. \n I promise, i don`t tell this anybody:)'))
        break
      except Exception:
        print ('Ups, something wrong! \n Enter a float number. Let`s try again!') 

    water_calc(act, mass, name)

def water_calc(act, mass, name):
    '''
    In this function i define daily norm of water
    Function receives 2 argumets:
      - 'act' - activity hours of the day
      - 'mass' - the weight of the human
    '''
    if act <= 1:
      res = mass * 0.03
    elif act <=2:
      res = mass * 0.035
    elif act <=4:
      res = mass * 0.04
    elif act <=5:
      res = mass * 0.045
    else:
      res = mass *0.055
    motivator (res, name)

def motivator (res, name):
  '''
  In this function i return sum of water_calc function.
  Print result message in terminal and add random motivator phrase for user.
  I use 'random' module for randomize phraze. Phrazes i take from network:)
  Function receive 2 arguments:
    - 'res' - result from water_calc function
    - 'name' - user name
  '''

  phrases_list = [
        "Sports bring people together.",
        "Winning isn't everything, but it's a great feeling.",
        "Sportsmanship is key in any game.",
        "There's nothing like the excitement of a close match.",
        "The thrill of competition is what drives athletes to be their best.",
        "In sports, anything is possible.",
        "A true athlete gives it their all, no matter the outcome.",
        "Sports can teach us valuable life lessons, such as perseverance and teamwork.",
        "For a true sports fan, there's nothing like the thrill of a good game.",
        "Sports bring people from all walks of life together in a shared passion."
    ]

  phrase = random.choice(phrases_list)

  print (f'Nice, {name}, \nyour daily norm of water: {res} litres'
  f'\n{phrase}')

user_data ()