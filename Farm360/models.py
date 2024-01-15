from django.db import models
from django.contrib.auth.models import User




class Event(models.Model):
    """
    Model to represent an event.

    Attributes:
        user (User): The user associated with the event.
        title (str): The title of the event.
        start_date (datetime): The start date and time of the event.
        end_date (datetime): The end date and time of the event.
        description (str): A text description of the event.
        occurrence_rate (OccurrenceRate): The occurrence rate settings for the event.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title
        


class Livestock(models.Model):
    STATUS_CHOICES = [
        ('alive', 'Alive'),
        ('sold', 'Sold'),
        ('slaughtered', 'Slaughtered'),
    ]

    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    livestock_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    identification_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='alive')
    physical_characteristics = models.TextField()
    birth_date = models.DateField()
    vet_contacts = models.TextField()

    def __str__(self):
        return self.name
    


class Resource(models.Model):
    RESOURCE_TYPES = [
        ('equipment', 'Equipment'),
        ('warehouse', 'Warehouse'),
        ('inventory', 'Inventory'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
