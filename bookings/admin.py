from django.contrib import admin

# Register your models here.
# bookings/admin.py
from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'accommodation', 'check_in_date', 'check_out_date', 'total_price')
    list_filter = ['check_in_date']
    search_fields = ('accommodation__title', 'user__username')

admin.site.register(Booking, BookingAdmin)
