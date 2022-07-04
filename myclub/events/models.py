from django.db import models

# Create your models here.

class Venue(models.Model):
	name = models.CharField('Venue Name', max_length=250)
	address = models.CharField(max_length=500)
	zip_code = models.CharField('Zip Code',max_length=20)
	phone = models.CharField('Contact Phone',max_length=15)
	web = models.URLField('Website Address')
	email_address = models.EmailField('Email Address')

	def __str__(self):
		return self.name

class MyClubUser(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField('User Email')

	def __str__(self):
		return self.first_name + ' ' + self.last_name

class Event(models.Model):
	name = models.CharField('Event Name',max_length = 250)
	event_date = models.DateTimeField('Event Date')
	venue = models.ForeignKey(Venue, blank=True, null=True, on_delete = models.CASCADE)
	manager = models.CharField(max_length = 100)
	description = models.TextField(blank = True)
	attendees = models.ManyToManyField(MyClubUser, blank=True)

	def __str__(self):
		return self.name