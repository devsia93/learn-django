from django.db import models
from django.utils.timezone import now


class Airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'City {self.city} : name {self.name}'

    def get_arrivals(self):
        return self.flights_destination.all()

    def get_flight_origin(self):
        return self.flights_origin.get(self.name)


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='flights_origin',
                               verbose_name='Место отбытия', null=True)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='flights_destination',
                                    verbose_name='Место прибытия', null=True)
    duration = models.IntegerField()
    date_pub = models.DateTimeField(verbose_name="Date of publish", default=now)

    def __str__(self):
        return f'From {self.origin.name} to {self.destination.name} : {self.duration} hours'


class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    flights = models.ManyToManyField(Flight, related_name='passengers', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
