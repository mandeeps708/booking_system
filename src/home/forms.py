from django.core.exceptions import ValidationError
from django.contrib.admin import widgets
from django import forms
from .models import Booking
from home.time_choices import TIME_CHOICES
import datetime

class BookingForm(forms.ModelForm):
	# This connects the 'Booking' model with this form and shows the specified fields on the html.
	class Meta:
		model = Booking 
		fields = ["hall", "date", "start_time", "no_of_hours", "event_name", "name", "email"]
	
	# With the help of the AdminDateWidget, a calender for the date input can be used.
	date = forms.DateField(widget=widgets.AdminDateWidget)
	
	def clean_date(self):
		date = self.cleaned_data['date']

		if date < datetime.date.today():
			raise forms.ValidationError("Must be a future date")
		return date

