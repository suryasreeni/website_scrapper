from django.db import models

class Links(models.Model):
    def __str__(self):
       return self.stringname
    address=models.CharField(max_length=500,null=True,blank=True)
    stringname=models.CharField(max_length=500,null=True,blank=True)
# Create your models here.
