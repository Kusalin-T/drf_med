from django.db import models

class MedAdmin(models.Model):
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    nid = models.CharField(max_length=20, default='000000000')              #National ID
    phonenumber = models.CharField(max_length=20, default='0123456789')
    email = models.EmailField(max_length=254, default="mock@gmail.com")