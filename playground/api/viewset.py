from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from playground.api import serializers
from playground import models
from playground.models import Person
from django_filters.rest_framework import DjangoFilterBackend


class PersonViewSet(ModelViewSet):
    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sexo']
    queryset = queryset.order_by('idade')

class MeerenWomanlist(generics.ListAPIView):
    serializer_class = serializers.PersonSerializer
    def get_queryset(self):
        return Person.objects.filter(sexo="F", cidade="Meeren")
