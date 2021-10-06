from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


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

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)

