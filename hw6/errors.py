class UpdError(Exception):
    '''Subclass for except errors in City and Weather Class.'''
    pass


class CoordinateError(UpdError):
        '''Interception of incorrectly entered coordinates.
        
        Returns:
            string: with text error'''
        error_text0 = 'Connection to Server OK but city name is incorrect!'
        
        def __init__(self):
            super().__init__()
            self.msg = self.error_text0

        def __str__(self):
              return self.msg


class CityNameError(UpdError):
        '''Interception of failed connection for weather update.
        
        Returns:
            string: with text error'''
        error_text = 'City name can contains only letters a-z, A-Z.\nTry again.'
        def __init__(self):
            super().__init__()
            self.msg = self.error_text

        def __str__(self):
              return self.msg


class UpdateWeatherError(UpdError):
        '''Interception of failed connection for weather update.
        
        Returns:
            string: with text error'''
        error_text = 'Connection error.\nCheck the url address or parameters (name, coordiantes) in url.'
        def __init__(self):
            super().__init__()
            self.msg = self.error_text

        def __str__(self):
              return self.msg


class ApiAnswerError(UpdError):
        '''Interception of wrong API response from api OpenWeather.
        
        Note: 
            Error text gets from API response. If API respone None returns default text.
        
        Returns:
            string: with text error.'''
        def __init__(self, error_text):
            self.msg = error_text
            if self.msg == '()' or None:
                  error_text = 'Something wrong with url parametrs (self._name, token) or connection to OpenWeather server!'
                  self.msg = error_text
            super().__init__()

        def __str__(self):
              return self.msg