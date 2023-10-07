from django.db import models

class StartUp(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  description = models.TextField()
  domains = models.CharField(max_length=100)
  email = models.EmailField()

class Mentor(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  description = models.TextField()
  domains = models.CharField(max_length=100)
  email = models.EmailField()

class Student(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  description = models.TextField()
  projects = models.TextField(default="None")
  domains = models.CharField(max_length=100)
  email = models.EmailField()