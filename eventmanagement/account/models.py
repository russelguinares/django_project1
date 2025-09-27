from django.db import models

# Create your models here.
class User(models.Model):
    user_type = (('S', 'Student'), ('T', 'Teacher'))
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=user_type, default='S')

    def __str__(self):
        return self.firstname + ' ' + self.middlename + ' ' + self.lastname

class Student(User):
    course = models.CharField(max_length=50)
    year = models.IntegerField(default=1)
    department = models.CharField(max_length=50)

class Teacher(User):
    specialization = models.CharField(max_length=50)
    age = models.IntegerField(default=1)