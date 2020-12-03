from django.contrib import admin


from .models import *


class FlightAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'duration')
    list_display_links = ('origin', 'destination')
    search_fields = ('origin', 'destination', 'duration')


class FlightInline(admin.TabularInline):
    model = Flight
    extra = 3
    fk_name = "origin"


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    # fields = ('city', )
    list_display_links = ('name', 'city')
    search_fields = ('name', 'city')
    inlines = (FlightInline, )


admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger)
# admin.site.register(Airport, AirportAdmin)
