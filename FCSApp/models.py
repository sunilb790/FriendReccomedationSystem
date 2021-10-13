from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    MobileNumber = models.CharField(max_length=10)
    Profile_Photo = models.ImageField(default='NotsetDefaultPicture.jpg', upload_to='profile_pics')
    DateTime=models.DateTimeField(default=timezone.now) #Date once added cannot be changed
    Age = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username

class FriendRelation(models.Model):
    Friend1 = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='Friend1_set')
    Friend2 = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='Friend2_set')
    
    def __str__(self):
        return f'{self.Friend1.user.username} has friendship with {self.Friend2.user.username}'


class Interest(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ManyToManyField(User)
    TRUE_INTEREST = 'YES'
    FALSE_INTEREST = 'NO'
    TRUE_FALSE_IN_INTEREST_CHOICES =[
        (TRUE_INTEREST,'Yes'),
        (FALSE_INTEREST,'No'),
    ]    
    Photography = models.CharField(max_length=10,choices=TRUE_FALSE_IN_INTEREST_CHOICES,default=FALSE_INTEREST)
    Healthansfitness = models.CharField(max_length=10,choices=TRUE_FALSE_IN_INTEREST_CHOICES,default=FALSE_INTEREST)
    Mentorship = models.CharField(max_length=10,choices=TRUE_FALSE_IN_INTEREST_CHOICES,default=FALSE_INTEREST)
    Gardening = models.CharField(max_length=10,choices=TRUE_FALSE_IN_INTEREST_CHOICES,default=FALSE_INTEREST)
    Sports = models.CharField(max_length=10,choices=TRUE_FALSE_IN_INTEREST_CHOICES,default=FALSE_INTEREST)

    def __str__(self):
        return self.title