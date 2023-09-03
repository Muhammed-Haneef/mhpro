from django.db import models

# Create your models here.
class contactdb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email_Id=models.EmailField(max_length=100,null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=200,null=True,blank=True)

class Applicantdb(models.Model):
    Firstname=models.CharField(max_length=100,null=True,blank=True)
    Lastname=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Position=models.CharField(max_length=100,null=True,blank=True)
    Resume=models.FileField(upload_to='resumes')

class newsletterdb(models.Model):
    email=models.EmailField(max_length=100,null=True,blank=True)
