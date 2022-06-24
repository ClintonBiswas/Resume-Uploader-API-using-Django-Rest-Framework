from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','name','email', 'location', 'dob', 'gender', 'state', 'pimage', 'rdoc',]

    