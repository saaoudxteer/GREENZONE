# accommodations/admin.py
from django.contrib import admin
from accommodations.models import Accommodation


class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'price_per_night', 'capacity', 'owner')
    list_filter = ('city', 'capacity')
    search_fields = ('title', 'description', 'address', 'city')


admin.site.register(Accommodation, AccommodationAdmin)
