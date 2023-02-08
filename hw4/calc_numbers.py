#!/usr/bin/env python3

def calc_numbers(*args):
    '''Function that calculate all numbers.
    
    For correctly work of this function, i check the type of arguments.
    I use 'isinstance()' function to check type. For check elements in list i opened them using 'for' loop.
    
    Function arguments:
        args(int, float, list, tuple) - int and float argumets, lists or tuples with int and float elements
    
    Function variables:
        sum_elements - service variable for summing elements in lists and tuples
        iterable - service variable to check types 'list', 'tuple' in *args
        item - service variable to check types in types 'int', 'float' in 'iterable'.
        
    Function return sum of all arguments and Sum divided by the number of elements, rounded to 2 digits'''

    sum_elements = 0

    try:
        for iterable in args:
            if isinstance(iterable, (list, tuple)) == True:
                for item in iterable:
                    if isinstance(item, (int, float)) == True:
                        sum_elements += item
            elif isinstance(iterable, (int, float)) == True:
                sum_elements += iterable
        return f'Sum of all elemetns: {round(sum_elements), 2}\n' \
               f'Sum divided by the number of elements: {round(sum_elements / len(args), 2)}'

    except Exception as ex:
        return f'{ex}\n Something wrong, look at the error message!'

#for tests
numberlist = [5,10,200,300, 400.99, 'omg!']
numbertuple = (999, 6886, 'lol', 94949)
print (calc_numbers(numberlist, numbertuple, 5, 10.77, 100.50505, 300, 'he-he', 500))