from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
# Create your views here.

def home(request, year=datetime.now().year , month=datetime.now().strftime('%B')):
	# Convert month from name to number
	month = month.capitalize()
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)

	# create a calendar
	cal = HTMLCalendar().formatmonth(
		year,
		month_number)

	# Get datetime
	now = datetime.now()
	current_year = now.year
	time = now.strftime('%I:%M %p')

	return render(request, 'events/home.html', {'cal':cal, 
		'current_year':current_year,
		'current_time': time})