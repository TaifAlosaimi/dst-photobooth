
# Create your views here.
from django.shortcuts import redirect, render

from .forms import BookingForm



def home(request):
    return render(request, "bookings/home.html")

def about(request):
    return render(request, "bookings/about.html")

def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("booking_success")

    else:
        form = BookingForm()

    return render(request, "bookings/booking.html", {"form": form})


def booking_success(request):
    return render(request, "bookings/booking_success.html")