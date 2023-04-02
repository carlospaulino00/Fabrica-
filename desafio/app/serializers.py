from rest_framework import serializers
from .models import PostoAtendimento 
from .models import Cliente


class PostoAtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostoAtendimento 
        fields = ['id', 'nome','cpf', 'combustivel','quantidade','valorPago']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome','cpf']



