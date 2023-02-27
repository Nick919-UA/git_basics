from config import token
import errors
import requests
import datetime

class City():
    '''Class that represent object City.
    
    in this class you can set coordinates of city.
    
    Atributes:
        name(str): String with city name.
        coordinates (taple): String with coordinates of city.
        
    Methods:
        get_cooridantes: for set new coordinates via API.
        name setter: for change city name'''
    def __init__ (self, name):
        '''Method that inicializated class
        
        Args:
            name(str): name of place on Earch for get weather. In english.
            coordinates(tuple): a tuple of coordinates with float numbers (latitude, longitude).
        Methods:
            get_cooridantes: for coordinates via API.
        '''
        self._name = name
        self._coordinates = None 
        self.get_cooridantes()   
        #print (self._coordinates)
    @property
    def name(self):
        '''Method returns coordinates in city Class.
        
        Returns:
            string: value of variable _name.'''
        return self._name

    @name.setter
    def name (self, val):
        '''Nethod for set coordinates of city.

        Args:
            val (str): string that contains city name (Only a-z, A-Z).
        
        Notes:
            A separate class (CityNameError()) is used to except errors with incorrect input of city name. 
        
        Tip:
            For test CityNameError() class try input incorrect name (like a: 'fdsfdsfds235434534'), watch error message.    
            
        Returns:    
            string: with new city name.'''
        if val.isalpha():
            self._name = val
            return f'New city name: {self._name}.'
        else:
            raise errors.CityNameError()

    def get_cooridantes(self):
        '''Method for get coordinates by city name
        
        Parametrs:
            self_name(str): city name
            token(str): open weather api token

        Notes:
            A separate class CoordinateError(), ApiAnswerError(), etc
            is used to except errors when updating coordinates.
            
        Returns:
            tuple: with new coordinates'''
        try:
            data_answer = ()
            url = f'http://api.openweathermap.org/geo/1.0/direct?q={self._name}&limit=1&appid={token}'
            req = requests.get(url)
            data_answer = req.json()
            self._coordinates = (data_answer[0]['lat'], data_answer[0]['lon'])
            #print (self._coordinates)
            #print(data_answer)
            return f'New coordinates of {self._name} is: {self._coordinates}'

        except requests.exceptions.ConnectionError:
            error_text = str(data_answer)
            raise errors.ApiAnswerError(error_text)
        
        except IndexError:
            raise errors.CoordinateError()

        except KeyError:
            error_text = str(data_answer)
            raise errors.ApiAnswerError(error_text)
                        
        
    def __str__(self):
        '''Method returns string with city name and coordinates.'''
        return f'name={self._name}, coordinates={self._coordinates}'


class Weather():
    '''Class for watch weather around ther world by coordinates or city name.
    
    Defoult value of 'name' i s Kyiv. So you can try watch weather without your parametrs.'''
    weather_data = None
    def __init__(self, name='Kyiv', coordinates=None):
        '''Method that inicializated class
        
        Args:
            name(str): name of place on Earch for get weather. In english.
            coordinates(tuple): a tuple of coordinates with float numbers (latitude, longitude).
        '''
        self.name = name
        self.coordinates = coordinates

    def _upd_weather(self):
        '''Updates the weather data for the city
        
        In this method weather data update by api openweathermap. 
        
        Notes:
            Method try to receive info from API by 2 types of URL, using coordinates and by city name. 
            Uncomment the 'print' to see which link got weather data.
            A separate class (UpdateWeatherError()) is used for return en errors with connection.

        Returns:
            string: json data from api.'''
        
        try:
            if self.coordinates is not None:
                self.lat = self.coordinates[0]
                self.lon = self.coordinates[1]
                url = f'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={token}&units=metric'
                req = requests.get(url)
                self.weather_data = req.json()
                #print (f'Weather updated by coordinates {self.coordinates}')

            else:
                url = f'https://api.openweathermap.org/data/2.5/weather?q={self.name}&appid={token}&units=metric'
                req = requests.get(url)
                self.weather_data = req.json()
                #print (f'Weather updated by city name {self.name}')

        except requests.exceptions.ConnectionError:
            raise errors.UpdateWeatherError()
    
    def watch_weater(self):
        '''Returns a string with the current weather for the city.
        
        Parameters:
            weather_data(str): Internal. Json data from api.
            weather_types(dict): Internal. Used to decorate weather information.

        Notes:
            A separate class (ApiAnswerError()) is used to except KeyError.
            Information about errors get from API answer, if API answer is None, info will be get from ApiAnswerError class.
        
        Tip:
            For test ApiAnswerError class try to update weather with incorrect city name or API Token and watch error message.
             
        Returns:
            string: formatted weather data from variable 'weather_data(str)'.'''
        weather_types = {'Clear' : 'Ясно \U00002600 / \U0001F319',
            'Clouds' : 'Хмарно \U00002601 ',
            'Rain':'Дощ \U0001F327',
            'Drizzle':'Невеликий дощ \U0001F326',
            'Thundestorm':'Гроза \U000026C8',
            'Snow':'Сніг \U0001F328',
            'Mist':'Туман \U0001F32B'}
        
        if not self.weather_data:
            self._upd_weather()

        if isinstance(self.weather_data, str):
            return self.weather_data
        
        try:
            ct_name = self.weather_data['name']
            cur_weather = self.weather_data['main']['temp']
            wea_desc = self.weather_data['weather'][0]['main']
            
            if wea_desc in weather_types:
                wd = weather_types[wea_desc]
            else:
                wd = 'Глянь у вікно:), там якась фігня' 
            
            humidity = self.weather_data['main']['humidity']
            pressure = self.weather_data['main']['pressure']
            wind = self.weather_data['wind']['speed']
            sunrise = datetime.datetime.fromtimestamp(self.weather_data['sys']['sunrise'])
            sunset = datetime.datetime.fromtimestamp(self.weather_data['sys']['sunset'])
            day_time = datetime.datetime.fromtimestamp(self.weather_data['sys']['sunset']) - datetime.datetime.fromtimestamp(self.weather_data['sys']['sunrise'])
            
            return (f'Погоду у {ct_name}\nТемпература: {cur_weather}°C, {wd}\n'
            f'Вологість: {humidity}%\n'
            f'Тиск: {pressure} мм. рт. ст.\n'
            f'Вітер: {wind} метрів за секунду\n\n'
            f'Схід сонця: {sunrise.strftime("%d/%m/%Y, %H:%M:%S")}\n'
            f'Захід сонця: {sunset.strftime("%d/%m/%Y, %H:%M:%S")}\n'
            f'Тривалість дня: {day_time}')  

        except KeyError:
            error_text = str(self.weather_data['message'])
            raise errors.ApiAnswerError(error_text)


    #>>>>> for tests City class        
#city1 = City('Lviv')

#print(city1)
#print(city1.get_cooridantes())
#print(city1)

    #>>>>> for Tests weather class
#weather = Weather().watch_weater()
#print(weather)

    #>>>>> for tests object of City class in Weather class
#city_weather = Weather(city1._name, city1._coordinates)
#print (city_weather.watch_weater())
#print (city_weather.name)
#print (city_weather.coordinates)

    #>>>>> for tests UpdError classes (watch file 'errors.py')
#city2 = City('Monogodoobo') #raise CoordinateError, because city name is invalid, metrhod get_cooridantes in init cant upd coordinates.
#city2.name = 'dgf433455345' #raise CityNameError
#city2.get_cooridantes() #raise CoordinateError
#city_weather2 = Weather('Trololo')
#print (city_weather2.watch_weater()) #raise ApiAnswerError with text from API.