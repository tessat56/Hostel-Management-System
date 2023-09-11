from django.db import models
from django.utils import timezone
from django .contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    stud_id = models.CharField(max_length=10,null=False,blank=False)
    email = models.EmailField()
    mob_no=models.IntegerField(null=True)
    password=models.CharField(max_length=10)
    date_of_birth=models.DateField(null=True)
    users=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.fname



class Warden(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    warden_id = models.CharField(max_length=10,null=False,blank=False)
    email = models.EmailField()
    mob_no=models.IntegerField(null=True)
    password=models.CharField(max_length=10)
    date_of_birth=models.DateField(null=True)
    users=models.OneToOneField(User,on_delete=models.CASCADE)

class Gatepasses(models.Model):
    option=(
        ('1','accepted'),
        ('0','rejected'),
    )
   
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    stud_id=models.CharField(max_length=10,null=False,blank=False)
    date_out=models.DateField(null=True)
    time_out=models.TimeField(null=True)
    reason=models.CharField(max_length=200)
    status=models.CharField(max_length=10)
    warden_approve=models.CharField(max_length=3,choices=option)
    date_in=models.DateField(null=True)
    time_in=models.TimeField(null=True)
    users=models.ForeignKey(Student,on_delete=models.CASCADE)



#tessa-g
class Room(models.Model):
    room_no = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    rent = models.FloatField()
    vacancy = models.PositiveIntegerField()
    
#tessa-g



#tessa-t

class mess(models.Model):
    name=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    payment_id=models.CharField(max_length=100)
    paid=models.BooleanField(default=False)
    # def __str__(self):
    #     return self.name

#tessa-t

#rose

class Messcut(models.Model):
    option=(
        ('1','accepted'),
        ('0','rejected'),
       )
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    stud_id=models.CharField(max_length=10,null=False,blank=False)
    date_from=models.DateField(null=True)
    date_to=models.DateField(null=True)
    reason=models.CharField(max_length=200)
    status=models.CharField(max_length=10)
    warden_approve=models.CharField(max_length=3,choices=option)
    users=models.ForeignKey(Student,on_delete=models.CASCADE)

    #
class Grievances(models.Model):
    stud_id=models.CharField(max_length=10,null=False,blank=False)
    room_no = models.CharField(max_length=10)
    complaint = models.TextField(null=True, blank=True)
    #users=models.ForeignKey(Student,on_delete=models.CASCADE)
    time_in = models.DateTimeField(default=timezone.now)

class Suggestion(models.Model):
    sugg= models.TextField(null=True, blank=True)