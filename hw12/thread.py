import threading
import requests
import json

#'cur_dict' need to collect all data from API
cur_dict = {}

def save_cache(name, data):
    '''Function for saving json cache from API'''
    with open (name, 'w') as f: 
        json.dump(data, f)
        result = 'Cache saved to json file'
        return result
    
def get_data(url, patch):
    '''Function for get json data from API and raturning data'''
    try:
        req = requests.get(url)
        data = req.json()
        save_cache(patch, data)
        return data
    except Exception:
        with open (patch, 'r') as file: 
            data = json.load(file)
            #print('data from file')
            return data
        
def get_pryvat():
    '''Function for get USD buy rate from Pryvatbank by API url. 
    Returns usd/uah buy rate'''
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'
    patch = fr'git_basics\hw12\data\pryvat_data.json'
    try:
        data = get_data(url, patch)
        usd = float(data[1]['buy']) 
        #print(usd)
        cur_dict['PRYVAT BANK'] = usd
        return usd
    except Exception as ex:
        print (f'{ex}')

def get_nbu():
    '''Function for get USD buy rate from NBU by API url. 
    Returns usd/uah buy rate'''
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    patch = fr'git_basics\hw12\data\nbu_data.json'
    try: 
        data = get_data(url, patch)
        usd = float(data[24]['rate'])
        #print(usd)
        cur_dict['NBU'] = usd
        return usd
    except Exception as ex:
        print (f'{ex}')

def get_exim():
    '''Function for get USD buy rate from EXIM BANK by API url. 
    Returns usd/uah buy rate'''
    url ='https://www.eximb.com/services/v1/rates/?lang=uk'
    patch = fr'git_basics\hw12\data\exim_data.json'
    try:
        data = get_data(url, patch)
        usd = float(data['rates']['cash']['data'][0]['buy'].replace(',', '.'))
        cur_dict['EXIM-BANK'] = usd
        return usd
    except Exception as ex:
        print (f'{ex}')

def currency(cur_dict):
        '''Function returns best buy rate for USD/UAH from dict'''
        m_value = max(cur_dict.values())
        m_key = max(cur_dict, key=cur_dict.get)
        print(cur_dict)
        print(f'The best USD/UAH buy rate is: {m_key}, {m_value} uah for 1 dollar')
        return f'The best bay USD/UAH buy rate is: {m_key}, {m_value} uah for 1 dollar'

get1 = threading.Thread(target=get_pryvat, name='Pryvat Bank API thread')
get2 = threading.Thread(target=get_nbu, name='NBU API thread')
get3 = threading.Thread(target=get_exim, name='Exim Bank API thread')
get4 = threading.Thread(target=currency, args=(cur_dict,), name='Best currency buy rate')

# Start the first two threads
get1.start()
get2.start()
get3.start()

# Wait for the first two threads to finish
get1.join()
get2.join()
get3.join()

#start last thread
get4.start()