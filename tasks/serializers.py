from rest_framework import serializers
from .models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'#Coloca todos los campos en una serializacion
        read_only_fields = ('created_date', )