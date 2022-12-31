from django.db import models

# Create your models here.

class MyImage(models.Model):
		
		imgName=models.CharField(max_length=100)
		mainImg=models.ImageField(upload_to='uploads')
		
		
		

