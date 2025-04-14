
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Accommodation
from bookings.models import Booking
from datetime import datetime

from django.shortcuts import render

def accommodation_list(request):
    accommodations = Accommodation.objects.all()
    return render(request, 'accommodations/list.html', {'accommodations': accommodations})
def accommodation_detail(request, pk):
    accommodation = get_object_or_404(Accommodation, pk=pk)
    return render(request, 'accommodations/detail.html', {'accommodation': accommodation})

def accommodation_search(request):
    city = request.GET.get('city', '')
    check_in = request.GET.get('check_in', '')
    check_out = request.GET.get('check_out', '')
    
    accommodations = Accommodation.objects.all()
    
    if city:
        accommodations = accommodations.filter(city__icontains=city)
    
    if check_in and check_out:
        try:
            check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
            check_out_date = datetime.strptime(check_out, '%Y-%m-%d').date()
            
            booked_accommodations = Booking.objects.filter(
                check_in_date__lte=check_out_date,
                check_out_date__gte=check_in_date,
                status='confirmed'
            ).values_list('accommodation_id', flat=True)
            
            accommodations = accommodations.exclude(id__in=booked_accommodations)
        except ValueError:
            pass
    
    return render(request, 'accommodations/search.html', {
        'accommodations': accommodations,
        'city': city,
        'check_in': check_in,
        'check_out': check_out,
    })
