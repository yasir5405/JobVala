from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
class Cate(models.Model):
    
    role = models.CharField(max_length=122)
    location = models.CharField(max_length=122)
    salary = models.CharField(max_length=122)
    link = models.CharField(max_length=500)
    company = models.CharField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.role