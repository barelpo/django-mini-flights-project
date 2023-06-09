# Generated by Django 4.2 on 2023-06-05 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_flights_app', '0005_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='available_seats',
            field=models.IntegerField(db_column='available seats on flight'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='date_time_destination',
            field=models.DateTimeField(blank=True, db_column='destination date and time', null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='date_time_origin',
            field=models.DateTimeField(blank=True, db_column='origin date and time', null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='price',
            field=models.FloatField(db_column='ticket price'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='total_seats_num',
            field=models.IntegerField(db_column='seats on flight'),
        ),
    ]
