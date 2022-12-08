from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from owner.models import Owner
from owner.serializers import OwnerSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer




