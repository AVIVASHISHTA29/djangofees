from django.db import models
from django import forms
from django.conf import settings
# Create your models here.

class Student(models.Model):
    admno = models.CharField(max_length=120,primary_key="True")
    roll = models.CharField(max_length=5,default="")
    class_student = models.CharField(max_length=2,default="")
    section = models.CharField(max_length=1,default="")
    fname = models.CharField(max_length=30,default="")
    lname = models.CharField(max_length=30,default="")
    gender = models.CharField(max_length=6,default="")
    dob = forms.DateField(input_formats = settings.DATE_INPUT_FORMATS)
    category = models.CharField(max_length=120,default="")
    religion = models.CharField(max_length=50,default="")
    caste = models.CharField(max_length=35,default="")
    phno = models.CharField(max_length=10,default="")
    email = models.CharField(max_length=50,default="")
    fathername = models.CharField(max_length=120,default="")
    fatherphone = models.CharField(max_length=10,default="")
    motherphone = models.CharField(max_length=10,default="")
    mothername = models.CharField(max_length=120,default="")
    fatherocc = models.CharField(max_length=120,default="")
    motherocc = models.CharField(max_length=120,default="")
    guardianphone = models.CharField(max_length=10,default="")
    guardianname = models.CharField(max_length=120,default="")
    guardianemail = models.CharField(max_length=120,default="")
    guardianrelation = models.CharField(max_length=30,default="")
    guardianocc = models.CharField(max_length=120,default="")
    guardianadd = models.CharField(max_length=200,default="")

    def __str__(self):
        return self.admno


class FeesType(models.Model):
    feestype = models.CharField(max_length=120,default="")
    class_fees = models.CharField(max_length=120,default="")
    fees_value = models.CharField(max_length=35,default="")

    def __str__(self):
        return self.feestype
