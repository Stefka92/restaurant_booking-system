from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation

# Create your views here.

def restaurant_list(request):
    # Retrieve a list of available restaurants
    restaurants = Restaurant.objects.all()
    return render(request, 'booking/restaurant_list.html', {'restaurants': restaurants})

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking:reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'booking/make_reservation.html', {'form': form})

def reservation_success(request):
    return render(request, 'booking/reservation_success.html')