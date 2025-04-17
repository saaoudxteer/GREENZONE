from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Booking
from accommodations.models import Accommodation

@login_required
def booking_create(request, accommodation_id):
    accommodation = get_object_or_404(Accommodation, pk=accommodation_id)

    if request.method == 'POST':
        in_date = request.POST['check_in']
        out_date = request.POST['check_out']
        guests = int(request.POST['guests'])

        in_date = datetime.strptime(in_date, '%Y-%m-%d').date()
        out_date = datetime.strptime(out_date, '%Y-%m-%d').date()
        nights = (out_date - in_date).days
        total = accommodation.price_per_night * nights

        booking = Booking.objects.create(
            accommodation=accommodation,
            user=request.user,
            check_in_date=in_date,
            check_out_date=out_date,
            guests=guests,
            total_price=total
        )

        return redirect('booking_confirm', pk=booking.pk)

    return render(request, 'bookings/create.html', {
        'accommodation': accommodation,
        'range': range(1, accommodation.capacity + 1)
    })


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
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/dashboard.html', {'bookings': bookings})
