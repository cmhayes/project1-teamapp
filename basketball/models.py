from django.db import models

# Create your models here.

class Team(models.Model):
	name = models.CharField(unique=False, max_length=50)
	season = models.CharField(unique=True, max_length=12)
	acc_record = models.CharField(unique=True, max_length=10)
	overall_record = models.CharField(unique=False, max_length=10)
	ranking = models.CharField(unique=False, max_length=3)
	
	def __unicode__(self):
		return U'%s %s %s %s' %(self.name, self.ranking, self.season, self.overall_record)

class Player(models.Model):
	name = models.CharField(unique=False, max_length=25)
	number = models.CharField(unique=True, max_length=3)
	position = models.CharField(unique=False, max_length=25)
	# height =
	# weight = 
	# year = 
	# hometown = 
	# high_school = 
	# major = 