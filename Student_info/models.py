from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.core.validators import MaxValueValidator


######################################################################################################################

COMP = 'COMP'
ENTC = 'ENTC'
MECH = 'MECH'
CIVIL = 'CIVIL'
BIOT = 'BIOT'
IT = 'IT'
CHEM = 'CHEM'
PROD = 'PROD'
ELEC = 'ELEC'
Teacher = 'Teacher'
BE 	= 'BE'
NONE = "None of the above"

depChoices = (

	(COMP,'computer'),
	(ENTC,'electronics & tele'),
	(MECH,'mechanical'),
	(CIVIL,'civil engineering'),
	(BIOT,'biotech'),
	(IT,'information tech.'),
	(CHEM,'chemical engineering'),
	(PROD,'production'),
	(ELEC,'electrical engineering'),

	)

getType = (
		(Teacher,"Teacher"),
		(BE,"BE"),
		(NONE,"None of the above"),
	)


######################################################################################################################



def generateCollege():

	coll = Colleges.objects.all()
	
	choiceInput = []

	newList=()

	for each in coll:
		newList = (str(each),str(each))

		choiceInput.append(newList)
		

	return choiceInput



######################################################################################################################

class Colleges(models.Model):
	collegeName = models.CharField(max_length=30,primary_key=True)
	number_of_departments = models.IntegerField(null = True,validators = [MaxValueValidator(20)])
	contact_number = models.BigIntegerField(null = True,validators = [MaxValueValidator(9999999999)])
	email = models.EmailField()

	def __unicode__(self):
		return str(self.collegeName)



######################################################################################################################

class studentID(models.Model):

	choiceInput = generateCollege()

	roll_Number = models.IntegerField(validators=[MaxValueValidator(999999)],primary_key = True)
	full_Name = models.CharField(max_length = 20)
	phone_Number = models.BigIntegerField(null = True,validators=[MaxValueValidator(9999999999)])
	email = models.EmailField()
	vote = models.BooleanField(default = False)
	firstSignUp = models.BooleanField(default = True)
	userN = models.CharField(max_length=20,null = True)
	collegeName = models.CharField(max_length = 30,null = True,choices = choiceInput)
	department = models.CharField(max_length=30,null=True,choices = depChoices)
	city = models.CharField(max_length=15,null = True)
	state = models.CharField(max_length=20,null = True)
	userType = models.CharField(max_length=10,null=True,choices = getType)


	def __unicode__(self):
		return str(self.roll_Number)


######################################################################################################################

class Candidates(models.Model):

	choiceInput = generateCollege()

	full_Name 	=  models.CharField(max_length=20,primary_key = True)
	phone_Number = models.BigIntegerField(null = True,validators = [MaxValueValidator(9999999999)])
	voteCount = models.IntegerField(default = 0)
	teacherVote = models.IntegerField(default = 0,null = True)
	seniorsVote = models.IntegerField(default = 0,null = True)
	description = models.CharField(max_length=400)
	email = models.EmailField()
	department = models.CharField(max_length=30,null=True,choices = depChoices)
	collegeName = models.CharField(max_length=30,null = True,choices = choiceInput)

	def __unicode__(self):
		return str(self.full_Name)

######################################################################################################################