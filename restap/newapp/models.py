from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50,blank=True)
    age=models.IntegerField(default=0)


class StudentData(models.Model):
    section=models.CharField(max_length=50)
    StudentInfo=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='StudentInfo')



class Emp(models.Model):
    name=models.CharField(max_length=50,blank=True)
    image=models.ImageField(upload_to='images/')