from django.db import models
from django.db.models import CASCADE

class Cordinator(models.Model):
    name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Stream(models.Model):
    name = models.CharField(max_length=20)
    cordinator = models.OneToOneField(Cordinator, on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.name


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    dob = models.DateField()
    email = models.EmailField()
    reg_no = models.CharField(max_length=30, default='123')
    stream = models.ForeignKey(Stream, on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=255)
    club_email = models.EmailField()
    student = models.ManyToManyField(Student, related_name='student_club')
