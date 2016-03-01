from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.core.validators import MaxValueValidator


class studentID(models.Model):
	roll_Number = models.IntegerField(validators=[MaxValueValidator(999999)],primary_key = True)
	full_Name = models.CharField(max_length = 20)
	phone_Number = models.BigIntegerField(null = True,validators=[MaxValueValidator(9999999999)])
	email = models.EmailField()
	vote = models.BooleanField(default = False)
	firstSignUp = models.BooleanField(default = True)
	userN = models.CharField(max_length=20,null = True)
	collegeName = models.CharField(max_length = 30,null = True)
	city = models.CharField(max_length=15,null = True)
	state = models.CharField(max_length=20,null = True)

	def __unicode__(self):
		return str(self.roll_Number)

class Candidates(models.Model):
	full_Name =  models.CharField(max_length=20,primary_key = True)
	phone_Number = models.BigIntegerField(null = True,validators = [MaxValueValidator(9999999999)])
	voteCount = models.IntegerField(default = 0)
	description = models.CharField(max_length=400)
	email = models.EmailField()
	collegeName = models.CharField(max_length=30,null = True)

	def __unicode__(self):
		return str(self.full_Name)