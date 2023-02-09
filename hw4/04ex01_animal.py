class Animal:
    def __repr__(self):
        return f'{self.__class__.__name__}()'


class Human(Animal):
    pass


class Person(Human):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(name={self.name!r})'


# TODO: fill classes above with the required logic
#       to represent human and person (probably with tax number, ...)
# TODO: try to make an Enterprise able to own Pets
# TODO: - add class to represent vaccine
#       - add class to represent generic chip,
#           and separate subclasses for concrete animal ID chips
#       - anything other you want to extend here


class Pet(Animal):
    """Abstracts an animal with an owner and name.

    Each pet is an animal having an owner and a name --
    that is how we model it.
    """

    def __init__(self, owner):
        """Set owner at instantiation."""
        self.change_owner(owner)

    def change_owner(self, new_owner):
        """Called to transfer ownership or set a new owner."""
        self.owner = new_owner

    @property
    def owner(self):
        """Dummy getter for hidden method."""
        return self.__owner

    @owner.setter
    def owner(self, value):
        """This is called when setting owner.

        The difference is that here we can check
        what the user sets owner to. E.g. check
        that owner is not number.

        Called at dog.owner = value
        """
        # do some checks here
        if isinstance(value, Person):
            self.__owner = value
        else:
            err = f'{value!r} must be an instance'
            err += ' or subclass of Person.'
            raise ValueError(err)

    def __repr__(self):
        clsname = self.__class__.__name__
        return f'{clsname}(owner={self.owner!r})'


if __name__ == '__main__':
    ...

