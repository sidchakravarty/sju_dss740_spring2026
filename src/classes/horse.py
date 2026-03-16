# Class         : Horse
# Description   : This class represents a horse with basic attributes and methods. It inherits from the Animal class.
# Author        : Sid Chakravarty
# Date          : 2025-10-30

import animal as Animal

class Horse(Animal.Animal):

    horse_count = 0

    def __init__(self, name: str, is_land_based: bool, age: int, gender: str, breed: str):
        """
        Initializes a new Horse instance.

        Args:
            name (str): The name of the horse.
            is_land_based (bool): Indicates whether the horse is land-based (True) or water-based (False).
            age (int): The age of the horse in years.
            gender (str): The gender of the horse.
            breed (str): The breed of the horse.

        Returns:
            None
        """
        super().__init__(name, is_land_based, age)
        self.gender = gender
        self.breed = breed
        Horse.horse_count += 1

    def __str__(self):
        """
        Returns a string representation of the horse.

        Returns:
            str: A string representation of the horse.
        """
        habitat = "Land" if self.is_land_based else "Water"
        return f"Horse(Name: {self.name}, Habitat: {habitat}, Age: {self.age}, Gender: {self.gender}, Breed: {self.breed})"
    
    @classmethod
    def get_horse_count(cls):
        """
        Returns the total number of Horse instances created.

        Returns:
            int: The total number of Horse instances created.
        """
        return cls.horse_count
    
    @classmethod
    def remove_horse(cls):
        """
        Removes the last Horse instance created.

        Returns:
            None
        """
        if cls.horse_count > 0:
            cls.horse_count -= 1
    
    def gallop(self):
        """
        Returns a string representation of the horse's galloping action.

        Returns:
            str: A string representation of the horse's galloping action.
        """
        return f"{self.name} is galloping!"
    
    def add_birthday(self, year_born, month_born, date_born):
        """
        Adds a birthday to the horse.

        Args:
            year_born (int): The year the horse was born.
            date_born (int): The date the horse was born.
            month_born (int): The month the horse was born.
        
        Returns:
            None
        """
        return super().add_birthday(year_born, date_born, month_born)   

    