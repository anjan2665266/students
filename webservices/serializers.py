# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from webservices.models import *

class MarksSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Group model """
    class Meta:
        model = Marks
        fields='__all__'

