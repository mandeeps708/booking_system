from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .forms import BookingForm, ViewBookingsForm
from .models import Booking
from django.core.mail import EmailMessage
from datetime import timedelta

"""
This will open the home page if the user is already loggedin otherwise it will rediect to the login page.
"""
@login_required
def home(request):
		return render(request, "home/home.html", {})

"""
View for 'click to book' page. If there is no errors in the form then it will be saved and a thanks page will be 
displayed and a email alert will be send to the admin as well as the user's emailID.
"""
@login_required
def book(request):
	if request.method == 'POST':
		form = BookingForm(request.POST)
		name = request.POST['name']
		email = request.user.email
		print email	

		if form.is_valid():
			value = form.save(commit=False)
			user = User.objects.all()
			value.email = request.user.email
			value.save()
			# user_email = EmailMessage('Booking System', 'Hi ' + name + ', Thanks for booking :)', to=[email])
			# user_email.send()
			return render(request, "home/thanks.html", {})
	else:
		form = BookingForm()
	return render(request, "home/book.html", {"form": form})
	# alternative of context, locals()


""" 
This view is linked with the "View bookings" page and it will return only those bookings whose status is true set
(finalized) by the admin.
"""
@login_required
def view(request):
	if request.method == 'POST':
		form = ViewBookingsForm(request.POST)
		view_hall = request.POST['hall']
		view_date = request.POST['date']
		if form.is_valid():
			boo = Booking.objects.filter(status = 1, hall = view_hall, date = view_date)
			return render(request, "home/view_booking.html", {"booking": boo})
	else:
		form = ViewBookingsForm()
	return render(request, "home/view.html", {"form": form})

"""
This view will list the booking made by loggedin user such that the user can send a cancellation request to admin for 
the event selected by user.
"""
@login_required
def cancel(request):
		can = Booking.objects.filter(status=1)
		return render(request, "home/cancel.html", {'cancel': can})


"""
The Logout button calls this view and it will return back to the default login page.
"""
def logout_view(request):
		from django.contrib.auth.views import logout
 		logout(request)
		return HttpResponseRedirect(reverse("home.views.home"))
		# return render(request, "registration/logout.html")
