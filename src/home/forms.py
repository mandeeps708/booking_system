from django.core.exceptions import ValidationError
# from django.contrib.admin import widgets
from django import forms
from .models import Booking
from datetime import timedelta
import datetime

class BookingForm(forms.ModelForm):
	# This connects the 'Booking' model with this form and shows the specified fields on the html.
	class Meta:
		model = Booking 
		fields = ["hall", "date", "duration", "start_time", "event_name", "name", "email"]

	# With the help of the AdminDateWidget, a calender for the date input can be used.
	# date = forms.DateField(widget=widgets.AdminDateWidget)
	"""
	If the input date is not valid then it will show a validation message
	"""
	def clean_date(self):
		date = self.cleaned_data['date']

		if date < datetime.date.today():
			raise forms.ValidationError("Must be a future date")
		return date

	def clean_time(self):
		data = self.cleaned_data
		event_start = cleaned_data.get('start_time')
		event_hours = cleaned_data.get('duration')
		event_end = ('event_start' + timedelta(hours = 'event_hours')).strftime('%H:%M %p')
		event_hall = cleaned_data.get('hall')
		event_date = cleaned_data.get('date')
		end_time = ('start_time' + timedelta(hours = 'duration')).strftime('%H:%M %p')
		event_time = Booking.objects.filter(hall = event_hall, date = 'event_date', \
			start_time__gte = 'event_start', end_time__lte = 'event_end').values('start_time')

		for t in event_time:
			if t is not None:
				raise forms.ValidationError("Invalid time")

		return data