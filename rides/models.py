from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Ride(models.Model):

    class RideGrade(models.TextChoices):
        Grade_1 = '1'
        Grade_2 = '2'
        Grade_3 = '3'
        Grade_4 = '4'
        Grade_5 = '5'


    name = models.CharField(max_length=32)
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.CharField(
        max_length=2, 
        choices=RideGrade.choices, 
        default=RideGrade.Grade_1
    )
    distance = models.IntegerField()
    speed_mph = models.IntegerField(default=15)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    location = models.CharField(max_length=32, null=True)
    cafe_stop = models.BooleanField()
    drop_ride = models.BooleanField()
    text = models.TextField()

    def __str__(self):
        return self.name + ' | ' + str(self.leader)

    def get_absolute_url(self):
        return reverse('ride-details', args=(self.id,))
