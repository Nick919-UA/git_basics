#!/usr/bin/env python3

USAGE = """USAGE: {script} initial_sum percent fixed_period set_period

\tCalculate deposit yield. See script source for more details.
"""
USAGE = USAGE.strip()


def deposit(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield."""
    
    per = percent / 100
    growth = (1 + per) ** (set_period / fixed_period)

    one_month = 1/12
    six_month = 1/2
    
    growth1month = (1 + per) ** (one_month / fixed_period)
    growth6month = (1 + per) ** (six_month / fixed_period)
    growth1year = (1 + per) ** (1 / fixed_period)
    growth4year = (1 + per) ** (4 / fixed_period)
    
    return (f'Your yield: {initial_sum * growth}',
    	   f'\n\nFor correct data below please input "fixed_period" in years',
    	   f'\nyour yield for 1 month: {initial_sum * growth1month}',
    	   f'\nyour yield for 6 month: {initial_sum * growth6month}',
           f'\nyour yield for 1 year: {initial_sum * growth1year}',
           f'\nyour yield for 4 years: {initial_sum * growth4year}',
           )

def main(args):
    """Gets called when run as a script."""
    if len(args) != 4 + 1:
        exit(USAGE.format(script=args[0]))

    args = args[1:]
    initial_sum, percent, fixed_period, set_period = map(float, args)

    # same as
    # initial_sum = float(args[0])
    # percent = float(args[1])
    # ...

    res = deposit(initial_sum, percent, fixed_period, set_period)
    print(res)

def deposit_from_file():
    '''Function for get argumets from file and write to file
    Parametrs:
        val0, val1, val2, val3 (float): internal parametrs for func.
    Returns:
        string: with deposit restult and write result to file.'''
    val0 = None
    val1 = None
    val2 = None
    val3 = None

    with open ('git_basics\hw8\deposit_args.txt', 'r', encoding='cp1251') as file:  
        lines = file.readlines()
        
        try:  
            val0 = float(lines[0].split('=')[1].strip())
            val1 = float(lines[1].split('=')[1].strip())
            val2 = float(lines[2].split('=')[1].strip())
            val3 = float(lines[3].split('=')[1].strip())
        
        except Exception as ex:
            raise ImportError(f'{ex}\nFile must contains 4 parametrs, 1 param per sting\nExemple:"key=value"')

    try:
            result = deposit(val0, val1, val2, val3)
            write_deposit_result(result)
            return result
    except Exception as ex:
            f'{ex}'
        

def write_deposit_result(result):
    '''Function for write result to file

    Args:
        result(list): returned data from functions'''
    with open('git_basics\hw8\deposit_results.txt', 'w') as f:
        for items in result:
            f.write(f'{items}')

deposit_from_file()

#if __name__ == '__main__':
    #import sys

    #main(sys.argv)