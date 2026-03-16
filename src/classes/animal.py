# Class         : Animal
# Description   : This class represents an animal with basic attributes and methods.
# Author        : Sid Chakravarty
# Date          : 2025-10-30

import datetime

class Animal:

    animal_count = 0

    def __init__(self, name: str, isLandBased: bool, age: int):
        """
        Constructor: Initializes a new Animal instance.

        Args:
            name (str): The name of the animal.
            isLandBased (bool): Indicates whether the animal is land-based (True) or water-based (False).
            age (int): The age of the animal in years.

        Returns:
            None
        """
        self.name = name
        self.isLandBased = isLandBased
        self.age = age
        Animal.animal_count += 1

    def __str__(self):
        """
        Returns a string representation of the Animal instance.

        Returns:
            str: A string representation of the Animal instance.            
        """
        habitat = "Land" if self.isLandBased else "Water"
        return f"Animal(Name: {self.name}, Habitat: {habitat}, Age: {self.age})"
    
    @classmethod
    def remove_animal(cls):
        """
        Removes the last Animal instance created.

        Returns:
            None
        """
        if Animal.animal_count > 0:
            Animal.animal_count -= 1

    @classmethod
    def get_animal_count(cls):
        """
        Returns the total number of Animal instances created.

        Returns:
            int: The total number of Animal instances created.
        """

        return cls.animal_count
    
    def is_adult(self):
        """
        Checks if the animal is an adult.

        Returns:
            bool: True if the animal is an adult (age >= 3), False otherwise.   
        """
        return self.age >= 3
    
    def add_birthday(self, year_born: int, month_born: int, date_born: int):
        """
        Adds a birthday to the animal's profile.

        Args:
            year_born (int): The year the animal was born.
            date_born (int): The day the animal was born.
            month_born (int): The month the animal was born.

        Returns:
            None
        """
        self.date_of_birth = datetime.date(year_born, month_born, date_born)

    def get_birthday(self):
        """
        Retrieves the animal's birthday.

        Returns:
            datetime.date: The date of birth of the animal.
        """
        return self.date_of_birth