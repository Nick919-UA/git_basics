class Animal():
    '''The main class of animals
    
    Parametrs:
        internal_id: internal int parametr, added an id to each animal'
    '''

    internal_id=1000

    def __init__(self):
        '''Method that initializes the Animal class and add id to amimal'''

        self.internal_id = Animal.internal_id
        Animal.internal_id += 10

    def __repr__(self):
        '''repe of the class'''
        
        return f'{self.__class__.__name__}()'


class Human(Animal):
    '''The subclass of Animal class
    
        Parametrs:
            human_list(list): internal list, added  each animal to list'
    '''
    human_list = []

    def __init__(self, age='Unknown'):
        '''Method that initializes the Human class and add age to Human
        
        Parametrs:
            age(str): age of the human
        '''

        self._age = age
        Human.human_list.append(self)
    
    @property
    def age(self):
        '''Method with decorator 'property' for portect varible 'age' to prohibit direct changes.
        
        Returns:
            String value of varible 'age'.
        '''        
        return self._age

    @age.setter
    def age(self, add_age):
        '''Method with decorator 'setter' for change varible 'age'.
        
        Parametrs:
            age(str): age of human

        Returns:
            String value of varible 'age'.
        ''' 
        if isinstance(add_age, str) and len(add_age) > 0:
            self._age = add_age
        else:
            raise ValueError("Age must be a non-empty string")

    @classmethod
    def all_humans(cls):
        '''Method with decorator 'classmethod' for receive all humans in class.

        Returns:
            List of humans.
        '''        
        return cls.human_list


class GenericChip():
    '''Class for install generic chip to animals'''
    def __init__ (self, chip_status):
        self.chipped = chip_status
    
    def chip_install(self, chip_status):
        '''Chip installation method
        
        Parametrs:
            chip_status(bool): True or False
        Returns:
                String for install status'''

        #print (f'Generic Chip install: {chip_status}')
        return f'Generic Chip install: {chip_status}'
    

class Person(Human):
    '''Class of Human. Class ierarchy: Animal > Human > Person'''
    def __init__(self, age='Unknown', name='Unknown', taxnumber='Unknown', chipped=None):
        '''Init of the class
 
        Parametrs:
            age(str): age of person
            name(str): name of person
            taxnumber(int): taxnumber of person
            chipped(bool): status of Generic chip
        '''         
        super().__init__(age)
        self._name = name
        self._taxnumber = taxnumber
        self.__chipped = chipped

    @property
    def name(self):
        '''Method with decorator 'property' for portect varible 'name' to prohibit direct changes.
        
        Returns:
            String value of varible 'name'.
        '''            
        return self._name

    @name.setter
    def name(self, new_name):
        '''Method with decorator 'setter' for change varible 'name'.
        
        Parametrs:
            name(str): name of person

        Returns:
            String value of varible 'name'.
        '''         
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name

        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def taxnumber(self):
        '''Method with decorator 'property' for portect varible 'taxnumber' to prohibit direct changes.
        
        Returns:
            String value of varible 'taxnumber'.
        '''           
        return self._taxnumber

    @taxnumber.setter
    def taxnumber(self, new_tax):
        '''Method with decorator 'setter' for change varible 'taxnumber'.
        
        Parametrs:
            taxnumber(int): taxnumber of person

        Returns:
            Int value of varible 'taxnumber'.
        '''         
        if isinstance(new_tax, int) and len(new_tax) > 0:
            self._taxnumber = new_tax 
        
        else:
            raise ValueError("taxnumber must be a non-empty int")

    @property
    def chipped(self):
        '''Method with decorator 'property' for portect varible 'chipped' to prohibit direct changes.
        
        Returns:
            Bool value of varible 'chipped'.
        '''         
        return self.__chipped

    @chipped.setter
    def install_generic_chip(self, value):
        '''Method with decorator 'setter' for change varible 'chipped'.

        The chip installation request is possible only 1 time. Once a decision is made, it cannot be changed.
        
        Parametrs:
            value(bool): True or False

        Important:
            This parameter can be changed only 1 time.

        Returns:
            String with install status
        '''         
        if self.__chipped is not None:
            #print(f'You can choose installiation of chip only one time.\nChip status {self.chipped}')
            return (f'You can choose installiation of chip only one time.\nChip status {self.chipped}')

        elif value == True:
            self.__chipped = value  
            return GenericChip.chip_install(self, value)

        elif value == False:
            self.__chipped = value
            #print (f'Installiaton chip status:{self.chipped}')  
            return f'Installiaton chip status:{self.chipped}'
        else:
            #print (f'Oops, something wrong! Only bool values supported!')
            return f'Oops, something wrong! Only bool values supported!'
        
    

    def __repr__(self):
        '''repr of the class'''
        cls = self.__class__.__name__
        return (f'\nInternal_id:{Animal().internal_id}\t'
            f'{cls}(age={self.age!r}, '
        f'name={self.name!r}, '
        f'taxnumber={self.taxnumber!r})'
        f'chipped={self.chipped})')

