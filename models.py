from django.db import models

# Create your models here.
class Bank(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    phone=models.BigIntegerField()
    addhar=models.BigIntegerField()
    email=models.EmailField(max_length=50)
    dob=models.DateField()
    mbalance=models.IntegerField()
    photo=models.ImageField(upload_to='images/')
    pwd=models.CharField(max_length=25,null=True)


