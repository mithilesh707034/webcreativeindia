from django.db import models
from tinymce.models import HTMLField
class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    message=models.TextField(default='',null=True,blank=True)
    date=models.DateField(auto_now=True)
    def __str__(self):
        return str(self.name)+" "+str(self.phone)+" "+str(self.date)

class Location(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)


class Service(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)

class Gallery(models.Model):
    id=models.AutoField(primary_key=True)
    image=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    name=models.CharField(max_length=100,default='',null=True,blank=True)
    def __str__(self):
        return str(self.name)

class Blog(models.Model):
    id=models.AutoField(primary_key=True)
    image=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    title=models.CharField(max_length=100)
    description=HTMLField()
    date=models.DateField(auto_now=True)

    def __str__(self):
        return str(self.title)


choice=((0,"Active"),(1,"Done"))
class Ticket(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,default='')
    subject=models.CharField(max_length=100)
    description=HTMLField()
    reply=HTMLField(default='')
    date=models.DateField(auto_now=True)
    status=models.IntegerField(choices=choice,default=0)

    def __str__(self):
        return str(self.subject)

