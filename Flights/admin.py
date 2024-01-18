from django.contrib import admin
from . import models 

class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin', 'destination', 'estimatedDuration', 'departureTime')
    
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'age', 'gender', 'email')    
    filter_horizontal = ('flights',)

# Register your models here.
admin.site.register(models.Airport)
admin.site.register(models.Flight, FlightAdmin)
admin.site.register(models.Passenger, PassengerAdmin)
admin.site.register(models.Thumbnail)