from django.db import models

# a file used to create model for the database

class Brand(models.Model):
    name = models.CharField(max_length=200)
    ownersNum = models.IntegerField(default=0)

class Processor(models.Model):
    name = models.CharField(max_length=200)
    ownersNum = models.IntegerField(default=0)

class OS(models.Model):
    ownersNum = models.IntegerField(default=0)

class OSChoice(models.Model):
    os = models.ForeignKey(OS, on_delete=models.CASCADE)
    Osname = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
