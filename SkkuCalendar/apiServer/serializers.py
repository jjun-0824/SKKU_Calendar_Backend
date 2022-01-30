from .models import PostSchedule
from rest_framework import serializers

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostSchedule
        fields = '__all__'