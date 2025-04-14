from django.shortcuts import render

# Create your views here.
# bookings/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime
from decimal import Decimal
from .models import Booking
from accommodations.models import Accommodation

@login_required
def booking_create(request, accommodation_id):
    accommodation = get_object_or_404(Accommodation, pk=accommodation_id)

    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        guests = int(request.POST.get('guests', 1))

        check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
        check_out_date = datetime.strptime(check_out, '%Y-%m-%d').date()

        days = (check_out_date - check_in_date).days
        total_price = accommodation.price_per_night * Decimal(days)

        booking = Booking(
            accommodation=accommodation,
            user=request.user,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            guests=guests,
            total_price=total_price
        )
        booking.save()

        return redirect('booking_confirm', pk=booking.pk)

    return render(request, 'bookings/create.html', {'accommodation': accommodation})

@login_required
def booking_confirm(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)

    if request.method == 'POST':
        booking.status = 'confirmed'
        booking.save()
        return redirect('booking_dashboard')

    return render(request, 'bookings/confirm.html', {'booking': booking})

@login_required
def booking_dashboard(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bookings/dashboard.html', {'bookings': bookings})
