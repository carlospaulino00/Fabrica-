from app.models import ToDo
from rest_framework import viewsets
from app.serializers import ToDoSerializers


class ToDoViewSet(viewsets.ModelViewSet):
   
   queryset = ToDo.objects.all()
   serializer_class = ToDoSerializers