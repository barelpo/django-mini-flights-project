from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Flight(models.Model):

    flight_number = models.CharField(max_length=128, db_column="flight number", null=False, blank=False)
    origin_country = models.CharField(max_length=128, db_column="origin country", null=False, blank=False)
    origin_city = models.CharField(max_length=128, db_column="origin city", null=False, blank=False)
    origin_airport_code = models.CharField(max_length=128, db_column="origin airport code", null=False, blank=False)
    destination_country = models.CharField(max_length=128, db_column="destination country", null=False, blank=False)
    destination_city = models.CharField(max_length=128, db_column="destination_city", null=False, blank=False)
    destination_airport_code = models.CharField(max_length=128, db_column="destination airport code", null=False, blank=False)
    date_time_origin = models.DateTimeField(db_column="origin date and time", null=False, blank=False)
    date_time_destination = models.DateTimeField(db_column="destination date and time", null=False, blank=False)
    total_seats_num = models.IntegerField(max_length=128, db_column="seats on flight", null=False, blank=False)
    available_seats = models.IntegerField(max_length=128, db_column="available seats on flight", null=False, blank=False)
    is_canceled = models.BooleanField(db_column="is canceled", null=False, blank=False)
    price = models.FloatField(max_length=128, db_column="ticket price", null=False, blank=False)

    class Meta:
        db_table = 'flights'


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)
    seats_num = models.IntegerField(max_length=128, db_column="seats_num", null=False, blank=False)
    order_date = models.DateField(db_column="order date", null=False, blank=False)
    total_price = models.FloatField(max_length=128, null=False, blank=False)

    class Meta:
        db_table = 'Orders'
