from django.db import models
from account.models import Teacher
from account.models import Student


# Create your models here.
class Event(models.Model):
    eventid = models.AutoField(primary_key=True)
    eventtitle = models.CharField(max_length=100)
    dateofevent = models.DateField()
    maxparticipants = models.IntegerField(default=1)

    # Reference Teacher from another app
    teacher = models.ManyToManyField('account.Teacher')

    attend = models.ManyToManyField('self', through='AttendEvent')

    def __str__(self):
        return self.eventtitle

class Room(models.Model):
    roomid = models.AutoField(primary_key=True)
    roomname = models.CharField(max_length=50)

    events = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.roomname

class AttendEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    dateregistered = models.DateField()

    def __str__(self):
        return self.student.firstname + ' ' + self.student.lastname + ' - ' + self.event.eventtitle