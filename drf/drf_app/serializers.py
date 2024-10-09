from rest_framework import serializers
# from .models import Person

# class PersonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Person
#         fields = ['name', 'age', 'height']

from django.contrib.auth.models import User
from .models import Snippet

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets', 'owner']