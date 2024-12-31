from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50, unique=True)
    capacity = models.PositiveIntegerField(help_text="Capacity in kilograms")
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Route(models.Model):
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    distance = models.FloatField(help_text="Distance in kilometers")

    def __str__(self):
        return f"{self.start_location} to {self.end_location}"

class Delivery(models.Model):
    item_name = models.CharField(max_length=200)
    weight = models.FloatField(help_text="Weight in kilograms")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    delivery_date = models.DateField()
    status = models.CharField(
        max_length=50,
        choices=[
            ('Pending', 'Pending'),
            ('In Progress', 'In Progress'),
            ('Delivered', 'Delivered'),
        ],
        default='Pending'
    )

    def __str__(self):
        return self.item_name
