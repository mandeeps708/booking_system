from django.core.exceptions import ValidationError
from django.db.models import Q
from django import forms
from .models import Booking
from datetime import timedelta
import datetime

class BookingForm(forms.ModelForm):
	# This connects the 'Booking' model with this form and shows the specified fields on the html.
	class Meta:
		model = Booking 
		exclude = ['status', 'email']


	"""
	If the input date is not valid then it will show a validation message.
	The form will also raise a validation error if the start time or the end time of the event is between the timings for 
	already booked or hall to be booked. e.g. If the hall is booked from 8AM to 10AM, then the user can't book the hall 
	from 9AM to 10AM.
	"""
	def clean(self):
		form_data = self.cleaned_data
		event_date = form_data['date']

		if event_date < datetime.date.today():
			raise forms.ValidationError("Invalid Date")

		event_start = form_data['start_time']
		event_end = form_data['end_time']
		# FMP = '%H:%M %p'
		# duration = datetime.strptime(event_end, FMP) - datetime.strptime(event_start, FMP)
		# event_end = (event_start + timedelta(hours = event_hours)).strftime('%H:%M %p')

		if event_start >= event_end:
			raise forms.ValidationError("Timings should be valid")

		event_hall = form_data['hall']
		event_time = Booking.objects.filter(Q(start_time__range = (event_start, event_end)) | \
			Q(end_time__range = (event_start, event_end)) | \
			Q(start_time__lte = event_start, end_time__gte = event_end) | \
			Q(start_time__gte = event_start, end_time__lte = event_end), \
			date = event_date, hall = event_hall)

		for t in event_time:
			if t is not None:
				raise forms.ValidationError("Invalid Time")

		return form_data
