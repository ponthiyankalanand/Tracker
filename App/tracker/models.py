from django.db import models

# Create your models here.
class userAdminDetails(models.Model):
	uname = models.CharField(max_length=100)
	umail = models.EmailField(max_length=100)
	upass = models.CharField(max_length=100)
	userID = models.IntegerField()
	status = models.BooleanField(default=True)
class locationDetails(models.Model):
	longitude = models.FloatField()
	latitude = models.FloatField()
	userID = models.IntegerField()
	count = models.IntegerField()
class userDetails(models.Model):
	uname = models.CharField(max_length=100)
	userID = models.IntegerField()
	status = models.BooleanField(default=True)



