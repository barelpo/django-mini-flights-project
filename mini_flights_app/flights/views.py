import django_filters
from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from mini_flights_app.flights.serializers import FlightsSerializer
from mini_flights_app.models import Flight


class FlightFilterSet(FilterSet):
    number = django_filters.CharFilter(field_name='flight_number', lookup_expr='iexact')
    origin = django_filters.CharFilter(field_name='origin_city', lookup_expr='iexact')
    destination = django_filters.CharFilter(field_name='destination_city', lookup_expr='iexact')

    departure__range = django_filters.DateTimeFromToRangeFilter(
        field_name='date_time_origin',
        label='Departure Date Range'
    )
    arrival__range = django_filters.DateTimeFromToRangeFilter(
        field_name='date_time_destination',
        label='Destination Date Range'
    )

    price_from = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_to = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    canceled = django_filters.BooleanFilter(field_name='is_canceled')
    id = django_filters.NumberFilter(field_name='id', lookup_expr='exact')

    class Meta:
        model = Flight
        fields = ['flight_number']


class IsStaffPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class FlightViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    GenericViewSet):

    queryset = Flight.objects.all()
    serializer_class = FlightsSerializer
    filterset_class = FlightFilterSet
    filter_backends = [DjangoFilterBackend]

    def filter_queryset(self, queryset):

        if self.action == 'retrieve':
            queryset = queryset.filter(id=self.kwargs['pk'])

        queryset = super().filter_queryset(queryset)

        return queryset

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update':
            return [IsAuthenticated(), IsStaffPermission()]
        else:
            return []



