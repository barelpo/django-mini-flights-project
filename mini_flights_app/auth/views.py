from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from mini_flights_app.auth.serializers import SignupSerializer, UserSerializer


class IsStaffPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):

    queryset = User.objects.all()
    serializer_class = SignupSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return UserSerializer
        elif self.action == 'create':
            return super().get_serializer_class()

    def get_permissions(self):
        if self.action == 'list':
            return [IsAuthenticated(), IsStaffPermission()]
        else:
            return []

    def filter_queryset(self, queryset):
        if self.action in ('retrieve', 'list'):
            first_name = None
            last_name = None
            if 'first_name' in self.request.query_params:
                first_name = self.request.query_params['first_name']
            if 'last_name' in self.request.query_params:
                last_name = self.request.query_params['last_name']

            if first_name and last_name:
                queryset = queryset.filter(first_name=first_name, last_name=last_name)
            elif first_name:
                queryset = queryset.filter(first_name=first_name)
            elif last_name:
                queryset = queryset.filter(last_name=last_name)

        return queryset


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    serializer = UserSerializer(instance=request.user)
    return Response(serializer.data)

