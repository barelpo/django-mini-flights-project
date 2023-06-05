# Generated by Django 4.2 on 2023-06-01 14:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mini_flights_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats_num', models.IntegerField(db_column='seats_num', max_length=128)),
                ('order_date', models.DateField(db_column='ordr date')),
                ('total_price', models.FloatField(max_length=128)),
            ],
            options={
                'db_table': 'Orders',
            },
        ),
        migrations.AddField(
            model_name='flight',
            name='available_seats',
            field=models.IntegerField(db_column='available seats on flight', default=0, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='date_time_destination',
            field=models.DateTimeField(db_column='destination date and time', default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='date_time_origin',
            field=models.DateTimeField(db_column='origin date and time', default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='is_canceled',
            field=models.BooleanField(db_column='is canceled', default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='price',
            field=models.FloatField(db_column='ticket price', default=0, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='total_seats_num',
            field=models.IntegerField(db_column='seats on flight', default=0, max_length=128),
            preserve_default=False,
        ),
    ]
