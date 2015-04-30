from django.contrib import admin
from .models import Booking, Hall, Feedback

class BookingAdmin(admin.ModelAdmin):
	list_display = ['hall', 'name', 'event_name', 'date', 'start_time', 'end_time', 'email', 'status']
	class Meta:
		model = Booking

admin.site.register(Booking, BookingAdmin)

class HallAdmin(admin.ModelAdmin):
	list_display = ['hall', 'seats']
	class Meta:
		model = Hall

admin.site.register(Hall, HallAdmin)

class FeedbackAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'feedback']
	class Meta:
		model = Feedback

admin.site.register(Feedback, FeedbackAdmin)