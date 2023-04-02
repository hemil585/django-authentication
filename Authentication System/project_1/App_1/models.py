from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.TextField(max_length=122)
    message = models.TextField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name

class Signup(models.Model):
    signupemail = models.CharField(max_length=100)
    signuppassword = models.CharField(max_length=100)

    def __str__(self):
        return self.signupemail