class Pet(Animal):
    '''Class of Pet. Class ierarchy: Animal > Pet'''
    pet_list =[]

    def __init__(self, owner='Unknown', nickname='Unknown', vaccinated=False, pet_chipped=None):
        '''Init of the class
 
        Parametrs:
            owner(str): pet owner
            nickname(str): nickname pet
            vaccinated(bool): vaccine status
            pet_chipped(bool): generic chip install status
        '''        
        self._owner = owner
        self._nickname = nickname
        self.vaccinated = vaccinated
        self.__pet_chipped = pet_chipped
        Pet.pet_list.append(self)
    
    @property
    def owner(self):
        '''Method with decorator 'property' for portect varible 'owner' to prohibit direct changes.
        
        Returns:
            String value of varible 'owner'.
        '''           
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        '''Method with decorator 'setter' for change varible 'owner'.
        
        Parametrs:
            new_owner(str): new_owner name. Only from Person class.

        Returns:
            String value of varible 'new_owner'.
        '''  
        if isinstance(new_owner, Person) or self.owner == 'Unknown':
            self._owner = new_owner
        else:
            err = f'{new_owner!r} must be an instance'
            err += ' or subclass of Person.'
            raise ValueError(err)

    @property
    def nickname(self):
        '''Method with decorator 'property' for portect varible 'nickname' to prohibit direct changes.
        
        Returns:
            String value of varible 'nickname'.
        '''          
        return self._nickname

    @nickname.setter 
    def nickname(self, new_nick):
        '''Method with decorator 'setter' for change varible 'nickname'.
        
        Parametrs:
            new_nick(str): new_nick name.

        Returns:
            String value of varible 'nickname'.
        '''        
        if isinstance (new_nick, str) and len(new_nick) > 0:
            self._nickname = new_nick 
        else:
            raise ValueError("nickname must be a non-empty sting")

    @property
    def vaccinated(self):
        '''Method with decorator 'property' for portect varible 'vaccinated' to prohibit direct changes.
        
        Returns:
            String value of varible 'vaccinated'.
        '''                 
        return (f'Pet {self.nickname}(Owner: {self.owner}). '
            f'Vaccination status: {self._vaccinated}')

    @vaccinated.setter
    def vaccinated(self, status):
        '''Method with decorator 'setter' for change varible 'vaccinated'.
        
        Parametrs:
            vaccinated(bool): True or False

        Returns:
            bool value of varible 'vaccinated'.
        '''          
        if isinstance (status, bool):
            self._vaccinated = status
            return self._vaccinated
        else:
            raise ValueError("Status mast be True or False")

    @property
    def pet_chipped(self):
        '''Method with decorator 'property' for portect varible 'pet_chipped' to prohibit direct changes.
        
        Returns:
            Bool value of varible 'pet_chipped'.
        ''' 
        return self.__pet_chipped

    @pet_chipped.setter
    def install_generic_chip(self, value):
        '''Method with decorator 'setter' for change varible 'pet_chipped'.

        The chip installation request is possible only 1 time. Once a decision is made, it cannot be changed.
        
        Parametrs:
            value(bool): True or False

        Important:
            This parameter can be changed only 1 time.

        Returns:
            String with install status
        '''         
        
        if self.__pet_chipped is not None:
            #print(f'You can choose installiation of chip only one time.\nChip status {self.pet_chipped}')
            return (f'You can choose installiation of chip only one time.\nChip status {self.pet_chipped}')

        elif value == True:
            self.__pet_chipped = value  
            return GenericChip.chip_install(self, value)

        elif value == False:
            self.__pet_chipped = value
            #print (f'Installiaton chip status:{self.pet_chipped}')  
            return f'Installiaton chip status:{self.pet_chipped}'
        else:
            #print (f'Oops, something wrong! Only bool values supported!')
            return f'Oops, something wrong! Only bool values supported!'

    @classmethod
    def all_pets(cls):
        '''Method with decorator 'classmethod' for receive all pets in class.

        Returns:
            List of pets.
        '''      
        return cls.pet_list

    def __repr__(self):
        '''repr of the class'''
        clsname = self.__class__.__name__
        return (f'\nInternal_id: {Animal().internal_id} - \t'
        f'{clsname}(owner={self.owner!r}, '
        f'nickname={self.nickname}, '
        f'vaccinated={self._vaccinated}, '
        f'chipped={self.pet_chipped})')


#for tests Human class
#man = Human()
#print (man.age)
#man.age = '57 years'
#print (man.age)

#for tests Person class
per1 = Person(age='50 years', name='Nick', taxnumber=48473587)
per2 = Person(age='20 years', name='Jo', taxnumber=54654645)
per3 = Person(age='33 years', name='Lili', taxnumber=456546546)

#print (per1)
#print (per1.chipped)
#per1.install_generic_chip = '45454'
#print (per1.chipped)
#per1.install_generic_chip = False
#print (per1.chipped)
#per1.install_generic_chip = True
#print (per1.chipped)
#print(Person().all_humans())

#for tests Pet class
cat1 = Pet(per1.name, 'Kotti')
cat2 = Pet(per1.name, 'Diggi')
cat3 = Pet(per1.name, 'Smitty')
#print(cat2)
#print(cat1)

#cat3.vaccinated = True
#print(cat3)

#print (cat1)
#print (cat1.pet_chipped)
#cat1.install_generic_chip = '45454'
#print (cat1.pet_chipped)
#cat1.install_generic_chip = True
#print (cat1.pet_chipped)
#cat1.install_generic_chip = False
#print (cat1.pet_chipped)

#print(Pet().all_pets())

#cat1.vaccinated = True

#print(cat1)
#cat1.owner = per
#print(cat1)
#print(cat1.install_generic_chip(True))