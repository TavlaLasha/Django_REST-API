from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    pn = models.CharField(max_length=11)
    birthdate = models.DateTimeField()
    gender = models.CharField(max_length=6)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=9, null=True)

    def __str__(self):
        return self.text