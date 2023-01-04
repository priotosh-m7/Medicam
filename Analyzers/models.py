import calendar
import datetime
import time

from django.db import models
import random
# Create your models here.
class UploadImage(models.Model):
    no = int(random.randint(1,999999))
    user = models.CharField('username',max_length=200)
    image = models.ImageField(null=True,blank=True,upload_to='images/brain_tumor_scans/')

    def __str__(self) :
        return self.user

class UploadChestImage(models.Model):
    now = int(random.randint(1,999999))
    user = models.CharField('username',max_length=200)
    image = models.ImageField(null=True,blank=True,upload_to='images/chest_xray/')

    def __str__(self) :
        return self.user

class UploadKidneyImage(models.Model):
    now = int(random.randint(1,999999))
    user = models.CharField('username',max_length=200)
    image = models.ImageField(null=True,blank=True,upload_to='images/kidney_scans/')

    def __str__(self) :
        return self.user