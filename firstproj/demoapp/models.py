from django.db import models

# Create your models here.  
class Customer(models.Model): 
    name = models.CharField(max_length=255) 

class Vehicle(models.Model): 
    name = models.CharField(max_length=255) 
    customer = models.ForeignKey( 
        Customer, 
        on_delete=models.CASCADE,
    ) 

class Artist(models.Model): 
    name = models.CharField(max_length=10) 

class Album(models.Model): 
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE) 

class Song(models.Model): 
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE) 
    album = models.ForeignKey(Album, on_delete=models.RESTRICT) 


# class Booking(models.Model):
#     first_name = models.CharField(max_length = 200)
#     last_name = models.CharField(max_length = 200)
#     guest_count = models.IntegerField()
#     reservation_time = models.DateField(auto_now=True)
#     comments = models.CharField(max_length = 1000)