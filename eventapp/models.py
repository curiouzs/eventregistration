
from django.db import models
from django.contrib import admin
# Create your models here.

class Participant(models.Model):
    name=models.CharField(max_length=20)
    inst=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    contnum=models.CharField(max_length=15)

class ParticipantAdmin(admin.ModelAdmin):
    list_display=("name","inst","email","contnum")