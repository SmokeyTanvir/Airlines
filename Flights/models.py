from django.db import models

# Create your models here.
class Airport(models.Model):
    name = models.CharField(max_length=100, null=False)
    code = models.CharField(max_length=5, null=False)
    city = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"{self.name}: {self.code}"    
    
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    estimatedDuration = models.IntegerField()
    departureTime = models.DateTimeField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    profileImage = models.ImageField(upload_to='profile_pictures', blank=True)
    firstName = models.CharField(max_length=100, null=False)
    lastName = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()
    genderChoices = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=genderChoices)
    email = models.EmailField(max_length=100)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.firstName}"

class Thumbnail(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='thumbnails', blank=True)

    def __str__(self):
        return f"{self.name}"