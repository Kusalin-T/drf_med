from django.db import models
from django.contrib.auth.models import User
from meddoctor.models import MedDoctor

class MedPatient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    nid = models.CharField(max_length=20, default='000000000')              #National ID
    phonenumber = models.CharField(max_length=20, default='0123456789')
    email = models.EmailField(max_length=254, default="mock@gmail.com")
    doctor = models.ForeignKey(MedDoctor, on_delete=models.PROTECT)