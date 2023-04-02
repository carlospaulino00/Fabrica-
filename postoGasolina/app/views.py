from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .models import PostoAtendimento 
from .serializers import ClienteSerializer
from .serializers import PostoAtendimentoSerializer
# Create your views here

class PostoAtendimentoViewSet(viewsets.ModelViewSet):
    queryset = PostoAtendimento .objects.all()
    serializer_class = PostoAtendimentoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer






