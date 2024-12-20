from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)  # Car make name
    description = models.TextField()  # Description of the car make

    def __str__(self):
        return self.name  # String representation of the CarMake object

# Car Model model
class CarModel(models.Model):
    # Relationship with CarMake (One CarMake can have many CarModels)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()  # Refers to a dealer created in the external database
    name = models.CharField(max_length=100)  # Name of the car model

    # Type of car with limited choices
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CHOICES)

    # Year with a range validator
    year = models.IntegerField(validators=[MinValueValidator(2015), MaxValueValidator(2023)])

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"  # String representation of the CarModel object
