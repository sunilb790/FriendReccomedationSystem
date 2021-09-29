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
        return f'{self.Friend1.user.username} has friendship with {self.Friend1.user.username}'