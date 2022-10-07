from django.db import models
from django.contrib.auth.models import User
from subjects.models import Subject


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sID = models.CharField(max_length=10)
    gender = models.CharField(
        max_length=6,
        choices=[('Male', 'Male'), ('Female', 'Female')]
    )

    def __str__(self):
        return f'{self.user.username}'


class Booking(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'Name:{self.username.first_name} Subject {self.subject.subjectCode}'

    

'''from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sID = models.CharField(max_length=10)
    gender = models.CharField(
        max_length=6,
        choices=[('Male', 'Male'), ('Female', 'Female')]
    )
'''

'''class Booking(models.Model):
    user '''
