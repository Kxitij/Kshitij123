from django.db import models

# Create your models here.
class student(models.Model):
    
    Name = models.CharField('Student name', max_length=25)
    Department = models.CharField('department name', max_length=25)
    Semester = models.CharField(max_length=5)
    Section = models.CharField('Section',max_length=2)
    Contact_no = models.CharField(max_length=11)
    USN = models.CharField(max_length=20, primary_key=True)

class classes(models.Model):
    Semester = models.CharField(max_length=5)
    Section = models.CharField('Section',max_length=2)
    department = models.CharField(max_length=20)
    Class_Code = models.CharField(max_length=25, primary_key=True)
    OOPS_lab = models.CharField(max_length=20)
    DS_lab = models.CharField(max_length=20)
    DBMS_lab = models.CharField(max_length=20)

class Labs(models.Model):
   LAB_CODE = models.CharField(max_length=20,primary_key=True)
   Course_name = models.CharField(max_length=30)
   faculty_name = models.CharField(max_length=30)
   credits = models.IntegerField()
   Hours_per_week = models.IntegerField()

class Attendance(models.Model):
    USN = models.ForeignKey(student, on_delete=models.CASCADE)
    Class_code = models.ForeignKey(classes, on_delete=models.CASCADE)
    OOPS_lab = models.CharField(max_length=20)
    DS_lab = models.CharField(max_length=20)
    DBMS_lab = models.CharField(max_length=20)
    
    



