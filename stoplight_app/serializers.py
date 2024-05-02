from rest_framework import serializers
from .models import ReformArea, Reform, State, ReformStatus

from rest_framework import serializers
from .models import ReformArea, Reform, State, ReformStatus

# Make sure you have the ReformAreaSerializer defined
class ReformAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReformArea
        fields = ['id', 'name']  # Include any other fields you want to expose

class ReformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reform
        fields = ['slcid', 'name', 'description', 'criteria', 'reform_area']
        extra_kwargs = {
            'description': {'required': False},
            'criteria': {'required': False}
        }

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class ReformStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReformStatus
        fields = '__all__'
