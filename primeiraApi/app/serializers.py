from rest_framework import serializers 
from app.models import ToDo

class ToDoSerializers (serializers.ModelSerializer):
    class Meta:
        model = ToDo
        queryset = ToDo.objects.all()
        fields = ['id', 'atividade', 'status' ]