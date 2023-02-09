class Galaxy():
    '''This is galaxy class'''
    
    def __init__(self, galaxyname):
        '''Method that initializes the Galaxy class.

        Parameters:
            galaxyname (str): The name of the galaxy.
        '''        
        self.set_galaxyname(galaxyname)

    def set_galaxyname(self, new_galaxyname):
        '''Method for change galaxy name.

        Parameters:
            new_galaxyname (str): The new name of the galaxy.
        
        Returns:
            String with new galaxy name.
        '''        
        self.__galaxyname =  new_galaxyname
        return f'Name has been changed to {self.galaxyname}'

    @property
    def galaxyname(self):
        '''Method with decorator 'property' for portect varible 'galaxyname' to prohibit direct changes.
        
        Returns:
            String value of varible 'galaxyname'.
            '''
            
        return self.__galaxyname

    def __str__(self):
        '''Method that return ifnormation about object in class.

        Returns:
            Name of class and value of parametr 'galaxyname'.
        '''           
        return f'This is {self.__class__.__name__} class\n'\
               f'The name of galaxy: {self.galaxyname}'
    
    def __repr__(self):
        '''Method that return representation of class.

        Returns:
            String with the class name and parameters.
        '''  
        return (f'{self.__class__.__name__}('
                f'{self.galaxyname!r})')

class PlanetarySytem(Galaxy):
    '''This is Solar System class
    
    Class ierarhy: Galaxy > PlanetarySytem'''
    
    def __init__(self, galaxyname, system_name, name_of_star, id_object):
        '''Method that initializes the PlanetarySytem class.

        Parameters:
            galaxyname (str): The name of the galaxy.
            system_name (str): The name of the planetary system.
            name_of_star (str): The name of the main star of system.
            id_object (str): Object id.
        '''     

        super().__init__(galaxyname)
        self.name_of_star = name_of_star
        self.system_name = system_name
        self.set_id_object(id_object)

    def set_id_object(self, new_id):
        '''Method for change id of object.

        Parameters:
            new_id (str): The new id of object.
        
        Returns:
            String with new id of object.
        '''         
        self.__id_object = new_id
        return f'The new id of object is: {self.id_object}'

    @property
    def id_object(self):
        '''Method with decorator 'property' for portect varible 'galaxyname' to prohibit direct changes.
        
        Returns:
            String value of varible 'galaxyname'.
        '''

        return self.__id_object

    def __str__(self):
        return f'The main class is: {Galaxy.__name__}\n'\
               f'The name of galaxy: {self.galaxyname}\n'\
               f'The name of system: {self.system_name}\n'\
               f'The name of star: {self.name_of_star}\n'\
               f'The id of object: {self.id_object}\n'\

    def __repr__(self):
        '''Method that return representation of class.

        Returns:
            String with the class name and parameters.
        ''' 

        return (f'{self.__class__.__name__}('
               f'{self.galaxyname!r},'
               f'{self.system_name!r},'
               f'{self.name_of_star!r},'
               f'{self.id_object!r})')

class SpaceObject(PlanetarySytem):
    '''This is SpaceObject class
    
    Class ierarhy: Galaxy > PlanetarySytem > SpaceObject'''

    def __init__(self, galaxyname, system_name, name_of_star, id_object, object_type, object_name, mass, radius, atmosphere):
        '''Method that initializes the PlanetarySytem class.

        Parameters:
            galaxyname (str): The name of the galaxy.
            system_name (str): The name of the planetary system.
            name_of_star (str): The name of the main star of system.
            id_object (str): Object id.
            object_type (str): type of object(Planets, Satellites, Comets etc).
            object_name (str): The name of object.
            mass (int, float): The mass of object in kg.
            radius (int, float): The radius of object in km.
            atmosphere (str): The type of atmosphere on object.
        ''' 

        super().__init__(galaxyname, system_name, name_of_star, id_object)
        self.object_type = object_type
        self.object_nyme = object_name
        self.object_mass = mass
        self.object_radius = radius
        self.object_atmosphere = atmosphere

    def gravity_calc(self):
        '''Gravity calculator for space objects
       
       This method calculates the gravity of a object using the formula: g = G * M / r^2.
       where g is the surface gravity, G is the gravitational constant, M is the mass of the planet, and r is the radius of the planet.
       
       Returns:
            String with gravity in ms^2.
       '''

        try:
            g = 6.67430 * (10**-11)
            self.object_mass
            return f'The gravity of a object is {round(g * float(self.object_mass) / (float(self.object_radius) ** 2), 2)} ms^2'

        except Exception as ex:
            return (f'{ex}\n',
            f'Ops, Something Wrong! Watch message above')

    def check_life(self):
        '''Method check is there a life on object
        
        Returns:
            String with information about life in the object'''

        if self.object_atmosphere == 'Oxygen':
            return f'There is life on the object {self.object_type} {self.object_nyme}'
        else:
            return f'There NO life on the object {self.object_type} {self.object_nyme}'

    def __str__(self):

        return f'Class ierarhy: {Galaxy.__name__} > {PlanetarySytem.__name__} > {self.__class__.__name__}\n'\
               f'{super().__str__()}\n'\
               f'The type of object: {self.object_type}\n'\
               f'The name of object: {self.object_nyme}\n'\
               f'The mass of object: {self.object_mass}\n'\
               f'The atmosphere in the object: {self.object_atmosphere}\n'

    def __repr__(self):
        '''Method that return representation of class.

        Returns:
            String with the class name and parameters.
        ''' 

        return (f'{self.__class__.__name__}('
            f'{self.galaxyname!r},'
            f'{self.system_name!r},'
            f'{self.name_of_star!r},'
            f'{self.id_object!r},'
            f'{self.object_type!r},'
            f'{self.object_nyme!r},'
            f'{self.object_mass!r},'
            f'{self.object_radius!r},'
            f'{self.object_atmosphere!r})')


# For tests Galaxy class
#gal = Galaxy('MilkyWay')
#print (gal)
#print (gal.__repr__())

# For tests PlanetarySystem class
#sol = PlanetarySytem('MilkyWay', 'Sun', '57584x1')
#print (sol.__repr__())
#print(sol)

# For tests SpaceObject class
sps = (SpaceObject('MilkyWay', 'Solar System', 'Sun', '57584x1', 'star', 'Sun', 1.989e30, 696340, 'plasma'))
sps2 = (SpaceObject('MilkyWay', 'Solar System', 'Sun', '344x1', 'planet', 'Earch', 5.97e24, 6378.1, 'Oxygen'))
sps3 = (SpaceObject('MilkyWay', 'Solar System', 'Sun', '9585x2', 'planet', 'Neptune', 1.02e26, 24764,'Hydrogen'))
sps4 = (SpaceObject('MilkyWay', 'Solar System', 'Sun', '9585x2', 'Satellite', 'Moon', 7.34e22, 1737.4, 'None'))

help(sps)

#print (sps2)
#print (sps.__repr__())
#print (sps.__str__())

# For tests 'gravity_calc' method of SpaceObject class
#print(sps2.gravity_calc())

# For tests 'set_galaxyname' method of Galaxy class that we have access with super(). function
#print(sps2.galaxyname)
#print(sps2.set_galaxyname('Alpha Centavra'))
#print(sps2.galaxyname)

# For tests 'set_id_object' method of PlanetarySytem class that we have access with super(). function
#print(sps3.id_object)
#print(sps3.set_id_object('4894x35443'))
#print(sps3.id_object)

# For tests 'check_life' method of SpaceObject class
#print(sps.check_life())
#print(sps2.check_life())