from rest_framework.serializers import ModelSerializer

from mini_flights_app.models import Flight


class FlightsSerializer(ModelSerializer):

    class Meta:
        model = Flight
        fields = '__all__'
        