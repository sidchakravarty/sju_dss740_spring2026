# Class         : Dog
# Description   : This class represents a dog with basic attributes and methods. It inherits from the Animal class.
# Author        : Sid Chakravarty
# Date          : 2025-10-30

import animal as Animal

class Dog(Animal.Animal):

    dog_count = 0

    def __init__(self, name: str, is_land_based: bool, age: int, breed: str, color: str):
        """
        Initializes a new Dog instance.

        Args:
            name (str): The name of the dog.
            is_land_based (bool): Indicates whether the dog is land-based (True) or water-based (False).
            age (int): The age of the dog in years.
            breed (str): The breed of the dog.
            color (str): The color of the dog.

            dog_count (int): The total number of Dog instances created.
        
        Returns:
            None
        """
        super().__init__(name, is_land_based, age)
        self.breed = breed
        self.color = color
        Dog.dog_count += 1

    @classmethod
    def get_dog_count(cls):
        """
        Returns the total number of Dog instances created.

        Returns:
            int: The total number of Dog instances created.
        """
        return cls.dog_count
    
    def bark(self):
        """
        Simulates the dog barking.
                
        Returns:
            str: The sound the dog makes.
        """
        return "Woof!"
    
    def play(self):
        """
        Simulates the dog playing.
        
        Returns:
            str: The action the dog is performing.
        """
        return f"{self.name} is playing fetch!"
    
    def sleep(self):
        """
        Simulates the dog sleeping.

        Returns:
            str: The action the dog is performing.
        """
        return f"{self.name} is sleeping in the bed."
    
    def __str__(self):
        """
        Returns a string representation of the Dog instance.

        Returns:
            str: A string representation of the Dog instance.
        """
        habitat = "Land" if self.isLandBased else "Water"
        return f"Dog(Name: {self.name}, Habitat: {habitat}, Age: {self.age}, Breed: {self.breed}, Color: {self.color})"
    
    @classmethod
    def remove_dog(cls):
        """
        Removes the last Dog instance created.

        Returns:
            None
        """
        if cls.dog_count > 0:
            cls.dog_count -= 1


    def add_birthday(self, year_born, month_born, date_born):
        """
        Adds a birthday to the dog's profile.

        Args:
            year_born (int): The year the dog was born.
            month_born (int): The month the dog was born.
            date_born (int): The date the dog was born.

        Returns:
            None
        """
        return super().add_birthday(year_born, month_born, date_born)
